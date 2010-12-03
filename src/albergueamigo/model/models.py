from sqlalchemy import Column,String,Integer,Float,Date
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.declarative import declarative_base
from formalchemy import FieldSet,Field
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

class User(Base):
    __tablename__ = 'user'
    
    username = Column('username', String, primary_key=True)
    email = Column('email', String,nullable=False)
    password = Column('password', String(40), nullable=False)
    name = Column('name',String, nullable = False)
    cpf = Column('cpf',String)
    creation_date = Column('creation_date', Date, nullable=False)
    max_diaria = Column('max_diaria',Float)
    hotel_fim = Column('hotel_fim', String)
    
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
        session = Session()
        session.add(self)
        session.commit()

#Hotel's FieldSet
HotelFieldSet = FieldSet(Hotel)
HotelFieldSet.append(Field('regiao').dropdown(options=HotelRegiao().get_values()))
HotelFieldSet.append(Field('finalidade').dropdown(options=HotelFim().get_values()))
HotelFieldSet.append(Field('tipo').dropdown(options=HotelTipo().get_values()))

#User's FieldSet
UserFieldSet = FieldSet(User)
UserFieldSet.configure(exclude=[UserFieldSet.creation_date])
UserFieldSet.append(Field('password', renderer='password'))
UserFieldSet.insert(UserFieldSet.password, Field('password2',renderer='password'))
