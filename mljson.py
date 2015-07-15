import sys, json

from utils import *

def ReturnJson(dict):
  print 'Content-type: application/json'
  print
  print json.dumps(dict)

def Return(dict):
  ReturnJson(dict)

def Error(str,dict=None):
  if not dict:
    dict = {}
  dict['error'] = Escape(str)
  Return(dict)
  sys.exit(1)

def Message(str,dict=None):
  if not dict:
    dict = {}
  dict['message'] = Escape(str)
  Return(dict)
