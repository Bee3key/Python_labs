#testsplitter.py

import splitter
# import doctest

# nfail, ntest = doctest.testmod(splitter, verbose=True)

# testsplitter.py

import unittest

# ¬«¨£¤¥½ §½
class TestSplitFunction(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	def testsimplestring(self):
		r = splitter.split('GOOG 100 490.50')
		self.assertEqual(r,['GOOG','100','490.50'])
	def testtypeconvert(self):
		r = splitter.split('GOOG 100 490.50',[str, int, float])
		self.assertEqual(r,['GOOG', 100, 490.5])
	def testdelimiter(self):
		r = splitter.split('GOOG,100,490.50',delimiter=',')
		self.assertEqual(r,['GOOG','100','490.50'])
	def testHalf(self):
		r = splitter.half(6.8)
		self.assertEqual(r, 3.4)

if __name__ == '__main__':
	unittest.main()

