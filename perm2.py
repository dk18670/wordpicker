#!/usr/bin/python

import sys, math

def swap(s,i):
  return s[:i]+s[i+1]+s[i]+s[i+1+1:]

def perm(s):
  # Compute the list of all permutations of s
  if len(s) <= 1:
    yield s
  else:
    i = 0
    for x in xrange(math.factorial(len(s))):
      yield s
      s = swap(s,i)
      i += 1
      if i>=len(s)-1:
        i = 0

for item in perm(sys.argv[1]):
  print item
