class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_set = {}
        for i, num_i in enumerate(nums):
            number_set[num_i] = i

        for i, num_i in enumerate(nums):
            # Calc the remaining number that needs to be found
            # Starting with 3 diff is 4
            difference = target - num_i
            # Check if the number is in the hashmap
            # AND if that number's index is unique 
            if difference in number_set and number_set[difference] != i:
                return [i, number_set[difference]]
        return []