# -*- coding: UTF-8 -*-
import sys,os
sys.path.insert(0,'../src/')

import unittest
from sqlalchemy import create_engine
from formalchemy import FieldSet
from cherrypy._cpcgifs import FieldStorage
from albergueamigo.view.ViewService import ViewService
from albergueamigo.view.EditService import EditService
from albergueamigo.view.ListServices import ListServices
from albergueamigo.view.ListTouristicSites import ListTouristicSites
from albergueamigo.view.ViewTouristicSite import ViewTouristicSite
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
os.remove('test.db')
engine = create_engine('sqlite:///test.db',echo=False)
Session.configure(bind=engine)
Base.metadata.create_all(engine)

cherrypy.session = {}

class ServiceControllerTest(unittest.TestCase):
    
    def test_service_creation(self):
        controller = ServiceController()
        params = {'Service--name':u'Frans Café',
                  'Service--hours':'8h-21h',
                  'Service--address':'Av. Pedroso de Morais, 1341',
                  'Service--cep':'05419-000'}
        r = controller.edit()
        self.assertEquals(EditService(searchList=[{'fs':ServiceFieldSet.render(),'user':None, 'last_hotels':get_last_hotels()}]).respond(),r)
        
        # Inserting a new service
        controller.edit(**params)
        service_saved = Session().query(Service).first()
        self.assertEquals(service_saved.name, 'Frans Café')
        
        # Editing an existing service
        params = {'Service-1-name':'Teste 2',
                  'Service-1-hours':'8h-21h',
                  'Service-1-address':'Av. Pedroso de Morais, 1341',
                  'Service-1-cep':'05419-000'}
        fs = ServiceFieldSet.bind(service_saved)
        self.assertEquals(EditService(searchList=[{'fs':fs.render(),'user':None, 'last_hotels':get_last_hotels()}]).respond(),
                          controller.edit(service_saved.id))
        controller.edit(id=service_saved.id,**params)
        service_saved = Session().query(Service).first()
        self.assertEquals(service_saved.name,'Teste 2')
        
    def test_index_services(self):
        controller = ServiceController()
        services = Session().query(Service).all()
        self.assertEquals(ListServices(searchList=[{'services':services,'user':None, 'last_hotels':get_last_hotels()}]).respond(),controller.index())
    
    def test_view_service(self):
         controller = ServiceController()
         service = Service(name="Cafeteria",
                          address="Pc Omaguas, 34",
                          cep='05419-020',
                          hours='8h-21h')
         service.save()
         self.assertEquals(ViewService(searchList=[{'service':service,'user':get_logged_user(), 'last_hotels':get_last_hotels()}]).respond(),controller.view(service.id))
        
class RootControllerTest(unittest.TestCase):
    """Class that test ControllerTest"""
    
    def test_index(self):
        root_controller = RootController()
        self.assertEquals(root_controller.index(),Index(searchList=[{'user':None, 'last_hotels':get_last_hotels()}]).respond())
        
    def test_mappings(self):
        #Hotels
        self.assertEquals(type(RootController().hotels),type(HotelController()))
        #Users
        self.assertEquals(type(RootController().users),type(UserController()))
        #TouristicSites
        self.assertEquals(type(RootController().sites),type(TouristicSiteController()))
        #Services
        self.assertEquals(type(RootController().services),type(ServiceController()))
        
