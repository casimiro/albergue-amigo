# -*- coding: UTF-8 -*-
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

import cherrypy
import Image
import datetime
from sqlalchemy import and_
from albergueamigo.view.ListServices import ListServices
from albergueamigo.view.EditService import EditService
from albergueamigo.view.ViewService import ViewService
from albergueamigo.view.ListTouristicSites import ListTouristicSites
from albergueamigo.view.EditTouristicSite import EditTouristicSite
from albergueamigo.view.ViewTouristicSite import ViewTouristicSite
from albergueamigo.view.Index import Index
from albergueamigo.view.UserPage import UserPage
from albergueamigo.view.UserLogin import UserLogin
from albergueamigo.view.EditHotel import EditHotel
from albergueamigo.view.EditUser import EditUser
from albergueamigo.view.ListHotels import ListHotels
from albergueamigo.view.ViewHotel import ViewHotel
from albergueamigo.model.models import *
from shutil import copyfileobj

class ServiceController(object):
    
    @cherrypy.expose
    def view(self, id):
        service = Session().query(Service).get(id)
        return ViewService(searchList=[{'service':service,'user':get_logged_user(), 'last_hotels':get_last_hotels()}]).respond()
    
    @cherrypy.expose
    def index(self):
        services = Session().query(Service).all()
        return ListServices(searchList=[{'services':services,'user':get_logged_user(), 'last_hotels':get_last_hotels()}]).respond()
    @cherrypy.expose    
    def edit(self, id = None, **kwargs):
        if id:
            service = Session().query(Service).get(id)
        else:
            service = Service()
        fs = None
        if kwargs:
            fs = ServiceFieldSet.bind(service, data = kwargs.items())
            if fs.validate():
                fs.sync()
                service.save()
                return self.index()
            
        if not fs:
            fs = ServiceFieldSet.bind(service)
            
        return EditService(searchList=[{'fs':fs.render(),'user':get_logged_user(), 'last_hotels':get_last_hotels()}]).respond()

class TouristicSiteController(object):
    
    @cherrypy.expose
    def view(self, id):
        site = Session().query(TouristicSite).get(id)
        return ViewTouristicSite(searchList=[{'site':site,'user':get_logged_user(), 'last_hotels':get_last_hotels()}]).respond()
    @cherrypy.expose
    def index(self):
        site = Session().query(TouristicSite).all()
        return ListTouristicSites(searchList=[{'last_hotels':get_last_hotels(),'sites':site,'user':get_logged_user()}]).respond()
    
    @cherrypy.expose
    def edit(self, id = None, **kwargs):
        fs = None
        if id:
            site = Session().query(TouristicSite).get(id)
        else:
            site = TouristicSite()
        if kwargs:
            fs = TouristicSiteFieldSet.bind(site,data = kwargs.items())
            if fs.validate():
                fs.sync()
                site.save()
                return self.index()
        if fs is None:
            fs = TouristicSiteFieldSet.bind(site)
        return EditTouristicSite(searchList=[{'last_hotels':get_last_hotels(),'fs':fs.render(),'user':get_logged_user()}]).respond()

class UserController(object):
    
    @cherrypy.expose
    def edit(self, **kwargs):
        if 'User--name' in kwargs:
            user = User(name = kwargs['User--name'],
                        email = kwargs['User--email'],
                        password = kwargs['User--password'],
                        username = kwargs['User--username'],
                        max_diaria = kwargs['User--max_diaria'],
                        hotel_fim = kwargs['User--hotel_fim'],
                        creation_date = datetime.date.today(),
                        cpf = kwargs['User--cpf'])
            user.save()
            return self.login()
        return EditUser(searchList=[{'last_hotels':get_last_hotels(),'fs':UserFieldSet.render(),'user':get_logged_user()}]).respond()
    
    @cherrypy.expose
    def logout(self):
        if 'user' in cherrypy.session.keys():
            cherrypy.session['user'] = None
            return RootController().index()
    @cherrypy.expose
    def login(self, **kwargs):
        if 'username' in kwargs:
            user = Session.query(User).filter(and_(User.username==kwargs['username'],User.password==kwargs['password']))
            
            if user is not None and user.count() == 1:
                cherrypy.session['user'] = user.first()
                return Index(searchList=[{'last_hotels':get_last_hotels(),'user':get_logged_user()}]).respond()
            else:
                return self.login()
                
        return UserLogin(searchList=[{'last_hotels':get_last_hotels(),'user':get_logged_user()}]).respond()

