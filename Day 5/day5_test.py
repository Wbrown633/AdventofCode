import unittest
from day5 import binary_split_columns, binary_split_rows, find_seat_id, find_column, find_row


class testDay5(unittest.TestCase):
        
    def test_binary_split_columns(self):
        """
        INPUT: RLR
        Start by considering the whole range, columns 0 through 7.
        R means to take the upper half, keeping columns 4 through 7.
        L means to take the lower half, keeping columns 4 through 5.
        The final R keeps the upper of the two, column 5."""
        
        self.assertEqual(binary_split_columns((0, 7), "R"), (4, 7))
        self.assertEqual(binary_split_columns((4, 7), "L"), (4, 5))
        self.assertEqual(binary_split_columns((4, 5), "R"), 5)

    def test_binary_split_rows(self):
        """
        INPUT: FBFBBFF
        Start by considering the whole range, rows 0 through 127.
        F means to take the lower half, keeping rows 0 through 63.
        B means to take the upper half, keeping rows 32 through 63.
        F means to take the lower half, keeping rows 32 through 47.
        B means to take the upper half, keeping rows 40 through 47.
        B keeps rows 44 through 47.
        F keeps rows 44 through 45.
        The final F keeps the lower of the two, row 44."""

        self.assertEqual(binary_split_rows((0, 127), "F"), (0, 63))
        self.assertEqual(binary_split_rows((0, 63), "B"), (32, 63))
        self.assertEqual(binary_split_rows((32, 63), "F"), (32, 47))
        self.assertEqual(binary_split_rows((32, 47), "B"), (40, 47))
        self.assertEqual(binary_split_rows((40, 47), "B"), (44, 47))
        self.assertEqual(binary_split_rows((44, 47), "F"), (44, 45))
        self.assertEqual(binary_split_rows((44, 45), "F"), 44)

    def test_find_column(self):
        self.assertEqual(find_column("RLR"), 5)
        self.assertEqual(find_column("RRR"), 7)
        self.assertEqual(find_column("RLL"), 4)

    def test_find_row(self):
        self.assertEqual(find_row("FBFBBFF"), 44)
        self.assertEqual(find_row("BFFFBBF"), 70)
        self.assertEqual(find_row("FFFBBBF"), 14)
        self.assertEqual(find_row("BBFFBBF"), 102)

    def test_find_seat_id(self):
        """
        FBFBBFFRLR: row 44, column 5, seat ID 357
        BFFFBBFRRR: row 70, column 7, seat ID 567.
        FFFBBBFRRR: row 14, column 7, seat ID 119.
        BBFFBBFRLL: row 102, column 4, seat ID 820"""

        self.assertEqual(find_seat_id("FBFBBFFRLR"), 357)
        self.assertEqual(find_seat_id("BFFFBBFRRR"), 567)
        self.assertEqual(find_seat_id("FFFBBBFRRR"), 119)
        self.assertEqual(find_seat_id("BBFFBBFRLL"), 820)


if __name__ == "__main__":
    unittest.main()