class TouristicSiteControllerTest(unittest.TestCase):
    
    def setUp(self):
        Session().query(TouristicSite).delete()
                
    def test_touristic_site_view(self):
        controller = TouristicSiteController()
        site = TouristicSite(name='EACH-USP',
                             value=0.0,
                             hours='8h-18h',
                             address=u'Av. Pedroso de Morais, 1341',
                             cep='05419-000',
                             url='www.each.usp.br')
        site.save()
        self.assertEquals(ViewTouristicSite(searchList=[{'site':site,'user':get_logged_user(), 'last_hotels':get_last_hotels()}]).respond(),controller.view(site.id))
    
    def test_touristic_site_creation(self):
        controller = TouristicSiteController()
        self.assertEquals(controller.edit(),EditTouristicSite(searchList=[{'user':None, 'last_hotels':get_last_hotels(),'fs':TouristicSiteFieldSet.render()}]).respond())
        
        params = {'TouristicSite--name':'EACH-USP',
                  'TouristicSite--value':'0.0',
                  'TouristicSite--hours':'8h-18h',
                  'TouristicSite--address':'Av. Assis Ribeiro',
                  'TouristicSite--cep':'05419-001',
                  'TouristicSite--url':'www.each.usp.br'}
        result = controller.edit(**params)
        self.assertEquals(controller.index(),result)
        
        saved_site = Session().query(TouristicSite).first()
        
        self.assertEquals('EACH-USP',saved_site.name)
        self.assertEquals(0.0,saved_site.value)
        self.assertEquals('8h-18h',saved_site.hours)
        self.assertEquals('Av. Assis Ribeiro',saved_site.address)
        self.assertEquals('www.each.usp.br',saved_site.url)

    def test_edit_touristic_site(self):
        controller = TouristicSiteController()
        site = TouristicSite(name='EACH-USP',
                             value=0.0,
                             hours='8h-18h',
                             address=u'Av. Pedroso de Morais, 1341',
                             cep='05419-000',
                             url='www.each.usp.br')
        site.save()
        params = {'TouristicSite-1-name':'EACH-USP',
                  'TouristicSite-1-value':'0.0',
                  'TouristicSite-1-hours':'8h-18h',
                  'TouristicSite-1-address':'Av. Assis Ribeiro',
                  'TouristicSite-1-cep':'05419-001',
                  'TouristicSite-1-url':'www.each.usp.br'}
        result = controller.edit(site.id)
        fs = TouristicSiteFieldSet.bind(site)
        self.assertEquals(EditTouristicSite(searchList=[{'user':get_logged_user(), 'last_hotels':get_last_hotels(),'fs':fs.render()}]).respond(),result)
        
        
    def test_touristic_site_index(self):
        controller = TouristicSiteController()
        site = TouristicSite(name='EACH-USP',
                             value=0.0,
                             hours='8h-18h',
                             address=u'Av. Pedroso de Morais, 1619',
                             cep='05419-001',
                             url='www.each.usp.br')
        site.save()
        sites = Session().query(TouristicSite).all()
        self.assertEquals(controller.index(),ListTouristicSites(searchList=[{'user':None, 'last_hotels':get_last_hotels(),'sites':sites}]).respond())
        
class UserControllerTest(unittest.TestCase):
    
    def setUp(self):
        #Clearing the mess
        Session.query(User).delete()
        Session.query(Hotel).delete()
    
    def test_user_creation(self):
        controller = UserController()
        
        self.assertEquals(EditUser(searchList=[{'last_hotels':get_last_hotels(),'fs':UserFieldSet.render(),'user':get_logged_user()}]).respond(), controller.edit())
        
        params = {'User--name':'Caio Casimiro', 
                  'User--username':'casimiro',
                  'User--email': 'caiorcasimiro@gmail.com',
                  'User--password':'teste',
                  'User--cpf':'35900763803',
                  'User--max_diaria': 150.0,
                  'User--hotel_fim':'Business'}
        
        self.assertEquals(controller.login(),controller.edit(**params))
        
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
        
        self.assertEquals(controller.login(),UserLogin(searchList=[{'user':None, 'last_hotels':get_last_hotels()}]).respond())
        
        params = {'username':'fulano','password':'teste'}
        result = controller.login(**params)
        self.assertEquals(cherrypy.session['user'],user)      
        
    def test_user_logout(self):
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
        controller.login(**{'username':user.username,'password':user.password})
        self.assertEquals(cherrypy.session['user'],user)
        
        controller.logout()
        self.assertEquals(cherrypy.session['user'],None)
