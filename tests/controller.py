import sys

sys.path.insert(0,'../src/')

import unittest
from elixir import *
from albergueamigo.view.EditHotel import EditHotel
from albergueamigo.view.ListHotels import ListHotels
from albergueamigo.model.models import *
from albergueamigo.controller.controllers import *

class RootControllerTest(unittest.TestCase):
    """Class that test ControllerTest"""
    
    def test_index(self):
        root_controller = RootController()
        self.assertEquals(root_controller.index(),'Hello Bitches!')
    

class HotelControllerTest(unittest.TestCase):
    """Class that will assert the controller behavior"""
    
    def setUp(self):
        setDB('sqlite:///:memory:')
        create_all()

    def test_create_hotel(self):
        controller = HotelController()
        
        #Asserting that Controller returns a Form
        result = controller.edit()
        self.assertEquals(result,EditHotel().respond())
        
        #Asserting that Controller creates a Hotel
        result = controller.edit(nome='Pocilga ZL',
                                      endereco='Av. Assis Ribeiro',
                                      regiao=HotelRegiao.LESTE,
                                      classificacao=5,
                                      finalidade=HotelFim.NEGOCIOS,
                                      custo_diaria=20.0,
                                      tipo=HotelTipo.INDIVIDUAL, 
                                      url='')
        hotel = Hotel.query.first()
        self.assertEquals(hotel.nome,'Pocilga ZL')

        self.assertEquals(result,ListHotels(searchList=[{'hotels':Hotel.query.all()}]).respond())
