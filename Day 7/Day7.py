
class Bag_Rules:
    def __init__(self, file: str):
        self.bags = make_dict(file)


def make_dict(file: str) -> dict:
    """Take in the input file containing lines with the following format:
    [color] bags contain [qty] [color] bag, [qty] [color] bags.
    
    These colors should be broken out and stored in two categories: Containers and
    Contained. The containers will be the Keys and the contained are the values"""
    f = open(file, "r")
    lines = f.readlines()

    bag_rules = {}
    
    for line in lines:
        split_line = line.split(" contain ")
        container = split_line.pop(0).strip()
        contained = split_line
        bag_rules[container] = contained
        
    return bag_rules
