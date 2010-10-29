import sys
import unittest
sys.path.insert(0,'../src/')

from albergueamigo.model.models import Hotel,Zona,HotelFim,HotelTipo

class HotelTest(unittest.TestCase):
    """This class just test the class Hotel!"""
    
    def setUp(self):
        self.hotel = Hotel(nome='Pocilga ZL',
                      endereco='Av. Assis Ribeiro, 1000',
                      regiao=Zona.OESTE,
                      classificacao=5,
                      finalidade=HotelFim.NEGOCIOS,
                      custo_diaria = 30.0,
                      tipo=HotelTipo.FAMILIAR,
                      url='www.pocilgazl.com')
        
    

    def test_create_hotel(self):
        """Test Constructor creation """ 
        # Asserting the Constructor
        self.assertEquals(self.hotel.nome,'Pocilga ZL')
        self.assertEquals(self.hotel.endereco,'Av. Assis Ribeiro, 1000')
        self.assertEquals(self.hotel.regiao,Zona.OESTE)             
        self.assertEquals(self.hotel.classificacao,5)
        self.assertEquals(self.hotel.finalidade,HotelFim.NEGOCIOS)
        self.assertEquals(self.hotel.custo_diaria,30.0)
        self.assertEquals(self.hotel.tipo,HotelTipo.FAMILIAR)
        self.assertEquals(self.hotel.url,'www.pocilgazl.com')


    
