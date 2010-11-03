import cherrypy
from albergueamigo.view.EditHotel import EditHotel
from albergueamigo.view.ListHotels import ListHotels
from albergueamigo.model.models import Hotel

class HotelController(object):
    """This class will handle the hotels HTTP requests """
    @cherrypy.expose
    def edit(self, **kwargs):
        if 'nome' in kwargs:
            hotel = Hotel(nome=kwargs['nome'],
                         endereco=kwargs['endereco'],
                         regiao = kwargs['regiao'],
                         classificacao = kwargs['classificacao'],
                         finalidade=kwargs['finalidade'],
                         custo_diaria=kwargs['custo_diaria'],
                         url=kwargs['url'])
            return self.index()
        return EditHotel().respond()

    @cherrypy.expose
    def index(self):
        hotels = Hotel.query.all()
        return ListHotels(searchList=[{'hotels':hotels}]).respond()

class RootController(object):
    """This class will handle root requests"""
    
    hotels = HotelController()

    @cherrypy.expose
    def index(self):
        return 'Hello Bitches!'
   
if __name__ == '__main__':
    cherrypy.quickstart(HotelController())
