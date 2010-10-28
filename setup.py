from distutils.core import setup

setup(
    name = 'albergue-amigo',
    version = '1.0',
    description = 'Web System that allow users register informations about hotels in Sao Paulo',
    author = 'Caio Casimiro',
    author_email = 'caiorcasimiro@gmail.com',
    packages = ['albergueamigo'],
    package_dir = {'albergueamigo':'src/albergueamigo'},
    package_data = {'albergueamigo':['data/*']}
)
