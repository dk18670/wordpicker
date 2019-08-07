import csv, re, datetime, collections, copy


class WPCounter(collections.Counter):
  def __init__(self,s):
    super(WPCounter,self).__init__()
    for c in s:
      self[c] += 1

  def __str__(self):
    return ''.join([k*v for k,v in self.items()])

  def __repr__(self):
    return 'WPCounter('+str(self)+')'

  def __add__(self,s):
    cpy = WPCounter(str(self))
    for c in s:
      cpy[c] += 1
    return cpy

  def __sub__(self,s):
    cpy = WPCounter(str(self))
    for c in s:
      if not cpy[c]:
        if not cpy['.']:
          raise Exception('Depleted character:',c)
        c = '.'
      cpy[c] -= 1
    return cpy

  def __contains__(self,s):
    cpy = WPCounter(str(self))
    for c in s:
      if c=='.' or c==' ':
        continue
      if not cpy[c]:
        if not cpy['.']:
          return False
        c = '.'
      cpy[c] -= 1
    return True


def gen_match(chars,mask):
  # remove the matched chars and leave the . chars
  # eg mask='P.AY.R' then match='.R..E.'
  return ''.join([(chars[i] if m=='.' else '.') for i,m in enumerate(mask)])


def fetch_matching_words(rack, min_len, max_len, patt=None, mask=None):
  matches = []
  with open('sowpods.txt') as file:
    reader = csv.reader(file)
    for row in reader:
      word = row[0]
      if not min_len <= len(word) <= max_len:
        continue
      if patt:
        m = re.search(patt, word)
        if m:
          #print(word,patt,m.group())
          match = gen_match(m.group(), mask)
          chars = word[:m.start()]+match+word[m.end():]
          if not rack or chars in rack:
            matches.append(word)
      else:
        if not rack or word in rack:
          matches.append(word)
  return matches


def process_rack(rack):
    # strip out any unwanted characters
    rack = re.sub('[^A-Z\.?_\-]','',rack.upper())
    # replace ?_- chars with .
    rack = re.sub('[?_\-]', '.', rack)

    max_len = len(rack)

    return WPCounter(rack), max_len


def process_patt(patt):
  beg = patt.startswith('$')
  end = patt.endswith('$')
  # strip out any unwanted characters
  patt = re.sub('[^A-Z\.?_\-\[\]]','',patt.upper())
  # replace ?_- chars with .
  patt = re.sub('[?_\-]', '.', patt)
  # compose a mask to remove matched chars
  mask = re.sub('\[.*?\]','.',patt)
  # if beginning match then add ^ prefix
  if beg: patt = '^'+patt
  # if end match then add $ suffix
  if end: patt = patt+'$'

  return patt, mask


def search(rack,patt):
  if not rack and not patt:
    return None

  min_len = 1
  max_len = 15

  if rack:
    rack, max_len = process_rack(rack)

  if patt:
    patt, mask = process_patt(patt)
    min_len = len(mask)
    max_len += len(mask)
    print(mask)
  else:
    mask = None

  matches = fetch_matching_words(rack, min_len, max_len, patt, mask)

  return matches if len(matches) else None


def search2(rack,patts):
  if not rack:
    return None

  min_len = 1
  max_len = 15

  if rack:
    rack, max_len = process_rack(rack)


  def expand(rack,results,prefix=''):
    #print('expand:', rack, results, prefix)
    if len(results)==1:
      for word in results[0]:
        if word in rack:
          yield prefix+word
    else:
      for word in results[0]:
        for ex in expand(rack-word,results[1:],prefix+word+' '):
          yield ex


  if not patts:
    return fetch_matching_words(rack, min_len, max_len)

  start = datetime.datetime.now()
  results = []
  masks = []
  for patt in patts:
    patt, mask = process_patt(patt)
    matches = fetch_matching_words(rack, len(mask), max_len+len(mask), patt, mask)
    results.append(matches)
    masks.append(mask)
  print('compiling results took:', datetime.datetime.now()-start)
  start = datetime.datetime.now()
  n = 1
  for result in results:
    print(len(result), result)
    n *= len(result)
  print(n, 'combinations..')
  matches = []
  for ex in expand(rack,results):
    matches.append(ex)
  td = datetime.datetime.now()-start
  microseconds = (td.days*24*60*60 + td.seconds)*1000000 + td.microseconds
  print(td, '= %d per second' % (n*1000000/microseconds))

  return matches
