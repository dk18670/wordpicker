#!/usr/bin/python

import sys, math

def perm(s):
  # Compute the list of all permutations of s
  if len(s) <= 1:
    yield s
  else:
    i = 0
    l = len(s)
    for x in xrange(math.factorial(l)):
      yield s
      t = s[i]
      s[i] = s[i+1]
      s[i+1] = t
      i += 1
      if i>=l-1:
        i = 0

for item in perm(list(sys.argv[1])):
  print ''.join(item)
