import unittest
from solution import Solution


class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_example_1(self):
        """Test case: s = "abcabcbb", expected = 3"""
        s = "abcabcbb"
        expected = 3
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        """Test case: s = "bbbbb", expected = 1"""
        s = "bbbbb"
        expected = 1
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)
    
    def test_example_3(self):
        """Test case: s = "pwwkew", expected = 3"""
        s = "pwwkew"
        expected = 3
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)
    
    def test_empty_string(self):
        """Test case: s = "", expected = 0"""
        s = ""
        expected = 0
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)
        
    def test_single_character(self):
        """Test case: s = " ", expected = 1"""
        s = " "
        expected = 1
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)

    def test_all_unique(self):
        """Test case: s = "au", expected = 2"""
        s = "au"
        expected = 2
        result = self.solution.lengthOfLongestSubstring(s)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()