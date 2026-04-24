class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        while i < len(numbers):
            diff = target - numbers[i]
            
            if diff in numbers and i < numbers.index(diff):
                return [i + 1, numbers.index(diff) + 1]
            i += 1