import unittest
from solution import Solution


class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Test case: s = "III", expected = 3"""
        s = "III"
        expected = 3
        result = self.solution.romanToInt(s)
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        """Test case: s = "LVIII", expected = 58"""
        s = "LVIII"
        expected = 58
        result = self.solution.romanToInt(s)
        self.assertEqual(result, expected)
    
    def test_example_3(self):
        """Test case: s = "MCMXCIV", expected = 1994"""
        s = "MCMXCIV"
        expected = 1994
        result = self.solution.romanToInt(s)
        self.assertEqual(result, expected)
    
    def test_single_characters(self):
        """Test single roman numeral characters"""
        test_cases = [
            ("I", 1),
            ("V", 5),
            ("X", 10),
            ("L", 50),
            ("C", 100),
            ("D", 500),
            ("M", 1000)
        ]
        for s, expected in test_cases:
            with self.subTest(s=s):
                result = self.solution.romanToInt(s)
                self.assertEqual(result, expected)
    
    def test_subtraction_cases(self):
        """Test subtraction cases: IV, IX, XL, XC, CD, CM"""
        test_cases = [
            ("IV", 4),
            ("IX", 9),
            ("XL", 40),
            ("XC", 90),
            ("CD", 400),
            ("CM", 900)
        ]
        for s, expected in test_cases:
            with self.subTest(s=s):
                result = self.solution.romanToInt(s)
                self.assertEqual(result, expected)
    
    def test_complex_numbers(self):
        """Test complex roman numerals"""
        test_cases = [
            ("XIV", 14),      # 10 + 4
            ("XXIV", 24),     # 20 + 4
            ("XLIX", 49),     # 40 + 9
            ("XCIV", 94),     # 90 + 4
            ("CDXLIV", 444),  # 400 + 40 + 4
            ("MCDXLIV", 1444), # 1000 + 400 + 40 + 4
            ("MMCDXLIV", 2444) # 2000 + 400 + 40 + 4
        ]
        for s, expected in test_cases:
            with self.subTest(s=s):
                result = self.solution.romanToInt(s)
                self.assertEqual(result, expected)
    
    def test_edge_cases(self):
        """Test edge cases"""
        test_cases = [
            ("MMMCMXCIX", 3999),  # Maximum value
            ("XLII", 42),         # 40 + 2
            ("DCLXVI", 666),      # 500 + 100 + 50 + 10 + 5 + 1
        ]
        for s, expected in test_cases:
            with self.subTest(s=s):
                result = self.solution.romanToInt(s)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()