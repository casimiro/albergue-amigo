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

##################################################
## MODULE CONSTANTS
VFFSL=valueFromFrameOrSearchList
VFSL=valueFromSearchList
VFN=valueForName
currentTime=time.time
__CHEETAH_version__ = '2.4.3'
__CHEETAH_versionTuple__ = (2, 4, 3, 'development', 0)
__CHEETAH_genTime__ = 1292127074.4837539
__CHEETAH_genTimestamp__ = 'Sun Dec 12 02:11:14 2010'
__CHEETAH_src__ = 'Base.tmpl'
__CHEETAH_srcLastModified__ = 'Sun Dec 12 01:11:34 2010'
__CHEETAH_docstring__ = 'Autogenerated by Cheetah: The Python-Powered Template Engine'

if __CHEETAH_versionTuple__ < RequiredCheetahVersionTuple:
    raise AssertionError(
      'This template was compiled with Cheetah version'
      ' %s. Templates compiled before version %s must be recompiled.'%(
         __CHEETAH_version__, RequiredCheetahVersion))

##################################################
## CLASSES

class Base(Template):

    ##################################################
    ## CHEETAH GENERATED METHODS


    def __init__(self, *args, **KWs):

        super(Base, self).__init__(*args, **KWs)
        if not self._CHEETAH__instanceInitialized:
            cheetahKWArgs = {}
            allowedKWs = 'searchList namespaces filter filtersLib errorCatcher'.split()
            for k,v in KWs.items():
                if k in allowedKWs: cheetahKWArgs[k] = v
            self._initCheetahInstance(**cheetahKWArgs)
        

    def respond(self, trans=None):



        ## CHEETAH: main method generated for this template
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
        
        write(u'''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\r
<!--\r
Design by Free CSS Templates\r
http://www.freecsstemplates.org\r
Released for free under a Creative Commons Attribution 2.5 License\r
\r
Title      : Ahoy!\r
Version    : 1.0\r
Released   : 20070413\r
Description: A two-column fixed-width template suitable for small business websites.\r
\r
-->\r
<html xmlns="http://www.w3.org/1999/xhtml">\r
<head>\r
<meta http-equiv="content-type" content="text/html; charset=utf-8" />\r
<title>Albergue Amigo</title>\r
<meta name="keywords" content="" />\r
<meta name="description" content="" />\r
<link href="/default.css" rel="stylesheet" type="text/css" />\r
''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"head",True) # u'$head' on line 21, col 1
        if _v is not None: write(_filter(_v, rawExpr=u'$head')) # from line 21, col 1.
        write(u'''\r
<script type="text/javascript">\r
function runScripts() {\r
\tinitialize();\r
}\r
</script>\r
\r
</head>\r
<body onload="runScripts()">\r
<div id="header">\r
\t<div id="logo">\r
\t\t<h1><a href="/">Albergue Amigo</a></h1>\r
\t\t<h2>N\xf3s sabemos o que voc\xea merece</h2>\r
\t</div>\r
\t<div id="menu">\r
\t\t<ul>\r
\t\t\t<li class="active"><a href="/" accesskey="H" title="Home"><b>H</b>ome</a></li>\r
\t\t\t<li><a href="/hotels/" accesskey="E" title="Encontre seu canto"><b>E</b>ncontre seu canto</a></li>\r
\t\t\t<li><a href="/sites/" accesskey="P" title="Pocilgas Turisticas"><b>P</b>ocilgas Turisticas</a></li>\r
\t\t\t<li><a href="/services/" accesskey="S" title="Servi\xe7os"><b>S</b>ervi\xe7os</a></li>\r
\t\t</ul>\r
\t</div>\r
</div>\r
<div id="page">\r
\t<div id="content">\r
\t''')
        _v = VFSL([locals()]+SL+[globals(), builtin],"body",True) # u'$body' on line 46, col 2
        if _v is not None: write(_filter(_v, rawExpr=u'$body')) # from line 46, col 2.
        write(u'''\r
\t</div>\r
\t<!-- end #content -->\r
\t<div id="sidebar">\r
\t\t<div id="news" class="boxed1">\r
\t\t<h2 class="title">Acesso</h2>\r
''')
        if VFSL([locals()]+SL+[globals(), builtin],"user",True) is not None: # generated from line 52, col 3
            write(u'''\t\t<p>Bem vindo, ''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"user.name",True) # u'$user.name' on line 53, col 17
            if _v is not None: write(_filter(_v, rawExpr=u'$user.name')) # from line 53, col 17.
            write(u'''</p>\r
\t\t<p><a href="/users/logout">Sair</a></p>\r
''')
        else: # generated from line 55, col 3
            write(u'''\t\t<p>Caro usu\xe1rio, efetue login<a href="/users/login"> aqui</a></p>\r
\t\t<p>Se voc\xea n\xe3o \xe9 registrado <a href="/users/edit">clique aqui</a></p>\r
''')
        write(u'''\t\t</div>\r
\t\t<div id="news" class="boxed1">\r
\t\t\t<h2 class="title">\xdaltimos Hoteis</h2>\r
\t\t\t<div class="content">\r
\t\t\t\t<ul>\r
''')
        for hotel in VFSL([locals()]+SL+[globals(), builtin],"last_hotels",True): # generated from line 64, col 6
            write(u'''\t\t\t\t\t<li>\r
\t\t\t\t\t\t<h3><a href="/hotels/view/''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"hotel.id",True) # u'$hotel.id' on line 66, col 33
            if _v is not None: write(_filter(_v, rawExpr=u'$hotel.id')) # from line 66, col 33.
            write(u'''">''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"hotel.nome",True) # u'$hotel.nome' on line 66, col 44
            if _v is not None: write(_filter(_v, rawExpr=u'$hotel.nome')) # from line 66, col 44.
            write(u'''</a></h3>\r
\t\t\t\t\t\t<p>''')
            _v = VFSL([locals()]+SL+[globals(), builtin],"hotel.endereco",True) # u'$hotel.endereco' on line 67, col 10
            if _v is not None: write(_filter(_v, rawExpr=u'$hotel.endereco')) # from line 67, col 10.
            write(u'''</p>\r
\t\t\t\t\t</li>\r
''')
        write(u'''\t\t\t\t</ul>\r
\t\t\t</div>\r
\t\t</div>\r
\t</div>\r
\t<!-- end #sidebar -->\r
\t<div style="clear: both; height: 1px;"></div>\r
</div>\r
<!-- end #page -->\r
<div id="footer">\r
\t<p>Copyright &copy; 2007 Ahoy! Designed by <a href="http://www.freecsstemplates.org/">Free CSS Templates</a></p>\r
</div>\r
</body>\r
</html>''')
        
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

    _mainCheetahMethod_for_Base= 'respond'

## END CLASS DEFINITION

if not hasattr(Base, '_initCheetahAttributes'):
    templateAPIClass = getattr(Base, '_CHEETAH_templateClass', Template)
    templateAPIClass._addCheetahPlumbingCodeToClass(Base)


# CHEETAH was developed by Tavis Rudd and Mike Orr
# with code, advice and input from many other volunteers.
# For more information visit http://www.CheetahTemplate.org/

##################################################
## if run from command line:
if __name__ == '__main__':
    from Cheetah.TemplateCmdLineIface import CmdLineIface
    CmdLineIface(templateObj=Base()).run()


