import sys
import unittest
import datetime
from sqlalchemy import *

sys.path.insert(0,'../src/')
from albergueamigo.model.models import *

engine = create_engine('sqlite:///:memory:',echo=True)
Session.configure(bind=engine)
Base.metadata.create_all(engine)

class UserTest(unittest.TestCase):
    
    def test_user_creation(self):
        #Creating infrastrucrure
        user = User(
                    username='fulano',
                    email='teste@gmail.com',
                    password='teste',
                    creation_date=datetime.date.today(),
                    name='Fulano de Tal',
                    cpf='35900763803',
                    max_diaria=20,
                    hotel_fim=HotelFim.NEGOCIOS
                    )
        user.save()
        user_saved = Session().query(User).first()
        self.assertEquals(user,user_saved)
    
    def test_user_fieldset_creation(self):
        user_fs = UserFieldSet
        keys = user_fs.render_fields.keys()
        self.assertTrue('name' in keys)
        self.assertTrue('password' in keys)
        self.assertTrue('password2' in keys)
        self.assertTrue('email' in keys)
        self.assertTrue('max_diaria' in keys)
        self.assertTrue('cpf' in keys)
        self.assertFalse('creation_date' in keys)
        
        print user_fs.render()
        
class HotelTest(unittest.TestCase):
    """This class just test the class Hotel!"""
    
    def test_create_hotel(self):
        #Creating infrastrucrure
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
