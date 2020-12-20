import unittest
from Day2 import validate_password, validate_password_b

class TestFinance(unittest.TestCase):
    
    def test_validate_password(self):
        self.assertTrue(validate_password(["1-3", "a:", "abcde"]))
        self.assertFalse(validate_password(["1-3", "b:", "cdefg"]))
    
    def test_validate_password_b(self):
        self.assertTrue(validate_password_b(["1-3", "a:", "abcde"]))
        self.assertFalse(validate_password_b(["1-3", "b:", "cdefg"]))

if __name__ == "__main__":
    unittest.main()