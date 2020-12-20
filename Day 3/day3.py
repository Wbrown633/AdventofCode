# The map for our toboggan journey is presented 
def import_map(input_file: str):
    f = open(input_file, "r")
    toboggan_map = []

    for line in f:
        list_contents = list(line)
        # clean up the formatting of the map we get (we don't care about new lines)
        if '\n' in list_contents:
            list_contents.remove('\n')
        toboggan_map.append(list_contents)
    f.close()

    return toboggan_map

# Count the number of times the tree character '#' occurs when iterating
def count_trees(toboggan_iterator):
    trees = 0
    for character in toboggan_iterator:
        if character == "#":
            trees += 1
    return trees
        

# Given a 'toboggan map'(defined below) traverse it diagonally downward with a given slope
# defined by given ints 'x_slope' and 'y_slope'. This class is an iterator and returns the
# character encountered at each level of the map when traveresed in this way.
# A map is defined as: a 2D array of chars either
#   "." - which represents an empty space or
#   "#" - which represents a tree
# Each row in the horizontal direction is assumed to repeat infinitely in the X plane.
# This should be handled in the code by causing the counter to wrap around to the beginning of
# the row when it encounters and edge.
class Toboggan:
    # constructor    
    def __init__(self, toboggan_map, x_slope, y_slope):   
        self.toboggan_map = toboggan_map
        self.xposn = 0
        self.yposn = 0
        self.width = len(toboggan_map[0])
        self.height = len(toboggan_map)
        self.x_slope = x_slope
        self.y_slope = y_slope

    def __iter__(self):
        self.xposn = 0
        self.yposn = 0
        return self

    # down 1 over 3
    def __next__(self):
        if (self.yposn + self.y_slope) < self.height: 
            self.yposn += self.y_slope
        else:
            raise StopIteration("No more items in the map")
        if (self.xposn + self.x_slope) < self.width:
            self.xposn += self.x_slope
        else:
            self.xposn = self.x_slope - (self.width - self.xposn)
        
        return self.toboggan_map[self.yposn][self.xposn] 


if __name__ == "__main__":
    t_map = import_map("input.txt")
    t0 = Toboggan(t_map, 1, 1)
    t1 = Toboggan(t_map, 3, 1)
    t2 = Toboggan(t_map, 5, 1)
    t3 = Toboggan(t_map, 7, 1)
    t4 = Toboggan(t_map, 1, 2)
    
    c0 = count_trees(t0)
    c1 = count_trees(t1)
    c2 = count_trees(t2)
    c3 = count_trees(t3)
    c4 = count_trees(t4)

    # Find the counts of the number of trees and multiply together for part B's answer
    counts = c0 * c1 * c2 * c3 * c4
    print(c0, c1, c2, c3, c4)
    print("Multiplied counts of trees: ", counts) # Answer to Day 3 Part B