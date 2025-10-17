import unittest
from solution import Solution


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Test case: nums = [2,7,11,15], target = 9"""
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_example_2(self):
        """Test case: nums = [3,2,4], target = 6"""
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_example_3(self):
        """Test case: nums = [3,3], target = 6"""
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_negative_numbers(self):
        """Test case with negative numbers"""
        nums = [-1, -2, -3, -4, -5]
        target = -8
        expected = [2, 4]  # -3 + -5 = -8
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))
    
    def test_zero_target(self):
        """Test case with zero target"""
        nums = [0, 4, 3, 0]
        target = 0
        expected = [0, 3]  # 0 + 0 = 0
        result = self.solution.twoSum(nums, target)
        self.assertEqual(sorted(result), sorted(expected))


if __name__ == '__main__':
    unittest.main()