def parse_form(file: str):
    """
    Given a text file representing the puzzle input, return the sum of unique
    letters per grouping. Group answers are seperated by a blank line.
    """
    f = open(file, "r")
    groups = create_groups(f.read())
    sum = 0
    for group in groups:
        sum += parse_form_group(group)

    return sum

def create_groups(file_contents: str):
    return file_contents.split("\n\n")

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
    print("Total sum of group answers:", parse_form("input.txt"))