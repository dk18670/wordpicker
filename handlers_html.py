import re

import search

# Word Picker - Search Engine

def special_case(rack, patt):
  if rack and rack.upper() == 'AWORDTHATISANANAGRAMOFLOW' and patt and patt.upper() == 'ITISALSOTHENAMEOFTHEBIRD':
    return ['OWL']
  return None

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

def handle_find(entry,values):
  rack = values.get('rack')
  patt = values.get('patt')

  # See if it's a special case (cookie)
  matches = special_case(rack, patt)
  if matches is None:
    # See if it's a multiple word case
    if patt:
      patts = []
      parts = patt.replace(',','/').split('/')
      if len(parts) > 1:
	for part in parts:
	  patts.append(format_patt(part, True))
      if len(patts) > 1:
	matches = search.search2(rack, patts)
  if matches is None:
    matches = search.search(rack, format_patt(patt))

  def compare(a,b):
    d = len(a)-len(b)
    if d:
      return -d
    if a < b:
      return -1
    elif a > b:
      return +1
    return 0

  entries = []

  if matches:
    matches.sort(cmp=compare)

    words = []
    last_len = 0
    for match in matches:
      l = len(match)
      if l != last_len and len(words):
        entries.append({'len': last_len, 'words': ', '.join(words)})
        words = []
      last_len = l
      words.append(match)
    if len(words):
      entries.append({'len': last_len, 'words': ', '.join(words)})

  return {
    'rack':    rack,
    'patt':    patt,
    'entries': entries
  }

# Word Picker - Game

WRD4 = 5<<8
WRD3 = 4<<8
WRD2 = 3<<8
LET3 = 2<<8
LET2 = 1<<8

SIZE = 15

INITIAL_BOARD = [
  0,0,0,WRD4,0,0,0,0,0,0,0,WRD4,0,0,0,
  0,0,WRD3,0,0,0,LET3,0,LET3,0,0,0,WRD3,0,0,
  0,WRD3,0,0,0,LET2,0,0,0,LET2,0,0,0,WRD3,0,
  WRD4,0,0,0,WRD2,0,0,0,0,0,WRD2,0,0,0,WRD4,
  0,0,0,WRD2,0,0,0,0,0,0,0,WRD2,0,0,0,
  0,0,LET2,0,0,0,LET2,0,LET2,0,0,0,LET2,0,0,
  0,LET3,0,0,0,LET2,0,0,0,LET2,0,0,0,LET3,0,
  0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
  0,LET3,0,0,0,LET2,0,0,0,LET2,0,0,0,LET3,0,
  0,0,LET2,0,0,0,LET2,0,LET2,0,0,0,LET2,0,0,
  0,0,0,WRD2,0,0,0,0,0,0,0,WRD2,0,0,0,
  WRD4,0,0,0,WRD2,0,0,0,0,0,WRD2,0,0,0,WRD4,
  0,WRD3,0,0,0,LET2,0,0,0,LET2,0,0,0,WRD3,0,
  0,0,WRD3,0,0,0,LET3,0,LET3,0,0,0,WRD3,0,0,
  0,0,0,WRD4,0,0,0,0,0,0,0,WRD4,0,0,0,
]

def byte(v,n):
  return (v>>(8*n))&0xFF

def mask(n):
  return 0xFF<<(8*n)

def elem(board,x,y):
  return board[y*SIZE+x]

def set_letter(board,x,y,letter):
  board[y*SIZE+x] = (elem(board,x,y)&(~mask(0))) + ord(letter);

def add_letters(board,x,y,direction,letters):
  for letter in letters:
    while byte(elem(board,x,y),0):
      if direction==0: x+=1
      if direction==1: y+=1
    set_letter(board,x,y,letter)
    if direction==0: x+=1
    if direction==1: y+=1

def handle_game(entry,values):
  board = INITIAL_BOARD
  add_letters(board,2,7,0,'YANN THE MAN')

  attrs = {}
  attrs['size'] = SIZE
  attrs['cell'] = 30

  attrs['board'] = board
  attrs['player_names'] = ['Keith H', 'Fran B']
  attrs['player_scores'] = [120, 96]
  attrs['player_turn'] = 0
  attrs['last_player'] = 1
  attrs['last_move'] = 'WEX'
  attrs['last_score'] = 33
  attrs['tiles_left'] = 56

  return attrs