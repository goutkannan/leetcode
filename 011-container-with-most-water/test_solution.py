import pytest
from solution import Solution


class TestContainerWithMostWater:
    def setup_method(self):
        self.solution = Solution()
    
    # Basic test cases from problem
    def test_example1(self):
        assert self.solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    
    def test_example2(self):
        assert self.solution.maxArea([1, 1]) == 1
    
    def test_example3(self):
        assert self.solution.maxArea([4, 3, 2, 1, 4]) == 16
    
    # Edge cases
    def test_two_elements_different_heights(self):
        assert self.solution.maxArea([1, 2]) == 1
    
    def test_two_elements_same_height(self):
        assert self.solution.maxArea([5, 5]) == 5
    
    def test_all_same_height(self):
        # Width = 4, Height = 3
        assert self.solution.maxArea([3, 3, 3, 3, 3]) == 12
    
    def test_ascending_heights(self):
        # Best is [1, 5] with area = min(1, 5) * 4 = 4
        assert self.solution.maxArea([1, 2, 3, 4, 5]) == 6
    
    def test_descending_heights(self):
        # Best is [5, 1] with area = min(5, 1) * 4 = 4
        assert self.solution.maxArea([5, 4, 3, 2, 1]) == 6
    
    # Complex cases
    def test_peak_in_middle(self):
        # Highest line in middle shouldn't necessarily be part of solution
        assert self.solution.maxArea([1, 3, 2, 5, 25, 24, 5]) == 24
    
    def test_multiple_same_max_heights(self):
        assert self.solution.maxArea([8, 1, 2, 3, 4, 5, 6, 7, 8]) == 64
    
    def test_zeros_in_array(self):
        # Best container: index 1 (height=2) to index 5 (height=4)
        # Area = min(2, 4) * (5 - 1) = 2 * 4 = 8
        assert self.solution.maxArea([0, 2, 0, 3, 0, 4]) == 8
    
    def test_large_numbers(self):
        assert self.solution.maxArea([10000, 10000]) == 10000
    
    def test_tall_lines_far_apart(self):
        # Lines at index 0 and 6 both have height 9
        assert self.solution.maxArea([9, 1, 1, 1, 1, 1, 9]) == 54
    
    def test_optimal_not_at_ends(self):
        # Sometimes optimal isn't using the full width
        assert self.solution.maxArea([1, 8, 100, 2, 100, 4, 8, 3, 7]) == 200
    
    # Performance edge case (conceptual - would need large array)
    def test_long_array(self):
        # Array of 100 elements, all height 5
        # Max area should be min(5,5) * 99 = 495
        height = [5] * 100
        assert self.solution.maxArea(height) == 495


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
