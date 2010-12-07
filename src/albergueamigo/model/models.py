# -*- coding: UTF-8 -*-
import urllib2
import simplejson as json
from sqlalchemy import Column,String,Integer,Float,Date
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.declarative import declarative_base
from formalchemy import FieldSet,Field,PasswordFieldRenderer
from hashed_property import HashedProperty

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
    name = Column(String, nullable = False)
    value = Column(Float)
    hours = Column(String, nullable = False)
    address = Column(String, nullable = False)
    cep = Column(String, nullable = False)
    latitude = Column(Float,nullable = False)
    longitude = Column(Float,nullable = False)
    url = Column(String)
    
    def save(self):
        if self.latitude == None:
            coord = _get_coordinates(self.cep)
            self.latitude = coord['lat']
            self.longitude = coord['lng']
        session = Session()
        session.add(self)
        session.commit()
    
class User(Base):
    __tablename__ = 'user'
    
    id = Column('id',Integer, primary_key=True)
    name = Column(String, nullable = False)
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
    
    id = Column('id',Integer, primary_key=True)
    nome = Column('nome',String, nullable = False)
    endereco = Column('endereco',String, nullable = False)
    cep = Column('cep',String, nullable = False)
    latitude = Column(Float, nullable = False)
    longitude = Column(Float, nullable = False)
    regiao = Column('regiao',String, nullable = False)
    classificacao = Column('classificacao',Integer, nullable = False)
    finalidade = Column('finalidade',String, nullable = False)
    custo_diaria = Column('custo_diaria',Float)
    tipo = Column('tipo',String, nullable = False)
    url = Column('url',String)

    def __repr__(self):
        return '<Hotel "%s">' % (self.__dict__)

    def __eq__(self, other):
        return self.id == other.id

    def save(self):
        if self.latitude == None:
            coord = _get_coordinates(self.cep)
            self.latitude = coord['lat']
            self.longitude = coord['lng']
        session = Session()
        session.add(self)
        session.commit()

def _get_coordinates(cep):
    #This function get the coordinates for a 
    #cep in são paulo
    resp = urllib2.urlopen("http://maps.google.com/maps/api/geocode/json?address="+cep+"+S%C3%83O%20PAULO+SP&sensor=false")
    payload = resp.read()    
    data = json.loads(payload)
    return data['results'][0]['geometry']['location']


#This function returns the last 5 hotels stored in the system
def get_last_hotels():
    return Session().query(Hotel).all()[-5:]

#Hotel's FieldSet
HotelFieldSet = FieldSet(Hotel)
HotelFieldSet.append(Field('regiao').dropdown(options=HotelRegiao().get_values()))
HotelFieldSet.append(Field('finalidade').dropdown(options=HotelFim().get_values()))
HotelFieldSet.append(Field('tipo').dropdown(options=HotelTipo().get_values()))

#User's FieldSet
UserFieldSet = FieldSet(User)
UserFieldSet.insert_after(UserFieldSet.password, Field(name='password2').with_renderer(PasswordFieldRenderer))
UserFieldSet.append(Field(name='password').with_renderer(PasswordFieldRenderer))
UserFieldSet.append(Field('hotel_fim').dropdown(options=HotelFim().get_values()))
UserFieldSet.configure(exclude=[UserFieldSet.creation_date])

#TouristicSite's FieldSet
TouristicSiteFieldSet = FieldSet(TouristicSite)

