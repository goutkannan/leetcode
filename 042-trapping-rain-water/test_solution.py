import pytest
from solution import Solution


class TestTrappingRainWater:
    def setup_method(self):
        self.solution = Solution()
    
    # Basic test cases from problem
    def test_example1(self):
        assert self.solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    
    def test_example2(self):
        assert self.solution.trap([4, 2, 0, 3, 2, 5]) == 9
    
    def test_example3(self):
        assert self.solution.trap([4, 2, 3]) == 1
    
    # Edge cases
    def test_single_element(self):
        assert self.solution.trap([5]) == 0
    
    def test_two_elements(self):
        assert self.solution.trap([3, 5]) == 0
    
    def test_three_elements_no_trap(self):
        # No water can be trapped with only 3 ascending elements
        assert self.solution.trap([1, 2, 3]) == 0
    
    def test_three_elements_with_trap(self):
        # Water trapped in the middle
        assert self.solution.trap([3, 0, 3]) == 3
    
    # All same height
    def test_all_same_height(self):
        assert self.solution.trap([2, 2, 2, 2, 2]) == 0
    
    def test_all_zeros(self):
        assert self.solution.trap([0, 0, 0, 0]) == 0
    
    # Ascending/Descending
    def test_strictly_ascending(self):
        # No water trapped in ascending sequence
        assert self.solution.trap([1, 2, 3, 4, 5]) == 0
    
    def test_strictly_descending(self):
        # No water trapped in descending sequence
        assert self.solution.trap([5, 4, 3, 2, 1]) == 0
    
    # Complex patterns
    def test_valley_pattern(self):
        # Single valley
        assert self.solution.trap([3, 0, 0, 2, 0, 4]) == 10
    
    def test_mountain_pattern(self):
        # Mountain - no water on top
        assert self.solution.trap([0, 1, 2, 3, 2, 1, 0]) == 0
    
    def test_multiple_valleys(self):
        # Multiple valleys at different levels
        assert self.solution.trap([5, 1, 5, 1, 5]) == 8
    
    def test_staircase_up_then_down(self):
        # Stairs going up then down
        assert self.solution.trap([0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]) == 8
    
    # Water trapped with zeros
    def test_zeros_in_middle(self):
        # Deep valley with zeros
        assert self.solution.trap([4, 0, 0, 0, 4]) == 12
    
    def test_zeros_at_ends(self):
        # Zeros at the beginning and end don't trap water
        # Water: indices 3,4 (4 each) + indices 6,7 (3 each) = 14
        assert self.solution.trap([0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 0]) == 14
    
    # Edge case patterns
    def test_single_peak(self):
        # Single tall peak in middle
        assert self.solution.trap([2, 0, 2]) == 2
    
    def test_plateau(self):
        # Flat sections
        assert self.solution.trap([3, 0, 0, 0, 3]) == 9
    
    def test_unequal_walls(self):
        # Different height walls - water limited by shorter wall
        assert self.solution.trap([5, 1, 3]) == 2
    
    def test_complex_elevation(self):
        # Complex pattern with multiple peaks and valleys
        assert self.solution.trap([6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 2]) == 45
    
    # Large values
    def test_large_heights(self):
        assert self.solution.trap([10000, 0, 10000]) == 10000
    
    # Realistic patterns
    def test_gradual_rise_and_fall(self):
        assert self.solution.trap([0, 2, 1, 3, 0, 1, 2, 1, 2, 1]) == 5


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
