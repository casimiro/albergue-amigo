import sys
from albergueamigo.view.ViewHotel import ViewHotel
sys.path.insert(0,'../src/')

import unittest
from sqlalchemy import create_engine
from formalchemy import FieldSet
from albergueamigo.view.EditHotel import EditHotel
from albergueamigo.view.ListHotels import ListHotels
from albergueamigo.model.models import *
from albergueamigo.controller.controllers import *

#Creating infrastrucrure
engine = create_engine('sqlite:///:test.db',echo=True)
Session.configure(bind=engine)
Base.metadata.create_all(engine)

class RootControllerTest(unittest.TestCase):
    """Class that test ControllerTest"""
    
    def test_index(self):
        root_controller = RootController()
        self.assertEquals(root_controller.index(),'Hello Bitches!')

class UserControllerTest(unittest.TestCase):
    
    def test_user_creation(self):
        controller = UserController()
        result = controller.edit()
        self.assertEquals(EditUser(searchList=[{'fs':UserFieldSet.render()}]))

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
