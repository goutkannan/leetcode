import time
import random
import string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Optimized O(N) approach using a dictionary (hash map).
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
        Simpler O(N^2) approach using string slicing.
        """
        window = ""
        max_len = 0
        
        for char in s:
            if char in window:
                window = window[window.index(char) + 1:]
            
            window += char
            max_len = max(max_len, len(window))
            
        return max_len

def run_benchmark():
    solution = Solution()
    
    print("Running benchmarks...")
    print("=" * 70)

    # Case 1: Random ASCII String (Small Window)
    # Window size is limited by ASCII set (~95 chars)
    length = 50000
    print(f"Case 1: Random ASCII string (len={length})")
    print("  - Window size stays small (limited by alphabet size)")
    large_string = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    
    start_time = time.time()
    solution.lengthOfLongestSubstring(large_string)
    time_opt = time.time() - start_time
    
    start_time = time.time()
    solution.SubOptimalLengthOfLongestSubstring(large_string)
    time_sub = time.time() - start_time
    
    print(f"  - Optimized (Dict): {time_opt:.6f}s")
    print(f"  - SubOptimal (Str): {time_sub:.6f}s")
    print(f"  - Speedup: {time_sub / time_opt:.2f}x")
    print("-" * 70)

    # Case 2: Unique Characters (Large Window)
    # Window grows linearly with input size. This exposes O(N^2) behavior.
    # We use a smaller length because O(N^2) will be very slow.
    length_unique = 20000
    print(f"Case 2: String with all unique characters (len={length_unique})")
    print("  - Window grows to full length of string")
    # Using unicode characters to ensure uniqueness
    unique_string = "".join(chr(i) for i in range(length_unique))
    
    start_time = time.time()
    solution.lengthOfLongestSubstring(unique_string)
    time_opt_unique = time.time() - start_time
    
    start_time = time.time()
    solution.SubOptimalLengthOfLongestSubstring(unique_string)
    time_sub_unique = time.time() - start_time
    
    print(f"  - Optimized (Dict): {time_opt_unique:.6f}s")
    print(f"  - SubOptimal (Str): {time_sub_unique:.6f}s")
    print(f"  - Speedup: {time_sub_unique / time_opt_unique:.2f}x")
    print("=" * 70)

if __name__ == "__main__":
    run_benchmark()
