from typing import List

# Given a list of integers find the two entries that sum to 2020 and return the value of
# those two entries multiplied together
def elf_finance(list_of_expenses: List[int]):
    int_1 = list_of_expenses.pop()
    int_2 = elf_finance_helper(int_1, list_of_expenses)
    if int_2:
        elf_value = int_1 * int_2
        return elf_value
    return elf_finance(list_of_expenses)

def elf_finance_helper(int_1: int, candidates: List[int]):
    for expense in candidates:
        if expense + int_1 == 2020:
            return expense
        
# Given a list of integers find the three entries that sum to 2020 and return the value of
# those three entries multiplied together
def elf_finance_b(list_of_expenses: List[int]):
    for int_1 in list_of_expenses:
        for int_2 in list_of_expenses:
            for int_3 in list_of_expenses:
                if int_1 + int_2 + int_3 == 2020:
                    return int_1 * int_2 * int_3
    return elf_finance_b(list_of_expenses)


# Convenience method that takes in an "Expense report" and returns a List[int].
# An Expense report is defined by the puzzle input, a text file with one integer per line.
def convert_expense_report(input_file: str):
    f = open(input_file, "r")
    expense_list = []
    for entry in f:
        expense_list.append(int(entry))
    f.close()
    return expense_list

if __name__ == "__main__":
    week_one_input = convert_expense_report("input_week_1.txt")
    elf_value = elf_finance_b(week_one_input)
    print("Elf Value: ", elf_value)
