# Approach 1
# Time Complexity = O(m + n) where two for loop to loop through n data
# Space Complexity = O(n) where string s is stored
# LeetCode runtime = 100 ms and memory usage = 13.9 MB
class Solution:
    def romanToInt(self, s: str) -> int:
        single_roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        double_roman = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        
        
        result = 0
        
        for roman, number in double_roman.items():
            if roman in s:
                result += number
                s = s.replace(roman, "")
                
        for roman in s:
            result += single_roman[roman]
            
        return result

# Approach 2


    
