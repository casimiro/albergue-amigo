import sys
import unittest
from sqlalchemy import *

sys.path.insert(0,'../src/')
from albergueamigo.model.models import *

class HotelTest(unittest.TestCase):
    """This class just test the class Hotel!"""
    
    def test_create_hotel(self):
        #Creating infrastrucrure
        engine = create_engine('sqlite:///:memory:',echo=True)
        Session.configure(bind=engine)
        Base.metadata.create_all(engine)
        
        hotel = Hotel(nome=u'Pocilga ZL',
                      endereco=u'Av. Assis Ribeiro, 1000',
                      regiao=HotelRegiao.OESTE,
                      classificacao=5,
                      finalidade=HotelFim.NEGOCIOS,
                      custo_diaria = 30.0,
                      tipo=HotelTipo.FAMILIAR,
                      url=u'www.pocilgazl.com') 
        hotel.save()
        
        hotel_saved = Session().query(Hotel).all()[0]
        self.assertEquals(hotel,hotel_saved)
    
    def testCreateHotelForm(self):
        fs = HotelFieldSet
unittest.main()
