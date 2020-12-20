import unittest

from day4 import import_passport_db, validate_passport_field

class TestFinance(unittest.TestCase):
    
    """def test_valid_passports_ex(self):
        valid_passports = import_passport_db("example.txt")
        self.assertEqual(len(valid_passports), 2)"""
    
    """def test_valid_passports_input(self):
        valid_passports_1 = import_passport_db("input.txt")
        self.assertEqual(len(valid_passports_1), 245)"""

    def test_invalid_passports(self):
        invalid_passports = import_passport_db("invalid_passports.txt")
        self.assertEqual(invalid_passports, []) # there should be no valid passports in this list

    def test_valid_passports(self):
        valid_passports = import_passport_db("valid_passports.txt")
        self.assertEqual(len(valid_passports), 4)

    def test_valid_byr_field(self):
        self.assertEqual(validate_passport_field("byr", "1920"), True)
        self.assertEqual(validate_passport_field("byr", "2002"), True)
        self.assertEqual(validate_passport_field("byr", "1996"), True)

    def test_invalid_byr_field(self):
        self.assertEqual(validate_passport_field("byr", "-100"), False)
        self.assertEqual(validate_passport_field("byr", "2020"), False)
        self.assertEqual(validate_passport_field("byr", "1919"), False)

    def test_valid_iyr_field(self):
        self.assertEqual(validate_passport_field("iyr", "2010"), True)
        self.assertEqual(validate_passport_field("iyr", "2015"), True)
        self.assertEqual(validate_passport_field("iyr", "2020"), True)

    def test_invalid_iyr_field(self):
        self.assertEqual(validate_passport_field("iyr", "2009"), False)
        self.assertEqual(validate_passport_field("iyr", "-2000"), False)
        self.assertEqual(validate_passport_field("iyr", "2021"), False)

    def test_valid_eyr_field(self):
        self.assertEqual(validate_passport_field("eyr", "2020"), True)
        self.assertEqual(validate_passport_field("eyr", "2025"), True)
        self.assertEqual(validate_passport_field("eyr", "2030"), True)

    def test_invalid_eyr_field(self):
        self.assertEqual(validate_passport_field("eyr", "2000"), False)
        self.assertEqual(validate_passport_field("eyr", "2019"), False)
        self.assertEqual(validate_passport_field("eyr", "2031"), False)

    def test_valid_hgt_field(self):
        self.assertEqual(validate_passport_field("hgt", "150cm"), True)
        self.assertEqual(validate_passport_field("hgt", "193cm"), True)
        self.assertEqual(validate_passport_field("hgt", "160 cm"), True)
        self.assertEqual(validate_passport_field("hgt", "59in"), True)
        self.assertEqual(validate_passport_field("hgt", "76in"), True)
        self.assertEqual(validate_passport_field("hgt", "69 in"), True)

    def test_invalid_hgt_field(self):
        self.assertEqual(validate_passport_field("hgt", "150"), False)
        self.assertEqual(validate_passport_field("hgt", "200cm"), False)
        self.assertEqual(validate_passport_field("hgt", "1cm"), False)
        self.assertEqual(validate_passport_field("hgt", "59"), False)
        self.assertEqual(validate_passport_field("hgt", "5in"), False)
        self.assertEqual(validate_passport_field("hgt", "690in"), False)

    def test_valid_hcl_field(self):
        self.assertEqual(validate_passport_field("hcl", "#0123af"), True)
        self.assertEqual(validate_passport_field("hcl", "#aabc12"), True)
        self.assertEqual(validate_passport_field("hcl", "#0a1d3a"), True)

    def test_invalid_hcl_field(self):
        self.assertEqual(validate_passport_field("hcl", "0123af"), False)
        self.assertEqual(validate_passport_field("hcl", "2019"), False)
        self.assertEqual(validate_passport_field("hcl", "#0a1d3aad"), False)
        self.assertEqual(validate_passport_field("hcl", "#012 3af"), False)
        self.assertEqual(validate_passport_field("hcl", "#axbc12"), False)

    def test_valid_ecl_field(self):
        self.assertEqual(validate_passport_field("ecl", "amb"), True)
        self.assertEqual(validate_passport_field("ecl", "blu"), True)
        self.assertEqual(validate_passport_field("ecl", "brn"), True)
        self.assertEqual(validate_passport_field("ecl", "gry"), True)
        self.assertEqual(validate_passport_field("ecl", "grn"), True)
        self.assertEqual(validate_passport_field("ecl", "hzl"), True)
        self.assertEqual(validate_passport_field("ecl", "oth"), True)

    def test_invalid_ecl_field(self):
        self.assertEqual(validate_passport_field("ecl", "0123af"), False)
        self.assertEqual(validate_passport_field("ecl", "2019"), False)
        self.assertEqual(validate_passport_field("ecl", "#0a1d3aad"), False)
        self.assertEqual(validate_passport_field("ecl", "#012 3af"), False)
        self.assertEqual(validate_passport_field("ecl", "#axbc12"), False)
        self.assertEqual(validate_passport_field("ecl", "ambblu"), False)
        self.assertEqual(validate_passport_field("ecl", "amb blu"), False)

    def test_valid_pid_field(self):
        self.assertEqual(validate_passport_field("pid", "000000000"), True)
        self.assertEqual(validate_passport_field("pid", "101010101"), True)
        self.assertEqual(validate_passport_field("pid", "000223109"), True)
        self.assertEqual(validate_passport_field("pid", "000044556"), True)
        self.assertEqual(validate_passport_field("pid", "000000012"), True)

    def test_invalid_pid_field(self):
        self.assertEqual(validate_passport_field("pid", "1"), False)
        self.assertEqual(validate_passport_field("pid", "00000001"), False)
        self.assertEqual(validate_passport_field("pid", "10123"), False)
        self.assertEqual(validate_passport_field("pid", "#012 3af"), False)
        self.assertEqual(validate_passport_field("pid", "1010 00023"), False)

    def test_valid_cid_field(self):
        self.assertEqual(validate_passport_field("cid", "000000000"), True)
        self.assertEqual(validate_passport_field("cid", "101010101"), True)
        self.assertEqual(validate_passport_field("cid", "as;dljf;alsjd   as;ldkfja  asdf"), True)
        self.assertEqual(validate_passport_field("cid", "102938102983$!@#!@#"), True)
        self.assertEqual(validate_passport_field("cid", "12"), True)

    
    
        
if __name__ == "__main__":
    unittest.main()