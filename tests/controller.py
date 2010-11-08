import sys
sys.path.insert(0,'../src/')

import unittest
from sqlalchemy import create_engine
from formalchemy import FieldSet
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
        #Creating infrastrucrure
        engine = create_engine('sqlite:///:memory:',echo=True)
        Session.configure(bind=engine)
        Base.metadata.create_all(engine)

    def test_create_hotel(self):
        controller = HotelController()
        session = Session()
        #Asserting that Controller returns a Form
        result = controller.edit()
        self.assertEquals(result,EditHotel(searchList=[{'fs':FieldSet(Hotel).render()}]).respond())
        
        #Asserting that Controller creates a Hotel
        result = controller.edit(nome='Pocilga ZL',
                                      endereco='Av. Assis Ribeiro',
                                      regiao=HotelRegiao.LESTE,
                                      classificacao=5,
                                      finalidade=HotelFim.NEGOCIOS,
                                      custo_diaria=20.0,
                                      tipo=HotelTipo.INDIVIDUAL, 
                                      url='')
        hotel = session.query(Hotel).first()
        self.assertEquals(hotel.nome,'Pocilga ZL')

        self.assertEquals(result,ListHotels(searchList=[{'hotels':session.query(Hotel).all()}]).respond())

unittest.main()