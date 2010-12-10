# -*- coding: UTF-8 -*-
import sys
import unittest
import datetime
from sqlalchemy import *

sys.path.insert(0,'../src/')
from albergueamigo.model.models import *

engine = create_engine('sqlite:///:memory:',echo=False)
Session.configure(bind=engine)
Base.metadata.create_all(engine)

class TouristicSiteTest(unittest.TestCase):
    
    def setUp(self):
        Session().query(TouristicSite).delete()
        
    def test_touristic_site_creation(self):
        site = TouristicSite(name='EACH-USP',
                             value=0.0,
                             hours='8h-18h',
                             address=u'Av. Pedroso de Morais, 1341',
                             cep='05419-000',
                             url='www.each.usp.br')
        site.save()
        site_saved = Session().query(TouristicSite).first()
        self.assertEquals(site,site_saved)
        
        self.assertEquals(-23.5593858,site_saved.latitude)
        self.assertEquals(-46.6966822,site_saved.longitude)
        
    def test_touristic_site_field_set(self):
        site_fs = TouristicSiteFieldSet
        keys = site_fs.render_fields.keys()
        self.assertTrue('name' in keys)
        self.assertTrue('value' in keys)
        self.assertTrue('hours' in keys)
        self.assertTrue('address' in keys)
        self.assertTrue('url' in keys)
        self.assertFalse('latitude' in keys)
        self.assertFalse('longitude' in keys)
        
    def test_get_touristic_sites_near_to(self):
        # The function get_touristic_sites_near_to
        # receives lat,lng,region and a limit in meters
        # which represents the max distance wished
        site = TouristicSite(name='EACH-USP',
                             value=0.0,
                             hours='8h-18h',
                             address=u'Av. Pedroso de Morais, 1341',
                             cep='05419-000',
                             url='www.colegiopalmares.com.br')
        site1 = TouristicSite(name='EACH-USP',
                             value=0.0,
                             hours='8h-18h',
                             address=u'Av. Pedroso de Morais, 998',
                             cep='05420-001',
                             url='www.subway.com')
        site.save()
        site1.save()
        hotel = Hotel(nome=u'Pocilga ZL',
                      endereco=u'Av. Pedroso de Morais, 1619',
                      cep='05419-001',
                      regiao=HotelRegiao.OESTE,
                      classificacao=5,
                      finalidade=HotelFim.NEGOCIOS,
                      custo_diaria = 30.0,
                      tipo=HotelTipo.FAMILIAR,
                      url=u'www.pocilgazl.com') 
        hotel.save()
        
        distances = get_touristic_sites_near_to(hotel,200)
        self.assertTrue(site in distances.keys())
        self.assertFalse(site1 in distances.keys())
        
        #Asserting the distances
        self.assertEquals(distances[site], 161.608)
    
class ServiceTest(unittest.TestCase):
    
    def test_service_creation(self):
        service = Service(name="Cafeteria",
                          address="Pc Omaguas, 34",
                          cep='05419-020',
                          hours='8h-21h')
        service.save()
        service_saved = Session().query(Service).first()
        self.assertEquals(service, service_saved)
        
        self.assertEquals(service.latitude,-23.5623732)
        self.assertEquals(service.longitude,-46.6920555)
        
    def test_service_field_set(self):
        service_fs = ServiceFieldSet
        keys = service_fs.render_fields.keys()

        self.assertTrue('name' in keys) 
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
        self.assertTrue('username' in keys)
        self.assertFalse('creation_date' in keys)
        
        
class HotelTest(unittest.TestCase):
    """This class just test the class Hotel!"""
    
    def setUp(self):
        Session().query(Hotel).delete()
    
    def test_create_hotel(self):
        #Creating infrastrucrure
        hotel = Hotel(nome=u'Pocilga ZL',
                      endereco=u'Av. Pedroso de Morais, 1619',
                      cep='05419-001',
                      regiao=HotelRegiao.OESTE,
                      classificacao=5,
                      finalidade=HotelFim.NEGOCIOS,
                      custo_diaria = 30.0,
                      tipo=HotelTipo.FAMILIAR,
                      url=u'www.pocilgazl.com') 
        hotel.save()
        
        hotel_saved = Session().query(Hotel).all()[0]
        self.assertEquals(hotel,hotel_saved)
        
        self.assertEquals(-23.5590562,hotel_saved.latitude)
        self.assertEquals(-46.6982242,hotel_saved.longitude)
    
    
    def testCreateHotelForm(self):
        hotel_fs = HotelFieldSet
        keys = hotel_fs.render_fields.keys()
        
        self.assertFalse('latitude' in keys)
        self.assertFalse('longitude' in keys)
        
    def test_get_last_hotels(self):
        #This method must return the 5 last hotels in the system
        hotel = Hotel(nome=u'Pocilga ZL',
                      endereco=u'Av. Pedroso de Morais, 1619',
                      cep='05419-001',
                      regiao=HotelRegiao.OESTE,
                      classificacao=5,
                      finalidade=HotelFim.NEGOCIOS,
                      custo_diaria = 30.0,
                      tipo=HotelTipo.FAMILIAR,
                      url=u'www.pocilgazl.com') 
        hotel.save()
        hotel2 = Hotel(nome=u'Pocilga ZO',
                      endereco=u'Av. Pedroso de Morais, 1619',
                      cep='05419-001',
                      regiao=HotelRegiao.OESTE,
                      classificacao=5,
                      finalidade=HotelFim.NEGOCIOS,
                      custo_diaria = 30.0,
                      tipo=HotelTipo.FAMILIAR,
                      url=u'www.pocilgazl.com') 
        hotel2.save()
        hotel3 = Hotel(nome=u'Pocilga ZS',
                      endereco=u'Av. Pedroso de Morais, 1619',
                      cep='05419-001',
                      regiao=HotelRegiao.OESTE,
                      classificacao=5,
                      finalidade=HotelFim.NEGOCIOS,
                      custo_diaria = 30.0,
                      tipo=HotelTipo.FAMILIAR,
                      url=u'www.pocilgazl.com') 
        hotel3.save()
        hotel4 = Hotel(nome=u'Pocilga ZN',
                      endereco=u'Av. Pedroso de Morais, 1619',
                      cep='05419-001',
                      regiao=HotelRegiao.OESTE,
                      classificacao=5,
                      finalidade=HotelFim.NEGOCIOS,
                      custo_diaria = 30.0,
                      tipo=HotelTipo.FAMILIAR,
                      url=u'www.pocilgazl.com') 
        hotel4.save()
        
        hotels = get_last_hotels()
        
        self.assertEquals(len(hotels),4)
unittest.main()
