#!/usr/bin/python

import search2

def format_patt(patt, strict=False):
  # if patt is an integer then treat as a fixed length word
  try:
    patt = '?'*int(patt)
    strict = True
  except:
    pass
  if strict:
    patt = '$' + patt + '$'
  return patt

#rack = 'lytyctodnleoyeig'
#patt = '3/4'
#rack = 'RJOAELMSBEN'
#patt = '_____[n]/5'
#rack = 'tilgoyhakha'
#patt = '4/5/2'
#rack = 'lytyctodnleoyeig'
#patt = '5/snow'
rack = 'Alenoirmef'
patt = '6,4'

patts = []
parts = patt.replace(',','/').split('/')
if len(parts) > 1:
  for part in parts:
    patts.append(format_patt(part, True))
if len(patts) > 1:
  matches = search2.search2(rack, patts)

for match in matches:
  print match
