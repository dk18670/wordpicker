import unittest

from wpcounter import WPCounter

class TestCases(unittest.TestCase):
  #maxDiff = None

  def test_canmatch(self):
    result = 'PAYER' in WPCounter('P.Y.R')
    self.assertEqual(result, True)

  def test_sustitutes(self):
    result = WPCounter('REAL..ING').substitutes('TRING')
    self.assertEqual(result, [0])
    result = WPCounter('REAL..ING').substitutes('HELP')
    self.assertEqual(result, [0,3])
    result = WPCounter('REAL..ING').substitutes('LEAVE')
    self.assertEqual(result, [3,4])
    result = WPCounter('REAL..ING').substitutes('ZIONIST')
    self.assertEqual(result, None)

if __name__ =='__main__':
  unittest.main()
