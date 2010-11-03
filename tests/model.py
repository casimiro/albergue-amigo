import sys
import unittest
from elixir import *

sys.path.insert(0,'../src/')
from albergueamigo.model import models
from albergueamigo.model.models import *

class HotelTest(unittest.TestCase):
    """This class just test the class Hotel!"""
    
    def setUp(self):
        setDB('sqlite:///:memory:')
        create_all()

        self.hotel = Hotel(nome=u'Pocilga ZL',
                      endereco=u'Av. Assis Ribeiro, 1000',
                      regiao=HotelRegiao.OESTE,
                      classificacao=5,
                      finalidade=HotelFim.NEGOCIOS,
                      custo_diaria = 30.0,
                      tipo=HotelTipo.FAMILIAR,
                      url=u'www.pocilgazl.com')
        session.commit() 

    def tearDown(self):
        self.hotel.delete()
        session.commit()
    

    def test_create_hotel(self):
        """Test Constructor creation """ 
        # Asserting the Constructor
        self.assertEquals(self.hotel.nome,u'Pocilga ZL')
        self.assertEquals(self.hotel.endereco,u'Av. Assis Ribeiro, 1000')
        self.assertEquals(self.hotel.regiao,HotelRegiao.OESTE)             
        self.assertEquals(self.hotel.classificacao,5)
        self.assertEquals(self.hotel.finalidade,HotelFim.NEGOCIOS)
        self.assertEquals(self.hotel.custo_diaria,30.0)
        self.assertEquals(self.hotel.tipo,HotelTipo.FAMILIAR)
        self.assertEquals(self.hotel.url,u'www.pocilgazl.com')

        session.commit()
        hotel2 = Hotel.query.first()
        self.assertEquals(self.hotel,hotel2)
    
    
