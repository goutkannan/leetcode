from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Given an array of integers nums and an integer target, return indices of the 
        two numbers such that they add up to target.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices that sum to target
        """
        num_dict = {target-nums[0]: 0}
        for idx, num in enumerate(nums[1:], start=1):
            if num in num_dict:
                return [num_dict[num], idx]
            num_dict[target - num] = idx