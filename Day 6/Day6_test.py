import unittest
from Day6 import parse_form, parse_form_group

class TestCase(unittest.TestCase):
    def test_parse_form(self):
        """
        docstring
        """
        self.assertEqual(parse_form("test_input.txt"), 11)

    def test_parse_form_group(self):
        """
        docstring
        """
        self.assertEqual(parse_form_group("abcx\nabcy\nabcz\n"), 6)

    def test_parse_form_group_all_yes(self):
        self.assertEqual(parse_form_group_all_yes("abc"), 3)

    