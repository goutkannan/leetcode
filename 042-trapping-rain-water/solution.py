class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Given n non-negative integers representing an elevation map where 
        the width of each bar is 1, compute how much water it can trap after raining.
        
        Args:
            height: List of non-negative integers representing elevation map
            
        Returns:
            int: Total amount of water that can be trapped
            
        Examples:
            >>> Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
            6
            >>> Solution().trap([4,2,0,3,2,5])
            9
            >>> Solution().trap([4,2,3])
            1
        """
        lmax = 0
        rmax = 0
        lptr = 0
        rptr = len(height) - 1
        result = 0
        while(lptr <= rptr):
            if(lmax < rmax):
                if(height[lptr] < lmax):
                    result += (lmax - height[lptr])
                else:
                    lmax = height[lptr]
                lptr += 1
            else:
                if(height[rptr] < rmax):
                    result += (rmax - height[rptr])
                else:
                    rmax = height[rptr]
                rptr -= 1
        return result


if __name__ == "__main__":
    solution = Solution()
    
    # Test case
    test_input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    result = solution.trap(test_input)
    
    print(f"Input: {test_input}")
    print(f"Output: {result}")
    print(f"Expected: 6")
