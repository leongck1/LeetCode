# Approach 1: Brute Force Method
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
                
# Approach 2: Hash Table Method
# Time Complexity = O(n^2) where two for loop to loop through n data
# Space Complexity = O(1) where no data is stored           
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:             
        for index in range(len(nums)):
            for index_2 in range(index + 1, len(nums)):
                if nums[index] + nums[index_2] == target:
                    return [index, index_2]
