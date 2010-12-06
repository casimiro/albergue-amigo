# -*- coding: UTF-8 -*-
import sys,os
sys.path.insert(0,'../src/')

import unittest
from sqlalchemy import create_engine
from formalchemy import FieldSet
from albergueamigo.view.ListTouristicSites import ListTouristicSites
from albergueamigo.view.EditTouristicSite import EditTouristicSite
from albergueamigo.view.Index import Index
from albergueamigo.view.UserPage import UserPage
from albergueamigo.view.UserLogin import UserLogin
from albergueamigo.view.ViewHotel import ViewHotel
from albergueamigo.view.EditHotel import EditHotel
from albergueamigo.view.ListHotels import ListHotels
from albergueamigo.model.models import *
from albergueamigo.controller.controllers import *

#Creating infrastrucrure
os.remove(':test.db')
engine = create_engine('sqlite:///:test.db',echo=False)
Session.configure(bind=engine)
Base.metadata.create_all(engine)

class RootControllerTest(unittest.TestCase):
    """Class that test ControllerTest"""
    
    def test_index(self):
        root_controller = RootController()
        self.assertEquals(root_controller.index(),Index().respond())
        
    def test_mappings(self):
        #Hotels
        self.assertEquals(type(RootController().hotels),type(HotelController()))
        #Users
        self.assertEquals(type(RootController().users),type(UserController()))
        #TouristicSites
        self.assertEquals(type(RootController().sites),type(TouristicSiteController()))
        
class TouristicSiteControllerTest(unittest.TestCase):
    
    def test_touristic_site_creation(self):
        controller = TouristicSiteController()
        self.assertEquals(controller.edit(),EditTouristicSite(searchList=[{'fs':TouristicSiteFieldSet.render()}]).respond())
        
        params = {'TouristicSite--name':'EACH-USP',
                  'TouristicSite--value':0.0,
                  'TouristicSite--hours':'8h-18h',
                  'TouristicSite--address':'Av. Assis Ribeiro',
                  'TouristicSite--url':'www.each.usp.br'}
        result = controller.edit(**params)
        self.assertEquals(controller.index(),result)
        
        saved_site = Session().query(TouristicSite).first()
        
        self.assertEquals('EACH-USP',saved_site.name)
        self.assertEquals(0.0,saved_site.value)
        self.assertEquals('8h-18h',saved_site.hours)
        self.assertEquals('Av. Assis Ribeiro',saved_site.address)
        self.assertEquals('www.each.usp.br',saved_site.url)

    def test_touristic_site_index(self):
        controller = TouristicSiteController()
        site = TouristicSite(name='EACH-USP',
                             value=0.0,
                             hours='8h-18h',
                             address=u'Av. Assis Ribeiro,1000 - São Miguel Paulista',
                             url='www.each.usp.br')
        site.save()
        sites = Session().query(TouristicSite).all()
        self.assertEquals(controller.index(),ListTouristicSites(searchList=[{'sites':sites}]).respond())
        
class UserControllerTest(unittest.TestCase):
    
    def setUp(self):
        #Clearing the mess
        Session.query(User).delete()
        Session.query(Hotel).delete()
    
    def test_user_creation(self):
        controller = UserController()
        
        self.assertEquals(EditUser(searchList=[{'fs':UserFieldSet.render()}]).respond(), controller.edit())
        
        params = {'User--name':'Caio Casimiro', 
                  'User--username':'casimiro',
                  'User--email': 'caiorcasimiro@gmail.com',
                  'User--password':'teste',
                  'User--cpf':'35900763803',
                  'User--max_diaria': 150.0,
                  'User--hotel_fim':'Business'}
        
        self.assertEquals(UserLogin().respond(),controller.edit(**params))
        
        user = Session().query(User).first()
        self.assertEquals('Caio Casimiro',user.name)
        
    def test_login(self):
        controller = UserController()
        user = User(username='fulano',
                    email='teste@gmail.com',
                    password='teste',
                    creation_date=datetime.date.today(),
                    name='Fulano de Tal',
                    cpf='35900763803',
                    max_diaria=20,
                    hotel_fim=HotelFim.NEGOCIOS
                    )
        user.save()
        
        self.assertEquals(controller.login(),UserLogin().respond())
        
        params = {'username':'fulano','password':'teste'}
        result = controller.login(**params)
        
        self.assertEquals(UserPage(searchList=[{'user':user}]).respond(),result)
        
class HotelControllerTest(unittest.TestCase):
    """Class that will assert the controller behavior"""
        
    def test_create_hotel(self):
        controller = HotelController()
        session = Session()
        #Asserting that Controller returns a Form
        result = controller.edit()
        self.assertEquals(result,EditHotel(searchList=[{'fs':HotelFieldSet.render()}]).respond())
        #Asserting that Controller creates a Hotel
        params = {'Hotel--nome':'Pocilga ZL',
                                      'Hotel--endereco':'Av. Assis Ribeiro',
                                      'Hotel--regiao':HotelRegiao.LESTE,
                                      'Hotel--classificacao':5,
                                      'Hotel--finalidade':HotelFim.NEGOCIOS,
                                      'Hotel--custo_diaria':20.0,
                                      'Hotel--tipo':HotelTipo.INDIVIDUAL, 
                                      'Hotel--url':''}
        result = controller.edit(**params)
        hotel = session.query(Hotel).first()
        self.assertEquals(hotel.nome,'Pocilga ZL')
        self.assertEquals(result,ListHotels(searchList=[{'hotels':session.query(Hotel).all()}]).respond())
    
    def test_view_hotel(self):
        controller = HotelController()
        hotel = Hotel(nome=u'Pocilga ZL',
                      endereco=u'Av. Assis Ribeiro, 1000',
                      regiao=HotelRegiao.OESTE,
                      classificacao=5,
                      finalidade=HotelFim.NEGOCIOS,
                      custo_diaria = 30.0,
                      tipo=HotelTipo.FAMILIAR,
                      url=u'www.pocilgazl.com') 
        hotel.save()
        result = controller.view(hotel.id)
        self.assertEquals(result,ViewHotel(searchList=[{'hotel':hotel}]).respond())
        
unittest.main()
