import unittest

from day3 import Toboggan, import_map, count_trees

class TestFinance(unittest.TestCase):
    
    def setUp(self):
        self.ex_map = import_map("example.txt")

    def test_count_trees_1(self):
        t1 = Toboggan(self.ex_map, 1, 1)      
        self.assertEqual(count_trees(t1), 2)
        
    def test_count_trees_2(self):
        t2 = Toboggan(self.ex_map, 3, 1)
        self.assertEqual(count_trees(t2), 7)

    def test_count_trees_3(self):
        t3 = Toboggan(self.ex_map, 5, 1)
        self.assertEqual(count_trees(t3), 3)
    
    def test_count_trees_4(self):
        t4 = Toboggan(self.ex_map, 7, 1)
        self.assertEqual(count_trees(t4), 4)
    
    def test_count_trees_5(self):
        t5 = Toboggan(self.ex_map, 1, 2)
        self.assertEqual(count_trees(t5), 2)


if __name__ == "__main__":
    unittest.main()