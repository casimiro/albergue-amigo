from sqlalchemy import Column,String,Integer,Float
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.declarative import declarative_base
from formalchemy import FieldSet,Field

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

class Hotel(Base):
    """This class is a model and represents a Hotel!"""
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

HotelFieldSet = FieldSet(Hotel)
HotelFieldSet.append(Field('regiao').dropdown(options=HotelRegiao().get_values()))
HotelFieldSet.append(Field('finalidade').dropdown(options=HotelFim().get_values()))
HotelFieldSet.append(Field('tipo').dropdown(options=HotelTipo().get_values()))

