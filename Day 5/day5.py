
def find_seat(instruction_string):
    pass

def binary_split_rows(range_tuple, half):
    """Given a tuple representing the range of remaining options and the half
       of the range to keep either {F, B} return the new tuple. "F" means to 
       take the lower half and "B" means to take the upper half. In the special
       case where the range_tuple contains two ints that are not seperated by any
       integers then return only the single value. E.g. : (54, 55), F -> 54."""

    if half == "B":
        ishigh = True
    elif half == "F":
        ishigh = False
    else:
        raise ValueError("Invalid half marker, must be one of {F, B}")

    return binary_split(range_tuple, ishigh)

def binary_split(range_tuple, ishigh):
    lower = range_tuple[0]
    higher = range_tuple[1]

    if higher - lower == 1:
        if ishigh:
            return higher
        else:
            return lower
    
    midpoint = higher // 2  # integer division, floors the result

    if ishigh:
        return (midpoint + 1, higher)      
    else:
        return (lower, midpoint)

def binary_split_columns(range_tuple, half):
    if half == "R":
        ishigh = True
    elif half == "L":
        ishigh = False
    else:
        raise ValueError("Invalid half marker, must be one of {L, R}")

    return binary_split(range_tuple, ishigh)