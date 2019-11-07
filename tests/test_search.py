import unittest

from search import WPCounter, gen_match, search, search2

class TestCases(unittest.TestCase):
  maxDiff = None

  def test_gen_match(self):
    result = gen_match('PAYER', 'P.Y.R')
    self.assertEqual(result, '.A.E.')

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

  def test_rack(self):
    matches = search('KEITHY', None)
    words = [(v[0]) for v in matches]
    results = ['EH', 'EIK', 'ET', 'ETH', 'HE', 'HET', 'HEY', 'HI', 'HIE', 'HIKE', 'HIT', 'HYE', 'HYKE', 'HYTE', 'IT', 'KET', 'KEY', 'KHET', 'KHI', 'KI', 'KIT', 'KITE', 'KITH', 'KITHE', 'KY', 'KYE', 'KYTE', 'KYTHE', 'TE', 'THE', 'THEY', 'THY', 'TI', 'TIE', 'TIKE', 'TYE', 'TYKE', 'YE', 'YEH', 'YET', 'YETI', 'YIKE', 'YITE']
    self.assertEqual(words, results)

  def test_rack_with_blanks(self):
    matches = search('P.X', None)
    results = [('AX', [0]), ('EX', [0]), ('OP', [0]), ('OX', [0]), ('PA', [1]), ('PAX', [1]), ('PE', [1]), ('PI', [1]), ('PIX', [1]), ('PO', [1]), ('POX', [1]), ('PYX', [1]), ('UP', [0]), ('XI', [1]), ('XU', [1])]
    self.assertEqual(matches, results)

  def test_rack_with_blanks_and_pattern(self):
    matches = search('P.R.', 'P.R.')
    results = [('APPRO', [0, 4]), ('PARA', [1, 3]), ('PARD', [1, 3]), ('PARE', [1, 3]), ('PARER', [1, 3]), ('PARK', [1, 3]), ('PARP', [1]), ('PARPS', [1, 4]), ('PARR', [1]), ('PARRA', [1, 4]), ('PARRS', [1, 4]), ('PARRY', [1, 4]), ('PARS', [1, 3]), ('PART', [1, 3]), ('PERE', [1, 3]), ('PERI', [1, 3]), ('PERK', [1, 3]), ('PERM', [1, 3]), ('PERN', [1, 3]), ('PERP', [1]), ('PERPS', [1, 4]), ('PERRY', [1, 4]), ('PERT', [1, 3]), ('PERV', [1, 3]), ('PIRL', [1, 3]), ('PIRN', [1, 3]), ('PIRS', [1, 3]), ('PORE', [1, 3]), ('PORER', [1, 3]), ('PORK', [1, 3]), ('PORN', [1, 3]), ('PORT', [1, 3]), ('PORY', [1, 3]), ('PURE', [1, 3]), ('PURER', [1, 3]), ('PURI', [1, 3]), ('PURL', [1, 3]), ('PURPY', [1, 4]), ('PURR', [1]), ('PURRS', [1, 4]), ('PURS', [1, 3]), ('PYRE', [1, 3]), ('PYRO', [1, 3])]
    self.assertEqual(matches, results)

  def test_rack_with_pattern_1(self):
    matches = search('KEITHY', 'TH')
    words = [(v[0]) for v in matches]
    results = ['ETH', 'HETH', 'HITHE', 'HYTHE', 'KHETH', 'KITH', 'KITHE', 'KYTHE', 'TETH', 'THE', 'THEY', 'THY', 'TITHE', 'TYTHE']
    self.assertEqual(words, results)

  def test_rack_with_pattern_2(self):
    matches = search('GAME', 'D')
    words = [(v[0]) for v in matches]
    results = ['AD', 'AGED', 'DA', 'DAE', 'DAG', 'DAM', 'DAME', 'DE', 'DEG', 'ED', 'EGAD', 'GAD', 'GADE', 'GAED', 'GAMED', 'GED', 'MAD', 'MADE', 'MADGE', 'MEAD', 'MED']
    self.assertEqual(words, results)

  def test_rack_with_multi_pattern(self):
    matches = search2('CHELSAY', ['$...$','$....$'])
    words = [(v[0]) for v in matches]
    results = [ 'ACH LEYS', 'ACH LYES', 'ACH LYSE', 'ACH SLEY', 'ALS YECH', 'AYS LECH', 'CEL ASHY', 'CEL HAYS', 'CEL SHAY', 'CEL YAHS', 'CHA LEYS', 'CHA LYES', 'CHA LYSE', 'CHA SLEY', 'CHE LAYS', 'CHE SLAY', 'CLY HAES', 'CLY SHEA', 'EAS LYCH', 'ECH LAYS', 'ECH SLAY', 'EHS ACYL', 'EHS CLAY', 'EHS LACY', 'ELS ACHY', 'ELS CHAY', 'HAY CELS', 'HES ACYL', 'HES CLAY', 'HES LACY', 'HEY LACS', 'HYE LACS', 'LAC HEYS', 'LAC HYES', 'LAH SCYE', 'LAH SYCE', 'LAS YECH', 'LAY SECH', 'LES ACHY', 'LES CHAY', 'LEY CASH', 'LEY CHAS', 'LYE CASH', 'LYE CHAS', 'SAC HYLE', 'SAE LYCH', 'SAL YECH', 'SAY LECH', 'SEA LYCH', 'SEC HYLA', 'SEL ACHY', 'SEL CHAY', 'SEY CHAL', 'SHE ACYL', 'SHE CLAY', 'SHE LACY', 'SHY ALEC', 'SHY LACE', 'SLY ACHE', 'SLY EACH', 'SYE CHAL', 'YAH CELS', 'YEH LACS', 'YES CHAL']
    self.assertEqual(words, results)

  def test_pattern(self):
    matches = search('', '$AZON')
    words = [(v[0]) for v in matches]
    results = ['AZON', 'AZONAL', 'AZONIC', 'AZONS']
    self.assertEqual(words, results)

if __name__ =='__main__':
  unittest.main()
