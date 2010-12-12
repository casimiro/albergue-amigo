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
__CHEETAH_genTime__ = 1292127074.6659429
__CHEETAH_genTimestamp__ = 'Sun Dec 12 02:11:14 2010'
__CHEETAH_src__ = 'ViewTouristicSite.tmpl'
__CHEETAH_srcLastModified__ = 'Sun Dec 12 00:47:57 2010'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class ViewTouristicSite(Base):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(ViewTouristicSite, self).__init__(*args, **KWs)
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
        _v = VFSL([locals()]+SL+[globals(), builtin],"site.latitude",True) # u'$site.latitude' on line 9, col 40
        if _v is not None: write(_filter(_v, rawExpr=u'$site.latitude')) # from line 9, col 40.
        write(u''', ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"site.longitude",True) # u'$site.longitude' on line 9, col 56
        if _v is not None: write(_filter(_v, rawExpr=u'$site.longitude')) # from line 9, col 56.
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
        _v = VFSL([locals()]+SL+[globals(), builtin],"site.name",True) # u'$site.name' on line 19, col 14
        if _v is not None: write(_filter(_v, rawExpr=u'$site.name')) # from line 19, col 14.
        write(u'''"
\t});
\t
\tvar content = "S\xedtio Tur\xedstico: ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"site.name",True) # u'$site.name' on line 22, col 34
        if _v is not None: write(_filter(_v, rawExpr=u'$site.name')) # from line 22, col 34.
        write(u'''<br>"
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



        ## CHEETAH: generated from #def body at line 31, col 1.
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
        _v = VFSL([locals()]+SL+[globals(), builtin],"site.name",True) # u'$site.name' on line 32, col 5
        if _v is not None: write(_filter(_v, rawExpr=u'$site.name')) # from line 32, col 5.
        write(u'''</h2>
<p>Endereco: ''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"site.address",True) # u'$site.address' on line 33, col 14
        if _v is not None: write(_filter(_v, rawExpr=u'$site.address')) # from line 33, col 14.
        write(u'''</p>
<p>Localiza\xe7\xe3o no Mapa</p>
<div id="map_canvas" style="width: 500px; height: 480px;"></div>
<br/>
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

    _mainCheetahMethod_for_ViewTouristicSite= 'writeBody'

## END CLASS DEFINITION

if not hasattr(ViewTouristicSite, '_initCheetahAttributes'):
    templateAPIClass = getattr(ViewTouristicSite, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(ViewTouristicSite)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=ViewTouristicSite()).run()


