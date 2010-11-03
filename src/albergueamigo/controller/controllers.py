from albergueamigo.view.EditHotel import EditHotel
from albergueamigo.model.models import Hotel
class Controller(object):
    """This class will handle the HTTP requests """
    
    def edit_hotel(self, **kwargs):
        if 'nome' in kwargs:
            hotel = Hotel(nome=kwargs['nome'],
                         endereco=kwargs['endereco'],
                         regiao = kwargs['regiao'],
                         classificacao = kwargs['classificacao'],
                         finalidade=kwargs['finalidade'],
                         custo_diaria=kwargs['custo_diaria'],
                         url=kwargs['url'])
             
        return EditHotel().respond()
    
