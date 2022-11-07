import unittest
from main import fibonacci

class TestFibonacci(unittest.TestCase):

    def test_fibonacci_negative_raise_exception(self):
        with self.assertRaises(ValueError):
            fibonacci(-10)

    def test_fibonacci_1_is_1(self):
        self.assertTrue(fibonacci(1) == 1)

    def test_fibonacci_9_is_34(self):
        self.assertEqual(fibonacci(9), 34)

if __name__ == '__main__':
    unittest.main()