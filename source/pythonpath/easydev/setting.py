# coding: utf-8

import logging
import sys
from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK, BUTTONS_YES_NO
from com.sun.star.awt.MessageBoxResults import OK, YES, NO
from com.sun.star.awt.MessageBoxType import INFOBOX, ERRORBOX, QUERYBOX

OS = sys.platform
NAME_EXT = 'EasyDev'

FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
DATE = '%d/%m/%Y %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, datefmt=DATE)
LOG = logging.getLogger(NAME_EXT)

VERSION = '2.0.0'
ID_EXT = 'org.universolibre.EasyDev'
NODE = '/{}.Configuration/Settings'.format(ID_EXT)
NODE_CONFIG = 'Values'
LINUX = 'linux'
WIN = 'win32'
DECIMALS = 2
FORMAT = '{{0:,.{}f}}'
DESKTOP = 'com.sun.star.frame.Desktop'
TOOLKIT = 'com.sun.star.awt.Toolkit'
SRV_JOB = ('com.sun.star.task.Job',)
CALC = 'scalc'
WRITER = 'swriter'
EXT_PDF = 'pdf'
CLIPBOARD_FORMAT_TEXT = 'text/plain;charset=utf-16'
TIMEOUT = 10
PYTHON = 'Python'
LOCATION_USER = 'user'
FILE_NAME_DEBUG = 'debug.odt'
TITLE_DEBUG = 'Debug'
COLORS = {
    'YELLOW': 16777164,
    'WHITE': 16777215,
    'BLUE': 255,
    'GRAY': 16119285,
    'GREEN': 12255176,
    'RED': 16764108,
}
DATA_TYPES = {
    #~ MySQL
    'bit': 'getByte',
    'tinyint': 'getLong',
    'bigint': 'getLong',
    'smallint': 'getLong',
    'integer': 'getLong',
    'decimal': 'getFloat',
    'float': 'getFloat',
    'double': 'getDouble',
    'char': 'getString',
    'varchar': 'getString',
    'text': 'getString',
    'date': 'getDate',
    'time': 'getTime',
    'timestamp': 'getTimestamp',
    'datetime': 'getTimestamp',
    #~ PostgreSQL
    '': 'getString',
    'int8': 'getLong',
    'int8': 'getLong',
    'unknown': 'getString',
    'bool': 'getBoolean',
    'bytea': 'getBytes',
    'cidr': 'getString',
    'float8': 'getDouble',
    'inet': 'getString',
    'int4': 'getLong',
    'macaddr': 'getString',
    'money': 'getDouble',
    'numeric': 'getDouble',
    'float4': 'getDouble',
    'int2': 'getLong',
    'int4': 'getLong',
    'timestamp without time zone': 'getTimestamp',
    'timestamp with time zone': 'getTimestamp',
    'uuid': 'getString',
    'xml': 'getString',
    #~ SQLite
    'real': 'getDouble',
    'blob': '',
    #~ MSSQL
}

