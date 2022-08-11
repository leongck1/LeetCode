# Approach 1: Brute Force Method
# Time Complexity = O(n) where a for loop to loop through n data
# Space Complexity = O(n) where data is stored in hash table
# LeetCode runtime = 118ms and memory usage = 15.2 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited_values = dict()
        for index, value in enumerate(nums):
            if target - value in visited_values:
                return [visited_values[target - value], index]
            else:
                visited_values[value] = index
        return []
                
# Approach 2: Hash Table Method
# Time Complexity = O(n^2) where two for loop to loop through n data
# Space Complexity = O(1) where no data is stored
# LeetCode runtime = 6262ms and memory usage = 14.9 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:             
        for index in range(len(nums)):
            for index_2 in range(index + 1, len(nums)):
                if nums[index] + nums[index_2] == target:
                    return [index, index_2]
        return []
       
# Approach 3: Sorting Method
# Time Complexity = O(nlog(n)) where standard python sorted() function will have runtime of nlog(n)
# Space Complexity = O(n) where sorted data is stored is a list of tuples
# LeetCode runtime = 143ms and memory usage = 15.4 MB
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(enumerate(nums), key=lambda x: x[1])  # LeetCode wants the original index and not the sorted index
        first_index = 0
        last_index = len(nums) - 1
        while first_index <= last_index:
            if nums[first_index][1] + nums[last_index][1] == target:
                return [nums[first_index][0], nums[last_index][0]]
            elif nums[first_index][1] + nums[last_index][1] > target:
                last_index -= 1
            else:
                first_index += 1
        return []
