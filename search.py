import os, csv, re

BASE_DIR = os.path.dirname(__file__)

def gen_match(chars,mask):
  # remove the matched chars and leave the . chars
  # eg mask='P.AY.R' then match='.R..E.'
  match = ''.join(map(lambda x:x[0] if x[1]=='.' else '.', zip(chars,mask)))
  return match

def canmatch(chars,rack):
  # check that all chars are also in rack
  for c in chars:
    if c=='.' or c==' ':
      continue
    m = re.search(c,rack)
    if not m:
      m = re.search('\.',rack)
      if not m:
        return False
    rack = rack[:m.start()]+rack[m.end():]
    #del rack[m.start()]
  return True

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

  matches = []
  with open(os.path.join(BASE_DIR, 'sowpods.txt')) as file:
    reader = csv.reader(file)
    for row in reader:
      word = row[0]
      if not min_len <= len(word) <= max_len:
        continue
      if patt:
        m = re.search(patt, word)
        if m:
          match = gen_match(m.group(), mask)
          chars = word[:m.start()]+match+word[m.end():]
          if canmatch(chars,rack):
            matches.append(word)
      else:
        if canmatch(word,rack):
          matches.append(word)

  return matches

def search2(rack,patts):
  if not rack:
    return None

  # strip out any unwanted characters
  rack = re.sub('[^A-Z\.?_\-]','',rack.upper())
  # replace ?_- chars with .
  rack = re.sub('[?_\-]', '.', rack)

  def scan(rack, min_len, max_len, patt=None, mask=None):
    matches = []
    with open(os.path.join(BASE_DIR, 'sowpods.txt')) as file:
      reader = csv.reader(file)
      for row in reader:
        word = row[0]
        if not min_len <= len(word) <= max_len:
          continue
        if patt:
          m = re.search(patt, word)
          if m:
            match = gen_match(m.group(), mask)
            chars = word[:m.start()]+match+word[m.end():]
            if canmatch(chars,rack):
              matches.append(word)
        else:
          if canmatch(word,rack):
            matches.append(word)

    return matches

  def expand(prefix,mask,results,masks,rack):
    mask = mask+masks[0]
    if len(results)==1:
      for word in results[0]:
        match = gen_match(prefix+word, mask)
        if canmatch(match, rack):
          yield prefix + word
    else:
      for word in results[0]:
        match = gen_match(prefix+word, mask)
        if canmatch(match, rack):
          for ex in expand(prefix+word+' ', mask, results[1:], masks[1:], rack):
            yield ex

  if not patts or len(patts)==0:
    return scan(rack, 1, len(rack))

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
  matches = []
  for group in expand('','',results,masks,rack):
    matches.append(group)
  return matches
