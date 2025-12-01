class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without repeating characters.
        
        Args:
            s: Input string
            
        Returns:
            Length of the longest substring without repeating characters
        """
        left = 0 
        seen = {} 
        max_len = 0 
        for r in range(0, len(s)): 
            current = s[r] 
            if current in seen and seen[current] >= left: 
                left = seen[current] + 1 
            seen[current] = r 
            max_len = max(max_len, r - left + 1) 
        return max_len

    def SubOptimalLengthOfLongestSubstring(self, s: str) -> int:
        """
        Simpler approach using string slicing. Less efficient due to string operations.
        I like this as shows the windowing concept clearly.
        """

        window = ""
        max_len = 0
        
        for char in s:
            if char in window:
                # Find the duplicate's index inside the current window
                # and slice off everything up to and including it.
                # Example: window="abc", char="b" -> new window="c"
                window = window[window.index(char) + 1:]
            
            window += char
            max_len = max(max_len, len(window))
            
        return max_len
    