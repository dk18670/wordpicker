#!/usr/bin/python

import sys

def perm(s):
  # Compute the list of all permutations of s
  if len(s) <= 1:
    yield s
  else:
    for i in xrange(len(s)):
      c = s[i]
      rest = s[:i] + s[i+1:]
      for x in perm(rest):
        yield [c] + x

for item in perm(list(sys.argv[1])):
  print ''.join(item)
