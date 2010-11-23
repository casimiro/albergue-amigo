import os
current_dir = os.path.dirname(os.path.abspath(__file__))

import cherrypy
from albergueamigo.view.EditHotel import EditHotel
from albergueamigo.view.ListHotels import ListHotels
from albergueamigo.model.models import Hotel,Session,HotelRegiao,HotelFieldSet
from formalchemy import FieldSet,Field

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
            hotel.save()
            
            return self.index()

        return EditHotel(searchList=[{'fs':HotelFieldSet.render()}]).respond()

    @cherrypy.expose
    def index(self):
        hotels = Session().query(Hotel).all()
        return ListHotels(searchList=[{'hotels':hotels}]).respond()

class RootController(object):
    """This class will handle root requests"""
    
    hotels = HotelController()

    @cherrypy.expose
    def index(self):
        return 'Hello Bitches!'
   
if __name__ == '__main__':
    from sqlalchemy import create_engine
    from albergueamigo.model.models import Session,Base
    #Creating infrastrucrure
    engine = create_engine('sqlite:///:memory:',echo=True)
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    
    cherrypy.quickstart(RootController(),config='server.config')