class HotelControllerTest(unittest.TestCase):
    """Class that will assert the controller behavior"""
    
    def test_create_hotel(self):
        controller = HotelController()
        session = Session()
        #Asserting that Controller returns a Form
        result = controller.edit()
        self.assertEquals(result,EditHotel(searchList=[{'user':None, 'last_hotels':get_last_hotels(),'fs':HotelFieldSet.render()}]).respond())
        #Asserting that Controller creates a Hotel
        params = {'Hotel--nome':'Pocilga ZL',
                  'Hotel--regiao':HotelRegiao.OESTE,
                  'Hotel--endereco':'Av. Assis Ribeiro',
                  'Hotel--cep':'05419-001',
                  'Hotel--classificacao':'5',
                  'Hotel--imagem':None,
                  'Hotel--finalidade':HotelFim.NEGOCIOS,
                  'Hotel--custo_diaria':'20.0',
                  'Hotel--tipo':HotelTipo.INDIVIDUAL,
                  'Hotel--url':''}
        result = controller.edit(**params)
        hotel = session.query(Hotel).first()
        self.assertEquals(hotel.nome,'Pocilga ZL')
        self.assertEquals(result,ListHotels(searchList=[{'user':None, 'last_hotels':get_last_hotels(),'hotels':session.query(Hotel).all()}]).respond())
    
    def test_edit_hotel(self):
        controller = HotelController()
        hotel = Hotel(nome=u'Pocilga ZL',
                      endereco=u'Av. Pedroso de Morais, 1619',
                      cep = '05419-001',
                      regiao=HotelRegiao.OESTE,
                      classificacao=5,
                      finalidade=HotelFim.NEGOCIOS,
                      custo_diaria = 30.0,
                      tipo=HotelTipo.FAMILIAR,
                      url=u'www.pocilgazl.com') 
        hotel.save()
        result = controller.edit(id = hotel.id)
        fs = HotelFieldSet
        fs = fs.bind(hotel)
        self.assertEquals(result,EditHotel(searchList=[{'user':None, 'last_hotels':get_last_hotels(),'fs':fs.render()}]).respond())
        
        
        params = {'Hotel-2-nome':'Pocilga ZL',
                  'Hotel-2-endereco':'Av. Assis Ribeiro',
                  'Hotel-2-cep':'05419-001',
                  'Hotel-2-regiao':HotelRegiao.LESTE,
                  'Hotel-2-classificacao':"5",
                  'Hotel-2-imagem':None,
                  'Hotel-2-finalidade':HotelFim.NEGOCIOS,
                  'Hotel-2-custo_diaria':"20.0",
                  'Hotel-2-tipo':HotelTipo.INDIVIDUAL, 
                  'Hotel-2-url':'www.usp.br'}
        controller.edit(id=hotel.id,**params)
        self.assertEquals(hotel.endereco,'Av. Assis Ribeiro')
        self.assertEquals(hotel.url, 'www.usp.br')
        
    def test_view_hotel(self):
        controller = HotelController()
        hotel = Hotel(nome=u'Pocilga ZL',
                      endereco=u'Av. Pedroso de Morais, 1619',
                      cep = '05419-001',
                      regiao=HotelRegiao.OESTE,
                      classificacao=5,
                      finalidade=HotelFim.NEGOCIOS,
                      custo_diaria = 30.0,
                      tipo=HotelTipo.FAMILIAR,
                      url=u'www.pocilgazl.com') 
        hotel.save()
        result = controller.view(hotel.id)
        nearby_sites = get_touristic_sites_near_to(hotel,200)
        self.assertEquals(result,ViewHotel(searchList=[{'user':None, 'nearby_sites':nearby_sites,'last_hotels':get_last_hotels(),'hotel':hotel}]).respond())
        
unittest.main()

