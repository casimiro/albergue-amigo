import os
current_dir = os.path.dirname(os.path.abspath(__file__))

import cherrypy
from albergueamigo.view.EditHotel import EditHotel
from albergueamigo.view.ListHotels import ListHotels
from albergueamigo.model.models import *

class HotelController(object):
    """This class will handle the hotels HTTP requests """
    
    @cherrypy.expose
    def edit(self, **kwargs):
        if 'Hotel--nome' in kwargs:
            hotel = Hotel(nome=kwargs['Hotel--nome'],
                         endereco=kwargs['Hotel--endereco'],
                         regiao = kwargs['Hotel--regiao'],
                         classificacao = kwargs['Hotel--classificacao'],
                         finalidade=kwargs['Hotel--finalidade'],
                         custo_diaria=kwargs['Hotel--custo_diaria'],
                         url=kwargs['Hotel--url'])
            hotel.save()
            
            return self.index()

        return EditHotel(searchList=[{'fs':HotelFieldSet.render()}]).respond()

    @cherrypy.expose
    def index(self, hotel_id = None):
        if hotel_id is None:
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
    #Creating infrastrucrure
    engine = create_engine('sqlite:///fuck.db',echo=True)
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    
    cherrypy.quickstart(RootController(),config='server.config')