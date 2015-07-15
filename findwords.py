#!/usr/bin/python

import search, logger

from utils import *
from mljson import *

dict = FetchFormFields()

logger.info('%s: %s' % (os.path.basename(__file__), repr(dict)))

rack = dict.get('rack')
patt = dict.get('patt')

matches = search.search(rack, patt)

Return({'words': matches})
