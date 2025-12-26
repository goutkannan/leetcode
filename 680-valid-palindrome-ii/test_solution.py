import pytest
from solution import Solution

    
class TestValidPalindromeII:
    def setup_method(self):
        self.solution = Solution()
    
    # Basic test cases from problem
    def test_example1(self):
        assert self.solution.validPalindrome("aba") == True
    
    def test_example2(self):
        assert self.solution.validPalindrome("abca") == True
    
    def test_example3(self):
        assert self.solution.validPalindrome("abc") == False
    
    # Edge cases
    def test_single_character(self):
        assert self.solution.validPalindrome("a") == True
    
    def test_two_same_characters(self):
        assert self.solution.validPalindrome("aa") == True
    
    def test_two_different_characters(self):
        assert self.solution.validPalindrome("ab") == True
    
    def test_already_palindrome(self):
        assert self.solution.validPalindrome("racecar") == True
    
    # More complex cases
    def test_delete_from_middle(self):
        assert self.solution.validPalindrome("raceacar") == True
    
    def test_delete_from_start(self):
        assert self.solution.validPalindrome("xracecar") == True
    
    def test_delete_from_end(self):
        assert self.solution.validPalindrome("racecarx") == True
    
    def test_need_two_deletions(self):
        # Would need to delete both 'd' and 'e' to make palindrome
        assert self.solution.validPalindrome("abcdefgfedcba") == True
        assert self.solution.validPalindrome("abcxyzba") == False
    
    def test_long_palindrome_with_one_error(self):
        assert self.solution.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga") == True
    
    def test_symmetric_mismatch(self):
        # Both ends have mismatches
        assert self.solution.validPalindrome("abcdedcxa") == False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
