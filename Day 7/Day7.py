
class Bag_Rules:
    def __init__(self, rules: dict):
        self.bags = rules

    def find_paths_to_bag(self, color_to_find: str) -> int:
        """Traverse the graph of bag rules (represented by the `self.bags` dict)
        by starting at all possible starting nodes (keys) and traveling through 
        all possible links, stopping when either: `color_to_find` is encountered
        or an endpoint is reached (node with no outward links)."""
        colors_with_path = []
        for color in self.bags.keys():
            if self.search_path(color, color_to_find):
                print(color, "Has a path!")
                colors_with_path.append(color)
            
        return len(colors_with_path)
    
    def search_path(self, current_color: str, color_to_find: str) -> bool:
        if current_color == color_to_find:
            return True
        
        # Get the list of possible paths from this node
        colors_to_try = self.bags[current_color]

        for color in colors_to_try:
            if color == color_to_find:
                return True
            else:
                self.search_path(color, color_to_find)
                
        return False


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
