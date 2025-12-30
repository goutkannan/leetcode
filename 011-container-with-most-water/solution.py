class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Find two lines that together with the x-axis form a container
        that contains the most water.
        
        Args:
            height: List of integers representing line heights
            
        Returns:
            int: Maximum amount of water a container can store
            
        Examples:
            >>> Solution().maxArea([1,8,6,2,5,4,8,3,7])
            49
            >>> Solution().maxArea([1,1])
            1
            >>> Solution().maxArea([4,3,2,1,4])
            16
        """
        left = 0
        right = len(height) - 1
        max_area = 0 
        while left < right:
            h_left, h_right = height[left], height[right]
            area = min(h_left, h_right) * ( right - left )
            max_area = max(max_area, area)
            if h_left < h_right:
                left += 1
            else:
                right -= 1
        return max_area