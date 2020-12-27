import unittest
from Day7 import Bag_Rules, make_dict

class TestCases(unittest.TestCase):
    def test_file_input(self):
        rules = make_dict("test_input.txt")
        bag = Bag_Rules(rules)
        self.assertEqual(bag.find_paths_to_bag("shiny gold"), 4)

    def test_search_path(self):
        pass

    def test_find_paths_to_bag(self):
        pass