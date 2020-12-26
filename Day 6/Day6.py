def parse_form(file: str, all_yes: bool):
    """
    Given a text file representing the puzzle input, return the sum of unique
    letters per grouping. Group answers are seperated by a blank line.
    """
    f = open(file, "r")
    groups = create_groups(f.read())
    sum = 0
    for group in groups:
        if all_yes:    
            sum += parse_form_group_all_yes(group)
        else:
            sum += parse_form_group(group)

    return sum

def create_groups(file_contents: str):
    return file_contents.split("\n\n")

def parse_form_group_all_yes(group_contents: str) -> int:
    """Given the answers from one group, return a count of questions for which
    ALL group memebers answered YES. Practically this means the letters that appear
    in all lines of the input."""

    letter_counts = {}
    all_answered = []
    num_of_group_members = 0
    sum_of_answers = 0

    # Count how many times each letter occurs in the group input, including newline
    for char in group_contents:
        if char not in letter_counts.keys():
            letter_counts[char] = 1
        else:
            letter_counts[char] += 1

    print(letter_counts)
    num_of_group_members = find_num_of_group_members(letter_counts)

    for char in letter_counts.keys():
        if letter_counts[char] == num_of_group_members:
            print("Letter: ", char, "Add: ", letter_counts[char])
            sum_of_answers += letter_counts[char]

    return sum_of_answers

def find_num_of_group_members(answers: dict) -> int:
    """Identify the number of group members (# of '\n' chars + 1)"""

    if "\n" in answers.keys():
        return answers["\n"] + 1
    else:
        return 1

def parse_form_group(answers: str) -> int:
    """Given the answers from one group, return a count of questions people 
    in this group answered yes to."""
    letters = []
    answers = answers.replace("\n", "")
    for char in answers:
        if char not in letters:
            letters.append(char)

    return len(letters)


if __name__ == "__main__":
    print("Total sum of group answers:", parse_form("input.txt", False))
    print("Total sum of all group yes: ", parse_form("input.txt", True))