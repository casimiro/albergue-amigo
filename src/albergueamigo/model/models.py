class Zona(object):
    """Enum of Zona"""
    OESTE = 0
    SUL = 1
    NORTE = 2
    LESTE = 3

class HotelTipo(object):
    """Enum of hotel types """
    FAMILIAR = 0
    INDIVIDUAL = 1

class HotelFim(object):
    """Enum of hotel propose"""
    NEGOCIOS = 0
    LAZER = 1

class Hotel(object):
    """This class is a model and represents a Hotel!"""

    def __init__(self, nome, endereco, regiao, classificacao, finalidade, custo_diaria, tipo, url):
       self.nome = nome
       self.endereco = endereco
       self.regiao = regiao
       self.classificacao = classificacao
       self.finalidade = finalidade
       self.custo_diaria = custo_diaria
       self.tipo = tipo
       self.url = url
