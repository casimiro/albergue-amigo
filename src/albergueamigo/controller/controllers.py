import os
current_dir = os.path.dirname(os.path.abspath(__file__))

import cherrypy
import datetime
from albergueamigo.view.UserLogin import UserLogin
from albergueamigo.view.EditHotel import EditHotel
from albergueamigo.view.EditUser import EditUser
from albergueamigo.view.ListHotels import ListHotels
from albergueamigo.view.ViewHotel import ViewHotel
from albergueamigo.model.models import Hotel,HotelFieldSet,Session,Base,UserFieldSet,User

class UserController(object):
    
    @cherrypy.expose
    def edit(self, **kwargs):
        if 'User--name' in kwargs:
            user = User(name = kwargs['User--name'],
                        email = kwargs['User--email'],
                        password = kwargs['User--password'],
                        username = kwargs['User--username'],
                        max_diaria = kwargs['User--max_diaria'],
                        hotel_fim = kwargs['User--hotel_fim'],
                        creation_date = datetime.date.today(),
                        cpf = kwargs['User--cpf'])
            user.save()
            return UserLogin().respond()
        return EditUser(searchList=[{'fs':UserFieldSet.render()}]).respond()

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
                         tipo =kwargs['Hotel--tipo'],
                         custo_diaria=kwargs['Hotel--custo_diaria'],
                         url=kwargs['Hotel--url'])
            hotel.save()
            return self.index()
        return EditHotel(searchList=[{'fs':HotelFieldSet.render()}]).respond()

    @cherrypy.expose
    def view(self, hotel_id):
        hotel = Session().query(Hotel).get(hotel_id)
        return ViewHotel(searchList=[{'hotel':hotel}]).respond()
    
    @cherrypy.expose
    def index(self):
        hotels = Session().query(Hotel).all()
        return ListHotels(searchList=[{'hotels':hotels}]).respond()
    
class RootController(object):
    """This class will handle root requests"""
    hotels = HotelController()
    users = UserController()

    @cherrypy.expose
    def index(self):
        return 'Hello Bitches!'
   
if __name__ == '__main__':
    from sqlalchemy import create_engine
    #Creating infrastructure
    engine = create_engine('sqlite:///fuck.db',echo=True)
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    
    cherrypy.quickstart(RootController(),config='server.config')