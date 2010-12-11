# -*- coding: UTF-8 -*-
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

import cherrypy
import Image
import datetime
from sqlalchemy import and_
from albergueamigo.view.ListTouristicSites import ListTouristicSites
from albergueamigo.view.EditTouristicSite import EditTouristicSite
from albergueamigo.view.Index import Index
from albergueamigo.view.UserPage import UserPage
from albergueamigo.view.UserLogin import UserLogin
from albergueamigo.view.EditHotel import EditHotel
from albergueamigo.view.EditUser import EditUser
from albergueamigo.view.ListHotels import ListHotels
from albergueamigo.view.ViewHotel import ViewHotel
from albergueamigo.model.models import *
from shutil import copyfileobj

class TouristicSiteController(object):
    
    @cherrypy.expose
    def index(self):
        site = Session().query(TouristicSite).all()
        return ListTouristicSites(searchList=[{'last_hotels':get_last_hotels(),'sites':site,'user':get_logged_user()}]).respond()
    
    @cherrypy.expose
    def edit(self, **kwargs):
        if 'TouristicSite--name' in kwargs:
            site = TouristicSite(name=kwargs['TouristicSite--name'],
                                 value=kwargs['TouristicSite--value'],
                                 hours=kwargs['TouristicSite--hours'],
                                 address=kwargs['TouristicSite--address'],
                                 cep=kwargs['TouristicSite--cep'],
                                 url=kwargs['TouristicSite--url'])
            site.save()
            return self.index()
        return EditTouristicSite(searchList=[{'last_hotels':get_last_hotels(),'fs':TouristicSiteFieldSet.render(),'user':get_logged_user()}]).respond()

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
            hotel = Hotel
        if kwargs:
            params = remove_prefix_from_dict(kwargs)
            
            if 'imagem' in params.keys():
                file = params['imagem'].file
                dist = 'static/images/'+str(get_last_hotel_id())+'.jpg'
                self.save_image(file, dist)
                params['imagem'] = dist[6:]
            if id:
                hotel.update(params)
            else:
                hotel = Hotel(**params)
                hotel.save()
            return self.index()
        fs = HotelFieldSet
        fs = fs.bind(hotel)
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
    
    @cherrypy.expose
    def index(self):
        return Index(searchList=[{'last_hotels':get_last_hotels(),'user':get_logged_user()}]).respond()

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