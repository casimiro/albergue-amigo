# -*- coding: UTF-8 -*-
import urllib2
import urllib
import simplejson as json
from sqlalchemy import Column,String,Integer,Float,Date,Unicode
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.declarative import declarative_base
from formalchemy import FieldSet,Field,PasswordFieldRenderer
from formalchemy.fields import FileFieldRenderer
from distance import vinc_dist

Session = scoped_session(sessionmaker())
Base = declarative_base()


class HotelRegiao(object):
    """Enum of Zona"""
    OESTE = 'Oeste'
    SUL = 'Sul'
    NORTE = 'Norte'
    LESTE = 'Leste'
    
    def get_values(self):
        return {'Zona Oeste':'Oeste','Zona Sul':'Sul','Zona Norte':'Norte','Zona Leste':'Leste'}

class HotelTipo(object):
    """Enum of hotel types """
    FAMILIAR = 'Familiar'
    INDIVIDUAL = 'Individual'
    
    def get_values(self):
        return {'Familiar':'Familiar','Individual':'Individual'}

class HotelFim(object):
    """Enum of hotel propose"""
    NEGOCIOS = 'Business'
    LAZER = 'Lazer'
    
    def get_values(self):
        return {'Business':'Business','Lazer':'Lazer'}

class TouristicSite(Base):
    __tablename__ = 'site'
    
    id = Column('id',Integer, primary_key=True)
    name = Column(Unicode, nullable = False)
    value = Column(Float)
    hours = Column(Unicode, nullable = False)
    address = Column(Unicode, nullable = False)
    cep = Column(String, nullable = False)
    latitude = Column(Float,nullable = False)
    longitude = Column(Float,nullable = False)
    url = Column(String)
    
    def save(self):
        if self.latitude == None:
            coord = _get_coordinates(self.address,self.cep)
            self.latitude = coord['lat']
            self.longitude = coord['lng']
        session = Session()
        session.add(self)
        session.commit()

class Service(Base):
    __tablename__ = 'service'
    
    id = Column(Integer,primary_key=True)
    name = Column(Unicode, nullable = False)
    hours = Column(Unicode, nullable = False)
    address = Column(Unicode, nullable = False)
    cep = Column(String, nullable = False)
    latitude = Column(Float,nullable = False)
    longitude = Column(Float,nullable = False)
    
    def save(self):
        if self.latitude == None:
            coord = _get_coordinates(self.address,self.cep)
            self.latitude = coord['lat']
            self.longitude = coord['lng']
        session = Session()
        session.add(self)
        session.commit()
        
class User(Base):
    __tablename__ = 'user'
    
    id = Column('id',Integer, primary_key=True)
    name = Column(Unicode, nullable = False)
    username = Column(String)
    email = Column(String,nullable=False)
    password = Column(String(40), nullable=False)
    cpf = Column(String)
    creation_date = Column(Date, nullable=False)
    max_diaria = Column(Float)
    hotel_fim = Column(String)
    
    def __repr__(self):
        return '<User "%s">' % (self.__dict__)
    
    def save(self):
        session = Session()
        session.add(self)
        session.commit()
        
class Hotel(Base):
    __tablename__ = 'hotel'
    
    id = Column(Integer, primary_key=True)
    nome = Column(Unicode, nullable = False)
    endereco = Column(Unicode, nullable = False)
    cep = Column(String, nullable = False)
    latitude = Column(Float, nullable = False)
    longitude = Column(Float, nullable = False)
    regiao = Column(String, nullable = False)
    classificacao = Column(Integer, nullable = False)
    finalidade = Column(String, nullable = False)
    custo_diaria = Column(Float)
    tipo = Column(String, nullable = False)
    imagem = Column(String)
    url = Column(String)

    def __repr__(self):
        return '<Hotel "%s">' % (self.__dict__)

    def __eq__(self, other):
        return self.id == other.id
    
    def update(self,d):
        self.nome = d['nome']
        self.endereco = d['endereco']
        self.cep = d['cep']
        self.regiao = d['regiao']
        self.classificacao = d['classificacao']
        self.finalidade = d['finalidade']
        self.custo_diaria = d['custo_diaria']
        self.tipo = d['tipo']
        self.url = d['url']
        if 'imagem' in d.keys():
            self.imagem = d['imagem']
        
        self.save()
    def save(self):
        if self.latitude == None:
            coord = _get_coordinates(self.endereco,self.cep)
            self.latitude = coord['lat']
            self.longitude = coord['lng']
        session = Session()
        session.add(self)
        session.commit()

def _get_coordinates(address,cep):
    #This function get the coordinates for a 
    #cep in são paulo
    address = urllib.quote(address)
    
    resp = urllib2.urlopen("http://maps.google.com/maps/api/geocode/json?address="+address+"+"+cep+"+S%C3%83O%20PAULO+SP&sensor=false")
    payload = resp.read()    
    data = json.loads(payload)
    return data['results'][0]['geometry']['location']


def get_touristic_sites_near_to(hotel,distance):
    sites = Session().query(TouristicSite).all()
    choosen = {}
    
    for site in sites:
        d = vinc_dist(hotel.latitude,hotel.longitude,site.latitude,site.longitude)
        if d <= distance:
            choosen[site] = d 
    return choosen

def get_last_hotel_id():
    r = Session().query(Hotel.id).order_by(Hotel.id)[0][0]
    print r
    return r

#This function returns the last 5 hotels stored in the system
def get_last_hotels():
    return Session().query(Hotel).all()[-5:]

#Hotel's FieldSet
HotelFieldSet = FieldSet(Hotel)
HotelFieldSet.append(Field('regiao').dropdown(options=HotelRegiao().get_values()))
HotelFieldSet.append(Field('finalidade').dropdown(options=HotelFim().get_values()))
HotelFieldSet.append(Field('tipo').dropdown(options=HotelTipo().get_values()))
HotelFieldSet.append(Field(name='imagem').with_renderer(FileFieldRenderer))
HotelFieldSet.configure(exclude=[HotelFieldSet.latitude,HotelFieldSet.longitude])

#User's FieldSet
UserFieldSet = FieldSet(User)
UserFieldSet.insert_after(UserFieldSet.password, Field(name='password2').with_renderer(PasswordFieldRenderer))
UserFieldSet.append(Field(name='password').with_renderer(PasswordFieldRenderer))
UserFieldSet.append(Field('hotel_fim').dropdown(options=HotelFim().get_values()))
UserFieldSet.configure(exclude=[UserFieldSet.creation_date])

#TouristicSite's FieldSet
TouristicSiteFieldSet = FieldSet(TouristicSite)
TouristicSiteFieldSet.configure(exclude=[TouristicSiteFieldSet.latitude,TouristicSiteFieldSet.longitude])

#Service's FieldSet
ServiceFieldSet = FieldSet(Service)
ServiceFieldSet.configure(exclude=[ServiceFieldSet.latitude,ServiceFieldSet.longitude])