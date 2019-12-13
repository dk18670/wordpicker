import collections

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
          raise Exception('Depleted character: %s'%c)
        c = '.'
      cpy[c] -= 1
    return cpy

  def __contains__(self,s):
    cpy = WPCounter(str(self))
    for c in s:
      if c=='.':
        continue
      if not cpy[c]:
        if not cpy['.']:
          return False
        c = '.'
      cpy[c] -= 1
    return True

  def substitutes(self,s):
    cpy = WPCounter(str(self))
    subs = []
    for i,c in enumerate(s):
      # Ignore non-alpha chars
      if c==' ':
        continue
      if not cpy[c]:
        if not cpy['.']:
          return None
        subs.append(i)
        c = '.'
      cpy[c] -= 1
    return subs
