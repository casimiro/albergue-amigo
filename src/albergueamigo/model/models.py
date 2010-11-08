from sqlalchemy import Column,String,Integer,Float
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.declarative import declarative_base

Session = scoped_session(sessionmaker())
Base = declarative_base()

class HotelRegiao(object):
    """Enum of Zona"""
    OESTE = 'Oeste'
    SUL = 'Sul'
    NORTE = 'Norte'
    LESTE = 'Leste'

class HotelTipo(object):
    """Enum of hotel types """
    FAMILIAR = 'Familiar'
    INDIVIDUAL = 'Individual'

class HotelFim(object):
    """Enum of hotel propose"""
    NEGOCIOS = 'Business'
    LAZER = 'Lazer'

class Hotel(Base):
    """This class is a model and represents a Hotel!"""
    __tablename__ = 'hotel'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    endereco = Column(String)
    regiao = Column(String)
    classificacao = Column(Integer)
    finalidade = Column(String)
    custo_diaria = Column(Float)
    tipo = Column(String)
    url = Column(String)


    def __repr__(self):
        return '<Hotel "%s">' % (self.__dict__)

    def __eq__(self, other):
        return self.id == other.id

    def save(self):
        session = Session()
        session.add(self)
        session.commit()