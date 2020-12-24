
def max_seat_id_of_inst_list(input_file: str):
    """Calculate the seat IDs for all the instruction stings in the input file. Then return
    the max calculated seat ID."""
    
    f = open(input_file, "r")
    seat_ids = []
    for instruction_string in f:
        string = instruction_string.strip("\n")
        seat_ids.append(find_seat_id(string))
    f.close()
    
    missing_id = find_missing_seat_id(seat_ids)
    print("Your Seat is: ", missing_id)
    return max(seat_ids)

def find_missing_seat_id(seat_ids: list):
    """For the second half of the prompt we are told to look for our seat. The prompt states that
    the entire plane is booked, and so our seat should the only seat ID that is missing from the list.
    To find the seat ID that's missing we first sort the incoming list of seat IDs that we calculated
    Then we construct a list of all valid seat IDs. After that we zip the list of all possible seat 
    ID's together with the list of seat IDs we've calculated. As we traverse the list at somepoint 
    our list of calculated seat IDs will be missing a value and will therefore skip past the value
    in the list of all possible seat IDs. At that moment we know that the value in the list of all
    possible seat IDs is an empty seat (because it doesn't appear in our list of seat IDs) and since
    we know that our seat is the only empty seat, we know we have found our seat and can stop searching."""
    
    seat_ids.sort()
    all_seats = range(seat_ids[0], seat_ids[-1])
    both_lists = zip(all_seats, seat_ids)
    for all_seat, seat_id in both_lists:
        if all_seat != seat_id:
            return all_seat
    
    raise ValueError("We searched the whole plane and couldn't find your seat!")

def find_seat_id(instruction_string):
    row_string = instruction_string[:7]
    column_string = instruction_string[7:]
    
    row = find_row(row_string)
    column = find_column(column_string)

    seat_id = row * 8 + column
    # print("Row: ", row, "Column: ", column)
    # print("Instruction: ", instruction_string, "Seat", seat_id )

    return seat_id

def find_row(instruction_string):
    """Iterate through all of the instructions in the given instruction string and
    return the row for the given seat as an int."""
    row_range = (0, 127)
    for instruction in instruction_string:
        row_range = binary_split_rows(row_range, instruction)
    
    return row_range

def find_column(instruction_string):
    """Iterate through all of the instructions in the given instruction string and 
    return the proper column for the seat as an int."""
    column_range = (0, 7)
    for instruction in instruction_string:
        column_range = binary_split_columns(column_range, instruction)
    
    return column_range

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
        raise ValueError("Invalid half marker, must be one of {F, B}, but was: ", half)

    return binary_split(range_tuple, ishigh)

def binary_split(range_tuple, ishigh):
    lower = range_tuple[0]
    higher = range_tuple[1]

    if higher - lower == 1:
        if ishigh:
            return higher
        else:
            return lower
    
    midpoint = (higher + lower) // 2  # integer division, floors the result

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
        raise ValueError("Invalid half marker, must be one of {L, R}, but was: ", half)

    return binary_split(range_tuple, ishigh)

if __name__ == "__main__":
    print(max_seat_id_of_inst_list("input.txt"))