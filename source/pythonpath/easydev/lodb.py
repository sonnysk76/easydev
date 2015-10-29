# coding: utf-8

import logging
from org.universolibre.EasyDev import XLODataBase
from easydev.setting import LOG, NAME_EXT
from easydev import comun
from easydev.comun import LODefault


log = logging.getLogger(NAME_EXT)


class LODataBase(XLODataBase, LODefault):

    def __init__(self, ctx, sm, desktop, toolkit):
        LODefault.__init__(self, ctx, sm, desktop, toolkit)

    def conODBC(self, name, user, password):
        dm = self._create_instance('com.sun.star.sdbc.DriverManager')
        pv = comun.set_properties((('user', user), ('password', password)))
        try:
            con = dm.getConnectionWithInfo('sdbc:odbc:{}'.format(name), pv)
            return con
        except Exception as e:
            log.error(str(e))
            return None