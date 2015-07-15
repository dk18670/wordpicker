#!/usr/bin/python

import os, cgi

from mlhtml import *

from logger import *

form = cgi.FieldStorage()
data = dict([(x,form.getvalue(x)) for x in form.keys()])

logger.info('%s: %s' % (os.path.basename(__file__), repr(data)))

Redirect('/find?%s' % ('&'.join(map(lambda x:'%s=%s'%(x,data[x]), data.keys()))))