def resize_image(src):
    img = Image.open(src)
    lim = 500.0,480.0
    dim = img.size
    ratio = min(lim[0]/dim[0],lim[1]/dim[1])
    print ratio
    if ratio >= 1:
        return
    img2 = img.resize((dim[0]*ratio,dim[1]*ratio))
    img2.save(src)
    
class HotelController(object):
    """This class will handle the hotels HTTP requests """
    
    def save_image(self, file, dist):
        os.remove(dist)
        f = open(dist, 'wb')
        data = file
        data.seek(0) # just to ensure we're at the beginning
        copyfileobj(fsrc=data, fdst=f, length=1024 * 8)
        f.close()
        resize_image(dist)
    
    @cherrypy.expose
    def edit(self,id = None, **kwargs):
        if id:
            hotel = Session().query(Hotel).get(id)
        else:
            hotel = Hotel()
        fs = None
        # if POST
        if kwargs:
            if id:
                img_key = 'Hotel-'+str(id)+'-imagem'
            else:
                img_key = 'Hotel--imagem'
            
            if kwargs[img_key] and kwargs[img_key].filename != '':
                file = kwargs[img_key].file
                dist = 'static/images/'+str(get_last_hotel_id())+'.jpg'
                self.save_image(file, dist)
                kwargs[img_key] = dist[6:]
             
            fs = HotelFieldSet.bind(hotel, data = kwargs.items())
            if fs.validate():
                fs.sync()
                hotel.save()
                return self.index()
        if not fs:
            fs = HotelFieldSet.bind(hotel)
        return EditHotel(searchList=[{'last_hotels':get_last_hotels(),'fs':fs.render(),'user':get_logged_user()}]).respond()

    @cherrypy.expose
    def view(self, hotel_id):
        hotel = Session().query(Hotel).get(hotel_id)
        nearby_sites = get_touristic_sites_near_to(hotel, 200)
        return ViewHotel(searchList=[{'nearby_sites':nearby_sites, 'last_hotels':get_last_hotels(),'hotel':hotel,'user':get_logged_user()}]).respond()
    
    @cherrypy.expose
    def index(self):
        hotels = Session().query(Hotel).all()
        return ListHotels(searchList=[{'last_hotels':get_last_hotels(),'hotels':hotels,'user':get_logged_user()}]).respond()
    
class RootController(object):
    """This class will handle root requests"""
    hotels = HotelController()
    users = UserController()
    sites = TouristicSiteController()
    services = ServiceController()
    @cherrypy.expose
    def index(self):
        session = Session()
        zl = session.query(Hotel).filter(Hotel.regiao==HotelRegiao.LESTE).all()
        zo = session.query(Hotel).filter(Hotel.regiao=='Zona Oeste').all()
        zs = session.query(Hotel).filter(Hotel.regiao==HotelRegiao.SUL).all()
        zn = session.query(Hotel).filter(Hotel.regiao==HotelRegiao.NORTE).all()
        print zo
        return Index(searchList=[{'zl':zl,
                                  'zo':zo,
                                  'zs':zs,
                                  'zn':zn,
                                  'last_hotels':get_last_hotels(),
                                  'user':get_logged_user()}]).respond()

def get_logged_user():
    if 'user' in cherrypy.session.keys():
        return cherrypy.session['user']
    return None

def remove_prefix_from_dict(dict):
    new_dict = {}
    for k,v in dict.items():
        new_dict[k[k.rfind('-')+1:]] = v
    return new_dict

if __name__ == '__main__':
    from sqlalchemy import create_engine
    #Creating infrastructure
    engine = create_engine('sqlite:///fuck.db',echo=True)
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    
    cherrypy.quickstart(RootController(),config='server.config')