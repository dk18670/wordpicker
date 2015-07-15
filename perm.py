#!/usr/bin/python

import sys

def perm(l):
  # Compute the list of all permutations of l
  if len(l) <= 1:
    yield l
  else:
    for i in range(len(l)):
      s = l[:i] + l[i+1:]
      p = perm(s)
      for x in p:
	yield l[i:i+1] + x

for item in perm(sys.argv[1]):
  print item
