#!/usr/bin/python
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class testMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """Tests for module docsting"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_function_empty(self):
        arr = []
        self.assertIsNone(max_integer(arr))

    def test_start(self):
        arr = [45, 12, 5, 12, 31, 22]
        self.assertEqual(max_integer(arr), 45)

    def test_middle(self):
        arr = [45, 18, 89, 74, 30, 26]
        self.assertEqual(max_integer(arr), 89)

    def test_end(self):
        arr = [1, 56, 20, 47, 32, 600]
        self.assertEqual(max_integer(arr), 600)

    def test_has_negative(self):
        arr = [62, 49, 22, 61, -10, -782]
        self.assertEqual(max_integer(arr), 62)

    def test_all_negative(self):
        arr = [-20, -56, -25, -740, -32, -680]
        self.assertEqual(max_integer(arr), -20)

    def test_has_string(self):
        arr = [20, 5.6, "25", 740, 32, -680]
        with self.assertRaises(TypeError):
            max_integer(arr)


if __name__ == "__main__":
    unittest.main()
