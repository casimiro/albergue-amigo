#!/usr/bin/env python
# -*- coding: UTF-8 -*-




##################################################
## DEPENDENCIES
import sys
import os
import os.path
try:
    import builtins as builtin
except ImportError:
    import __builtin__ as builtin
from os.path import getmtime, exists
import time
import types
from Cheetah.Version import MinCompatibleVersion as RequiredCheetahVersion
from Cheetah.Version import MinCompatibleVersionTuple as RequiredCheetahVersionTuple
from Cheetah.Template import Template
from Cheetah.DummyTransaction import *
from Cheetah.NameMapper import NotFound, valueForName, valueFromSearchList, valueFromFrameOrSearchList
from Cheetah.CacheRegion import CacheRegion
import Cheetah.Filters as Filters
import Cheetah.ErrorCatchers as ErrorCatchers
from Base import Base

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.3'
__CHEETAH_versionTuple__ = (2, 4, 3, 'development', 0)
__CHEETAH_genTime__ = 1292127074.6361611
__CHEETAH_genTimestamp__ = 'Sun Dec 12 02:11:14 2010'
__CHEETAH_src__ = 'ViewHotel.tmpl'
__CHEETAH_srcLastModified__ = 'Sun Dec 12 02:03:46 2010'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class ViewHotel(Base):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(ViewHotel, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def head(self, **KWS):



        ## CHEETAH: generated from #def head at line 5, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false&language=pt-br"></script>
<script type="text/javascript">
  function initialize() {
    var hotel = new google.maps.LatLng(''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"hotel.latitude",True) # u'$hotel.latitude' on line 9, col 40
        if _v is not None: write(_filter(_v, rawExpr=u'$hotel.latitude')) # from line 9, col 40.
        write(u''', ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"hotel.longitude",True) # u'$hotel.longitude' on line 9, col 57
        if _v is not None: write(_filter(_v, rawExpr=u'$hotel.longitude')) # from line 9, col 57.
        write(u''');
    var myOptions = {
      zoom: 16,
      center: hotel,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
    var hotelMarker = new google.maps.Marker({
      position: hotel, 
      map: map, 
      title:"''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"hotel.nome",True) # u'$hotel.nome' on line 19, col 14
        if _v is not None: write(_filter(_v, rawExpr=u'$hotel.nome')) # from line 19, col 14.
        write(u'''"
\t});
\t
''')
        for i in range(len(VFN(VFSL([locals()]+SL+[globals(), builtin],"nearby_sites",True),"keys",False)())): # generated from line 22, col 2
            s = VFN(VFSL([locals()]+SL+[globals(), builtin],"nearby_sites",True),"keys",False)()[VFSL([locals()]+SL+[globals(), builtin],"i",True)]
            write(u'''\tvar pos''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"i",True) # u'$i' on line 24, col 9
            if _v is not None: write(_filter(_v, rawExpr=u'$i')) # from line 24, col 9.
            write(u''' = new google.maps.LatLng(''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"s.latitude",True) # u'$s.latitude' on line 24, col 37
            if _v is not None: write(_filter(_v, rawExpr=u'$s.latitude')) # from line 24, col 37.
            write(u''', ''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"s.longitude",True) # u'$s.longitude' on line 24, col 50
            if _v is not None: write(_filter(_v, rawExpr=u'$s.longitude')) # from line 24, col 50.
            write(u''');
\tvar marker''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"i",True) # u'$i' on line 25, col 12
            if _v is not None: write(_filter(_v, rawExpr=u'$i')) # from line 25, col 12.
            write(u''' = new google.maps.Marker({
\t  icon: "/images/beerMarker.png",
      position: pos''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"i",True) # u'$i' on line 27, col 20
            if _v is not None: write(_filter(_v, rawExpr=u'$i')) # from line 27, col 20.
            write(u''', 
      map: map, 
      title:"''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"s.name",True) # u'$s.name' on line 29, col 14
            if _v is not None: write(_filter(_v, rawExpr=u'$s.name')) # from line 29, col 14.
            write(u'''"
\t});
\t
\tvar content''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"i",True) # u'$i' on line 32, col 13
            if _v is not None: write(_filter(_v, rawExpr=u'$i')) # from line 32, col 13.
            write(u''' = "Hotel: ''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"s.name",True) # u'$s.name' on line 32, col 26
            if _v is not None: write(_filter(_v, rawExpr=u'$s.name')) # from line 32, col 26.
            write(u'''<br>";
\tvar infoWindow''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"i",True) # u'$i' on line 33, col 16
            if _v is not None: write(_filter(_v, rawExpr=u'$i')) # from line 33, col 16.
            write(u''' = new google.maps.InfoWindow({content: content''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"i",True) # u'$i' on line 33, col 65
            if _v is not None: write(_filter(_v, rawExpr=u'$i')) # from line 33, col 65.
            write(u'''});
\t(infoWindow''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"i",True) # u'$i' on line 34, col 13
            if _v is not None: write(_filter(_v, rawExpr=u'$i')) # from line 34, col 13.
            write(u''').setPosition(pos''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"i",True) # u'$i' on line 34, col 32
            if _v is not None: write(_filter(_v, rawExpr=u'$i')) # from line 34, col 32.
            write(u''');
    (infoWindow''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"i",True) # u'$i' on line 35, col 16
            if _v is not None: write(_filter(_v, rawExpr=u'$i')) # from line 35, col 16.
            write(u''').open(map);
\t
''')
        write(u'''\t
\tvar content = "Hotel: ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"hotel.nome",True) # u'$hotel.nome' on line 39, col 24
        if _v is not None: write(_filter(_v, rawExpr=u'$hotel.nome')) # from line 39, col 24.
        write(u'''<br> Classifica\xe7ao: ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"hotel.classificacao",True) # u'$hotel.classificacao' on line 39, col 55
        if _v is not None: write(_filter(_v, rawExpr=u'$hotel.classificacao')) # from line 39, col 55.
        write(u''' estrelas<br>"
\tvar infoWindow = new google.maps.InfoWindow({content: content});
\tinfoWindow.setPosition(hotel);
    infoWindow.open(map);
  }

</script>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def body(self, **KWS):



        ## CHEETAH: generated from #def body at line 48, col 1.
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''<h2>''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"hotel.nome",True) # u'$hotel.nome' on line 49, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$hotel.nome')) # from line 49, col 5.
        write(u'''</h2>
<p>Endereco: ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"hotel.endereco",True) # u'$hotel.endereco' on line 50, col 14
        if _v is not None: write(_filter(_v, rawExpr=u'$hotel.endereco')) # from line 50, col 14.
        write(u'''</p>
<p>Classifica\xe7\xe3o: ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"hotel.classificacao",True) # u'$hotel.classificacao' on line 51, col 19
        if _v is not None: write(_filter(_v, rawExpr=u'$hotel.classificacao')) # from line 51, col 19.
        write(u''' estrelas</p>
<p>Regi\xe3o: ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"hotel.regiao",True) # u'$hotel.regiao' on line 52, col 12
        if _v is not None: write(_filter(_v, rawExpr=u'$hotel.regiao')) # from line 52, col 12.
        write(u'''</p>
''')
        if VFSL([locals()]+SL+[globals(), builtin],"hotel.imagem",True) is not None: # generated from line 53, col 1
            write(u'''<p>Imagem do Hotel</p>
<img src="''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"hotel.imagem",True) # u'$hotel.imagem' on line 55, col 11
            if _v is not None: write(_filter(_v, rawExpr=u'$hotel.imagem')) # from line 55, col 11.
            write(u'''" />
''')
        write(u'''<p>Localiza\xe7\xe3o no Mapa</p>
<div id="map_canvas" style="width: 500px; height: 480px;"></div>
<br/>
<h2>S\xedtios Tur\xedsticos Pr\xf3ximos</h2>
<ul>
''')
        for site,dist in VFN(VFSL([locals()]+SL+[globals(), builtin],"nearby_sites",True),"items",False)(): # generated from line 62, col 1
            write(u'''<li><b>''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"site.name",True) # u'$site.name' on line 63, col 8
            if _v is not None: write(_filter(_v, rawExpr=u'$site.name')) # from line 63, col 8.
            write(u'''</b> - ''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"dist",True) # u'$dist' on line 63, col 25
            if _v is not None: write(_filter(_v, rawExpr=u'$dist')) # from line 63, col 25.
            write(u''' m</li>
''')
        write(u'''</ul>
''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def writeBody(self, **KWS):



        ## CHEETAH: main method generated for this template
        trans = KWS.get("trans")
        if (not trans and not self._CHEETAH__isBuffering and not callable(self.transaction)):
            trans = self.transaction # is None unless self.awake() was called
        if not trans:
            trans = DummyTransaction()
            _dummyTrans = True
        else: _dummyTrans = False
        write = trans.response().write
        SL = self._CHEETAH__searchList
        _filter = self._CHEETAH__currentFilter
        
        ########################################
        ## START - generated method body
        
        write(u'''

''')
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        
    ##################################################
    ## CHEETAH GENERATED ATTRIBUTES


    _CHEETAH__instanceInitialized = False

    _CHEETAH_version = __CHEETAH_version__

    _CHEETAH_versionTuple = __CHEETAH_versionTuple__

    _CHEETAH_genTime = __CHEETAH_genTime__

    _CHEETAH_genTimestamp = __CHEETAH_genTimestamp__

    _CHEETAH_src = __CHEETAH_src__

    _CHEETAH_srcLastModified = __CHEETAH_srcLastModified__

    _mainCheetahMethod_for_ViewHotel= 'writeBody'

## END CLASS DEFINITION

if not hasattr(ViewHotel, '_initCheetahAttributes'):
    templateAPIClass = getattr(ViewHotel, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(ViewHotel)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=ViewHotel()).run()


