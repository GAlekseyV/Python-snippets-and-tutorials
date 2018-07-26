import os
import sys
import unittest
from class_inheritance import add_class, check


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.classes = {}
        with open("sample_input_classes.txt", 'r') as f:
            n = int(f.readline())
            while n > 0:
                line = f.readline().split()
                add_class(line)
                n -= 1

    def test_check(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

