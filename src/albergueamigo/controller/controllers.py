# -*- coding: UTF-8 -*-
import os
current_dir = os.path.dirname(os.path.abspath(__file__))

import cherrypy
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

class TouristicSiteController(object):
    
    @cherrypy.expose
    def index(self):
        site = Session().query(TouristicSite).all()
        return ListTouristicSites(searchList=[{'last_hotels':get_last_hotels(),'sites':site}]).respond()
    
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
        return EditTouristicSite(searchList=[{'last_hotels':get_last_hotels(),'fs':TouristicSiteFieldSet.render()}]).respond()

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
        return EditUser(searchList=[{'last_hotels':get_last_hotels(),'fs':UserFieldSet.render()}]).respond()
    
    @cherrypy.expose
    def login(self, **kwargs):
        if 'username' in kwargs:
            user = Session.query(User).filter(and_(User.username==kwargs['username'],User.password==kwargs['password']))
            
            if user is not None and user.count() == 1:
                return UserPage(searchList=[{'last_hotels':get_last_hotels(),'user':user.first()}]).respond()
            else:
                return self.login()
                
        return UserLogin(searchList=[{'last_hotels':get_last_hotels()}]).respond()
    
class HotelController(object):
    """This class will handle the hotels HTTP requests """
    
    @cherrypy.expose
    def edit(self, **kwargs):
        if 'Hotel--nome' in kwargs:
            hotel = Hotel(nome=kwargs['Hotel--nome'],
                         endereco=kwargs['Hotel--endereco'],
                         cep=kwargs['Hotel--cep'],
                         regiao = kwargs['Hotel--regiao'],
                         classificacao = kwargs['Hotel--classificacao'],
                         finalidade=kwargs['Hotel--finalidade'],
                         tipo =kwargs['Hotel--tipo'],
                         custo_diaria=kwargs['Hotel--custo_diaria'],
                         url=kwargs['Hotel--url'])
            hotel.save()
            return self.index()
        return EditHotel(searchList=[{'last_hotels':get_last_hotels(),'fs':HotelFieldSet.render()}]).respond()

    @cherrypy.expose
    def view(self, hotel_id):
        hotel = Session().query(Hotel).get(hotel_id)
        nearby_sites = get_touristic_sites_near_to(hotel, 200)
        return ViewHotel(searchList=[{'nearby_sites':nearby_sites, 'last_hotels':get_last_hotels(),'hotel':hotel}]).respond()
    
    @cherrypy.expose
    def index(self):
        hotels = Session().query(Hotel).all()
        return ListHotels(searchList=[{'last_hotels':get_last_hotels(),'hotels':hotels}]).respond()
    
class RootController(object):
    """This class will handle root requests"""
    hotels = HotelController()
    users = UserController()
    sites = TouristicSiteController()
    
    @cherrypy.expose
    def index(self):
        return Index(searchList=[{'last_hotels':get_last_hotels()}]).respond()
   
if __name__ == '__main__':
    from sqlalchemy import create_engine
    #Creating infrastructure
    engine = create_engine('sqlite:///fuck.db',echo=True)
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    
    cherrypy.quickstart(RootController(),config='server.config')