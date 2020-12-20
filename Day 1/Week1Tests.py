import unittest
from Week1 import elf_finance, convert_expense_report, elf_finance_b

class TestFinance(unittest.TestCase):

    def test_elf_finance_example(self):
        example_list = convert_expense_report("example_input.txt")
        self.assertEqual(elf_finance(example_list), 514579)
    
    def test_elf_finance_example_b(self):
        example_list_b = convert_expense_report("example_input.txt")
        self.assertEqual(elf_finance_b(example_list_b),241861950)

if __name__ == "__main__":
    unittest.main()