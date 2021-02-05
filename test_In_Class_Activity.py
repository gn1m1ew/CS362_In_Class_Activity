import unittest
import In_Class_Activity

class TestCase(unittest.TestCase):

	def test_add(self):
		self.assertEqual(In_Class_Activity.add(2, 1), 3)

	def test_sub(self):
		self.assertEqual(In_Class_Activity.sub(3, 1), 2)

	def test_mul(self):
		self.assertEqual(In_Class_Activity.mul(3, 2), 6)

	def test_div(self):
		self.assertEqual(In_Class_Activity.div(6, 2), 3)

if __name__ == '__main__':
	unittest.main(verbosity=2)