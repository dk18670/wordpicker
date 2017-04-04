import unittest

import search

class TestCases(unittest.TestCase):

  def test_gen_match(self):
    result = search.gen_match('PAYER', 'P.Y.R')
    self.assertEqual(result, '.A.E.')

  def test_canmatch(self):
    result = search.canmatch('PAYER', 'P.Y.R')
    self.assertEqual(result, True)

  def test_rack(self):
    matches = search.search('KEITHY', None)
    results = ['EH', 'EIK', 'ET', 'ETH', 'HE', 'HET', 'HEY', 'HI', 'HIE', 'HIKE', 'HIT', 'HYE', 'HYKE', 'HYTE', 'IT', 'KET', 'KEY', 'KHET', 'KHI', 'KI', 'KIT', 'KITE', 'KITH', 'KITHE', 'KY', 'KYE', 'KYTE', 'KYTHE', 'TE', 'THE', 'THEY', 'THY', 'TI', 'TIE', 'TIKE', 'TYE', 'TYKE', 'YE', 'YEH', 'YET', 'YETI', 'YIKE', 'YITE']
    self.assertEqual(matches, results)

  def test_rack_with_pattern(self):
    matches = search.search('KEITHY', 'TH')
    results = ['ETH', 'HETH', 'HITHE', 'HYTHE', 'KHETH', 'KITH', 'KITHE', 'KYTHE', 'TETH', 'THE', 'THEY', 'THY', 'TITHE', 'TYTHE']
    self.assertEqual(matches, results)

if __name__ =='__main__':
  unittest.main()
