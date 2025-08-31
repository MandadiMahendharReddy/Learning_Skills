# test_calculator1.py
import unittest
import calculator1

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator1.add(10, 5), 15)
        self.assertEqual(calculator1.add(-1, 1), 0)

    def test_divide(self):
        self.assertEqual(calculator1.divide(10, 2), 5)
        with self.assertRaises(ValueError):
            calculator1.divide(10, 0)

if __name__ == '__main__':
    unittest.main()

#python -m unittest test_calculator1.py
