import unittest
from octal import Octal

class OctalTest(unittest.TestCase):
    # @unittest.skip
    def test_octal_1_is_decimal_1(self):
        self.assertEqual(1, Octal("1").to_decimal())

    # @unittest.skip
    def test_octal_10_is_decimal_8(self):
        self.assertEqual(8, Octal("10").to_decimal())

    # @unittest.skip
    def test_octal_17_is_decimal_15(self):
        self.assertEqual(15, Octal("17").to_decimal())

    # @unittest.skip
    def test_octal_11_is_decimal_9(self):
        self.assertEqual(9, Octal("11").to_decimal())

    # @unittest.skip
    def test_octal_130_is_decimal_88(self):
        self.assertEqual(88, Octal("130").to_decimal())

    # @unittest.skip
    def test_octal_2047_is_decimal_1063(self):
        self.assertEqual(1063, Octal("2047").to_decimal())

    # @unittest.skip
    def test_octal_7777_is_decimal_4095(self):
        self.assertEqual(4095, Octal("7777").to_decimal())

    # @unittest.skip
    def test_octal_1234567_is_decimal_342391(self):
        self.assertEqual(342391, Octal("1234567").to_decimal())

    # @unittest.skip
    def test_invalid_octal_is_decimal_0(self):
        self.assertEqual(0, Octal("carrot").to_decimal())

    # @unittest.skip
    def test_8_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("8").to_decimal())

    # @unittest.skip
    def test_9_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("9").to_decimal())

    # @unittest.skip
    def test_6789_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("6789").to_decimal())

    # @unittest.skip
    def test_abc1z_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("abc1z").to_decimal())

    # @unittest.skip
    def test_valid_octal_formatted_string_011_is_decimal_9(self):
        self.assertEqual(9, Octal("011").to_decimal())

    # @unittest.skip
    def test_234abc_is_seen_as_invalid_and_returns_0(self):
        self.assertEqual(0, Octal("234abc").to_decimal())

if __name__ == "__main__":
    unittest.main()