import unittest

from search import gen_match, search, search2

class TestCases(unittest.TestCase):
  #maxDiff = None

  def test_gen_match(self):
    result = gen_match('PAYER', 'P.Y.R')
    self.assertEqual(result, '.A.E.')

  def test_rack(self):
    matches = search('KEITHY', None)
    results = ['EH', 'EIK', 'ET', 'ETH', 'HE', 'HET', 'HEY', 'HI', 'HIE', 'HIKE', 'HIT', 'HYE', 'HYKE', 'HYTE', 'IT', 'KET', 'KEY', 'KHET', 'KHI', 'KI', 'KIT', 'KITE', 'KITH', 'KITHE', 'KY', 'KYE', 'KYTE', 'KYTHE', 'TE', 'THE', 'THEY', 'THY', 'TI', 'TIE', 'TIKE', 'TYE', 'TYKE', 'YE', 'YEH', 'YET', 'YETI', 'YIKE', 'YITE']
    self.assertEqual(matches, results)

  def test_rack_with_blanks(self):
    matches = search('P.X', None)
    results = ['AX', 'EX', 'OP', 'OX', 'PA', 'PAX', 'PE', 'PI', 'PIX', 'PO', 'POX', 'PYX', 'UP', 'XI', 'XU']
    self.assertEqual(matches, results)

  def test_rack_with_blanks_and_pattern(self):
    matches = search('P.R.', 'P.R.')
    results = ['APPRO', 'PARA', 'PARD', 'PARE', 'PARER', 'PARK', 'PARP', 'PARPS', 'PARR', 'PARRA', 'PARRS', 'PARRY', 'PARS', 'PART', 'PERE', 'PERI', 'PERK', 'PERM', 'PERN', 'PERP', 'PERPS', 'PERRY', 'PERT', 'PERV', 'PIRL', 'PIRN', 'PIRS', 'PORE', 'PORER', 'PORK', 'PORN', 'PORT', 'PORY', 'PURE', 'PURER', 'PURI', 'PURL', 'PURPY', 'PURR', 'PURRS', 'PURS', 'PYRE', 'PYRO']
    self.assertEqual(matches, results)

  def test_rack_with_pattern_1(self):
    matches = search('KEITHY', 'TH')
    results = ['ETH', 'HETH', 'HITHE', 'HYTHE', 'KHETH', 'KITH', 'KITHE', 'KYTHE', 'TETH', 'THE', 'THEY', 'THY', 'TITHE', 'TYTHE']
    self.assertEqual(matches, results)

  def test_rack_with_pattern_2(self):
    matches = search('GAME', 'D')
    results = ['AD', 'AGED', 'DA', 'DAE', 'DAG', 'DAM', 'DAME', 'DE', 'DEG', 'ED', 'EGAD', 'GAD', 'GADE', 'GAED', 'GAMED', 'GED', 'MAD', 'MADE', 'MADGE', 'MEAD', 'MED']
    self.assertEqual(matches, results)

  def test_rack_with_pattern_3(self):
    matches = search('KEITH', '$...$')
    results = ['EIK', 'ETH', 'HET', 'HIE', 'HIT', 'KET', 'KHI', 'KIT', 'THE', 'TIE']
    self.assertEqual(matches, results)

  def test_pattern(self):
    matches = search('', '$AZON')
    results = ['AZON', 'AZONAL', 'AZONIC', 'AZONS']
    self.assertEqual(matches, results)

  def test_rack_with_multi_pattern(self):
    matches = search2('CHELSAY', ['$...$','$....$'])
    results = [ 'ACH LEYS', 'ACH LYES', 'ACH LYSE', 'ACH SLEY', 'ALS YECH', 'AYS LECH', 'CEL ASHY', 'CEL HAYS', 'CEL SHAY', 'CEL YAHS', 'CHA LEYS', 'CHA LYES', 'CHA LYSE', 'CHA SLEY', 'CHE LAYS', 'CHE SLAY', 'CLY HAES', 'CLY SHEA', 'EAS LYCH', 'ECH LAYS', 'ECH SLAY', 'EHS ACYL', 'EHS CLAY', 'EHS LACY', 'ELS ACHY', 'ELS CHAY', 'HAY CELS', 'HES ACYL', 'HES CLAY', 'HES LACY', 'HEY LACS', 'HYE LACS', 'LAC HEYS', 'LAC HYES', 'LAH SCYE', 'LAH SYCE', 'LAS YECH', 'LAY SECH', 'LES ACHY', 'LES CHAY', 'LEY CASH', 'LEY CHAS', 'LYE CASH', 'LYE CHAS', 'SAC HYLE', 'SAE LYCH', 'SAL YECH', 'SAY LECH', 'SEA LYCH', 'SEC HYLA', 'SEL ACHY', 'SEL CHAY', 'SEY CHAL', 'SHE ACYL', 'SHE CLAY', 'SHE LACY', 'SHY ALEC', 'SHY LACE', 'SLY ACHE', 'SLY EACH', 'SYE CHAL', 'YAH CELS', 'YEH LACS', 'YES CHAL']
    self.assertEqual(matches, results)

if __name__ =='__main__':
  unittest.main()
