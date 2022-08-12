# Approach 1: String Method
# Time Complexity = O(n) where a while loop to loop through n / 2 data
# Space Complexity = O(1) where only left_index and right_index are stored regardless of the length of input
# LeetCode runtime = 88 ms and memory usage = 13.9 MB
class Solution:
    def isPalindrome(self, x: int) -> bool:
        left_index = 0
        right_index = len(str(x)) - 1
        while left_index < right_index:
            if str(x)[left_index] == str(x)[right_index]:
                left_index += 1
                right_index -= 1
            else:
                return False
        return True
