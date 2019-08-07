import csv, re, datetime, collections, copy

class WPCounter(collections.Counter):
  def __init__(self,s):
    super(WPCounter,self).__init__(self)
    for c in s:
      self[c] += 1

  def __repr__(self):
    return 'WPCounter('+''.join([k*v for k,v in self.items()])+')'

  def __add__(self,s):
    for c in s:
      self[c] += 1
    return self

  def __sub__(self,s):
    for c in s:
      self[c] -= 1
    return self

  def __contains__(self,s):
    cpy = collections.Counter(self)
    for c in s:
      if c=='.' or c==' ':
        continue
      if not cpy[c]:
        c = '.'
        if not cpy[c]:
          return False
      cpy[c] -= 1
    return True

def gen_match(chars,mask):
  #print('gen_match:', chars, mask)
  # remove the matched chars and leave the . chars
  # eg mask='P.AY.R' then match='.R..E.'
  match = ''
  for i in xrange(len(mask)):
    match += chars[i] if mask[i]=='.' else '.'
  return match

def search(rack,patt):
  if not rack and not patt:
    return None

  min_len = 1
  max_len = len(rack) if rack else 15

  if rack:
    # strip out any unwanted characters
    rack = re.sub('[^A-Z\.?_\-]','',rack.upper())
    # replace ?_- chars with .
    rack = re.sub('[?_\-]', '.', rack)
  if patt:
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
    min_len = min(min_len,len(mask))
    max_len += len(mask)
    print(mask)

  rack = WPCounter(rack)

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

  return matches if len(matches) else None


def search2(rack,patts):
  if not rack:
    return None

  # strip out any unwanted characters
  rack = re.sub('[^A-Z\.?_\-]','',rack.upper())
  # replace ?_- chars with .
  rack = re.sub('[?_\-]', '.', rack)

  rack = WPCounter(rack)

  def scan(rack, min_len, max_len, patt=None, mask=None):
    print('scan:', rack, min_len, max_len, patt, mask)
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
            # remove the matched chars and leave the . chars, eg patt='P.AY.R' match='.R..E.'
            match = ''
            for i in xrange(len(mask)):
              match += m.group()[i] if mask[i]=='.' else '.'
            chars = word[:m.start()]+match+word[m.end():]
            if chars in rack:
              matches.append(word)
        else:
          if word in rack:
            matches.append(word)
 
    return matches

  def expand(prefix,mask,results,masks,rack):
    print('expand:', prefix, mask, masks, rack)
    mask = mask+masks[0]
    if len(results)==1:
      for word in results[0]:
        match = gen_match(prefix+word, mask)
        if match in rack:
          yield prefix + word
    else:
      for word in results[0]:
        match = gen_match(prefix+word, mask)
        if match in rack:
          for ex in expand(prefix+word+' ', mask, results[1:], masks[1:], rack):
            yield ex

  if not patts or len(patts)==0:
    return scan(rack, 1, len(rack))

  now = datetime.datetime.now()
  results =[]
  masks = []
  for patt in patts:
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
    min_len = len(mask)
    max_len = len(rack)+len(mask)
    matches = scan(rack, min_len, max_len, patt, mask)
    results.append(matches)
    masks.append(mask)
  print('compiling results took:', datetime.datetime.now()-now)
  now = datetime.datetime.now()
  n = 1
  for result in results:
    print(len(result), result)
    n *= len(result)
  print(n, 'combinations..')
  matches = []
  for group in expand('','',results,masks,rack):
    matches.append(group)
  td = datetime.datetime.now()-now
  microseconds = (td.days*24*60*60 + td.seconds)*1000000 + td.microseconds
  print(td, '= %d per second' % (n*1000000/microseconds))
  now = datetime.datetime.now()
  return matches
