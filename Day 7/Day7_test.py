import unittest
from Day7 import Bag_Rules, make_dict

class TestCases(unittest.TestCase):
    def test_file_input(self):
        rules = make_dict("test_input.txt")
        bag = Bag_Rules(rules)
        self.assertEqual(bag.find_paths_to_bag("shiny gold"), 4)

    def test_search_path_basic(self):
        # mirrored beige bags contain 1 drab brown bag, 3 dotted crimson bags
        rules = {"mirrored beige" : ["drab brown", "dotted crimson"]}
        test_bag = Bag_Rules(rules)
        self.assertEqual(test_bag.find_paths_to_bag("drab brown"), 1)

    def test_search_path_example(self):
        rules = {"light red" : ["bright white", "muted yellow"],
                 "dark orange" : ["bright white", "muted yellow"],
                 "bright white" : ["shiny gold"],
                 "muted yellow" : ["shiny gold", "faded blue"],
                 "shiny gold" : ["dark olive", "vibrant plum"],
                 "dark olive" : ["faded blue", "dotted black"],
                 "vibrant plum" : ["faded blue", "dotted black"],
                 "faded blue" : [],
                 "dotted black" : []}
        test_bag = Bag_Rules(rules)
        self.assertEqual(test_bag.find_paths_to_bag("shiny gold"), 4)

    def test_find_paths_to_bag(self):
        pass