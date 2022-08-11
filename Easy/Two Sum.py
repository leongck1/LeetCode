# Approach 1
# Time Complexity = O(n) where a for loop to loop through n data
# Space Complexity = O(n) where values are stores in hash table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_values = dict()
        for index, value in enumerate(nums):
            if target - value in visited_values:
                return [visited_values[target - value], index]
            else:
                visited_values[value] = index
