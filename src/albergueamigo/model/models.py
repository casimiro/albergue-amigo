from elixir import *

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

class Hotel(Entity):
    """This class is a model and represents a Hotel!"""
    
    nome = Field(Unicode(20))
    endereco = Field(Unicode(30))
    regiao = Field(Unicode(10))
    classificacao = Field(Integer)
    finalidade = Field(Unicode(10))
    custo_diaria = Field(Float)
    tipo = Field(Unicode(10))
    url = Field(Unicode(30))


    def __repr__(self):
        return '<Hotel "%s">' % (self.__dict__)

    def __eq__(self, other):
        return self.id == other.id

def setDB(db):
    metadata.bind = db
    metadata.echo = True

setup_all()
