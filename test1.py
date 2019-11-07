#!/usr/bin/python

import search2

def format_patt(patt, strict=False):
  # if patt is an integer then treat as a fixed length word
  try:
    patt = '?'*int(patt)
    if strict:
      patt = '$' + patt + '$'
  except:
    pass
  return patt

rack = '.rbllvs'
patt = '$..[ou][nyox][aeoiu]'
rack = 'BXAEDXLWQLUD'
patt = '$....$'

matches = search2.search(rack, patt)

if not matches:
  print 'None found'
else:
  for match in matches:
    print match
