import unittest

from app import *

class CalculatorTest(unittest.TestCase):
  def testEmpty(self):
    calculator = Calculator()
    result = calculator.add("")
    self.assertEqual(result, 0)
    return None

if __name__ == '__main__':
    unittest.main()