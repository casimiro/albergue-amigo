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
__CHEETAH_genTime__ = 1292127074.5860319
__CHEETAH_genTimestamp__ = 'Sun Dec 12 02:11:14 2010'
__CHEETAH_src__ = 'ListTouristicSites.tmpl'
__CHEETAH_srcLastModified__ = 'Sun Dec 12 01:31:09 2010'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class ListTouristicSites(Base):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(ListTouristicSites, self).__init__(*args, **KWs)
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
        
        
        ########################################
        ## END - generated method body
        
        return _dummyTrans and trans.response().getvalue() or ""
        

    def body(self, **KWS):



        ## CHEETAH: generated from #def body at line 8, col 1.
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
        
        write(u'''<h2>Lista de S\xed\xadtios Tur\xedsticos</h2>
''')
        for site in VFSL([locals()]+SL+[globals(), builtin],"sites",True): # generated from line 10, col 1
            write(u'''<p><a href="/sites/view/''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"site.id",True) # u'$site.id' on line 11, col 25
            if _v is not None: write(_filter(_v, rawExpr=u'$site.id')) # from line 11, col 25.
            write(u'''">''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"site.name",True) # u'$site.name' on line 11, col 35
            if _v is not None: write(_filter(_v, rawExpr=u'$site.name')) # from line 11, col 35.
            write(u'''</a>
''')
            if VFSL([locals()]+SL+[globals(), builtin],"user",True) is not None and VFSL([locals()]+SL+[globals(), builtin],"user.username",True) == 'admin': # generated from line 12, col 1
                write(u''' - <a href="/sites/edit/''')
                _v = VFSL([locals()]+SL+[globals(), builtin],"site.id",True) # u'$site.id' on line 13, col 25
                if _v is not None: write(_filter(_v, rawExpr=u'$site.id')) # from line 13, col 25.
                write(u'''">Editar</a>
''')
            write(u'''</p>
''')
        write(u'''
''')
        if VFSL([locals()]+SL+[globals(), builtin],"user",True) is not None and VFSL([locals()]+SL+[globals(), builtin],"user.username",True) == 'admin': # generated from line 18, col 1
            write(u'''<p>Clique <a href="/sites/edit">aqui</a> para adicionar um s\xedtio tur\xedstico</p>
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

    _mainCheetahMethod_for_ListTouristicSites= 'writeBody'

## END CLASS DEFINITION

if not hasattr(ListTouristicSites, '_initCheetahAttributes'):
    templateAPIClass = getattr(ListTouristicSites, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(ListTouristicSites)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=ListTouristicSites()).run()


