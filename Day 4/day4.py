# The database of passports is presented 
def import_passport_db(input_file: str):
    f = open(input_file, "r")
    passport_db = []
    passports = f.read().split("\n\n")
    for entry in passports:
        passport = make_passport(entry)
        if passport:
            passport_db.append(passport)
    f.close()

    return passport_db

def make_passport(passport_entry):
    """A valid passport entry contains the following information:
           - byr (Birth Year)
           - iyr (Issue Year)
           - eyr (Expiration Year)
           - hgt (Height)
           - hcl (Hair Color)
           - ecl (Eye Color)
           - pid (Passport ID)
           - cid (Country ID)
           
           "passport_entry" is a string containing key:value pairs where the 
            keys are one of the above categories and the values are the value
            for this passport in that category.
            
            Ex. 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
            byr:1937 iyr:2017 cid:147 hgt:183cm'"""

    passport = {} 
    list_of_pairs = passport_entry.split()
    present_fields = []
    for pair in list_of_pairs:
        p = pair.split(":")
        passport[p[0]] = p[1]
        if not validate_passport_field(p[0], p[1]):
            print("Passport Failed: ", p[0])
            return None
        present_fields.append(p[0])
    if not check_req_fields_present(present_fields):
        print("Failed: Not all fields present")
        print("Fields: ", present_fields)
        return None
    return passport

def check_req_fields_present(list_of_values):
    if "cid" in list_of_values:
        list_of_values.remove("cid")
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    required_fields.sort()
    list_of_values.sort()
    return required_fields == list_of_values


def validate_passport_field(field, value):
    """Validate passport based on the given business logic:
        - byr (Birth Year) - four digits; at least 1920 and at most 2002.
        - iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        - eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        - hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        - hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        - ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        - pid (Passport ID) - a nine-digit number, including leading zeroes.
        - cid (Country ID) - ignored, missing or not."""

    if field == "byr":
        byr = int(value)
        valid = (byr >= 1920 and byr <= 2002)
        if not valid:
            print("Failed birthyear: ", value)
            return False
        else:
            return valid
    elif field == "iyr":
        iyr = int(value)
        valid = (iyr >= 2010 and iyr <= 2020)
        if not valid:
            print("Failed iyr: ", value)
            return False
        else:
            return valid
    elif field == "eyr":
        eyr = int(value)
        valid = (eyr >= 2020 and eyr <= 2030)
        if not valid:
            print("Failed eyr: ", value)
            return False
        else:
            return valid
    elif field == "hgt":
        if "in" in value:
            value = value.replace("in", "")
            value = int(value)
            return (value >= 59 and value <= 76)
        elif "cm" in value:
            value = value.replace("cm", "")
            value = int(value)
            return (value >= 150 and value <= 193)
        else:
            print("Failed height: ", value)
            return False
    elif field == "hcl":
        if len(value) != 7:
            print("Failed haircolor, invalid length: ", value)
            return False
        if "#" in value:
            legal_values = ["0", "1", "2", "3", "4", "5", "6", 
            "7", "8", "9", "a", "b", "c", "d", "e", "f", "#"]
            for letter in value:
                if letter not in legal_values:
                    print("Falied haircolor, illegal char: ", letter, "in ", value)
                    return False
            return True
        else:
            print("Failed haircolor, no #: ", value)
            return False
    elif field == "ecl":
        if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return True
        else:
            print("Failed ecl: ", value)
            return False
    elif field == "pid":
        if len(value) == 9:
            return is_int(value)
        else:
            print("Failed Passport ID: ", value)
            return False
    elif field == "cid":
        return True
    else:
        print("Invalid Field encountered: ", field)
        print("Invalid Value encountered: ", value)
        return False

def is_int(value):
    """Helper method, return True if value is an int, else false"""
    try:
        int(value)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    valid_passports = import_passport_db("input.txt")
    print("Number of valid passports: ", len(valid_passports))