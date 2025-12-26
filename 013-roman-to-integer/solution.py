class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Given a roman numeral, convert it to an integer.
        
        Args:
            s: A string representing a roman numeral
            
        Returns:
            Integer value of the roman numeral
        """

        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
        for digit in reversed(s):
            current_value = roman_numerals[digit]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        return total