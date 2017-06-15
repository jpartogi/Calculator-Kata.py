import unittest

from app import *

class CalculatorTest(unittest.TestCase):
  def testEmpty(self):
    calculator = Calculator()
    result = calculator.add("")
    self.assertEqual(result, 0)
    return None

  def testOneNumber(self):
    calculator = Calculator()
    result = calculator.add("1")
    self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()