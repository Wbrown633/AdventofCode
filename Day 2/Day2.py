from typing import List

# Convenience method that takes in an "Corrupted database" and returns a List[int].
# An Expense report is defined by the puzzle input, a text file with one integer per line.
def convert_database(input_file: str):
    f = open(input_file, "r")
    database_list = []
    for entry in f:
        database_list.append(entry.split())
    f.close()
    return database_list

# Given the corrupted password information return the status of the password
# The password information needs to be formatted as a list of strings as follows:
# ["min_number - max_number", letter, password]
# Where a valid "password" is a string of chars that contains "letter" at least 
# "min_number" of times and but no more than "max_number" of times
# a valid password returns True, invalid False
def validate_password(password_entry: List[str]):
    number_range = password_entry[0]
    letter = password_entry[1][0]  # Split the colon off of the required letter
    password = password_entry[2]

    numbers_split = number_range.split("-")
    min_number = int(numbers_split[0])
    max_number = int(numbers_split[1])

    count_of_chars = password.count(letter)

    return count_of_chars <= max_number and count_of_chars >= min_number

def validate_password_b(password_entry: List[str]):
    number_range = password_entry[0]
    letter = password_entry[1][0]  # Split the colon off of the required letter
    password = password_entry[2]

    numbers_split = number_range.split("-")
    # 0 index position numbers
    first_pos = int(numbers_split[0]) - 1
    second_pos = int(numbers_split[1]) - 1

    return (password[first_pos] == letter) ^ (password[second_pos] == letter)

if __name__ == "__main__":
    password_list = convert_database("input.txt")
    valid = 0
    for entry in password_list:
        if validate_password_b(entry):
            valid += 1
    print("Valid Passwords: ", valid)