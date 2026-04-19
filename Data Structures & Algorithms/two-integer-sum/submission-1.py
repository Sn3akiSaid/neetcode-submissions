class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_set = {}

        for i, num_i in enumerate(nums):
            difference = target - num_i

            # Does difference exist in hashmap
            if difference in number_set:
                # If yes, return current index and other one
                # Order changes, as here our first index is the difference
                # Hashmap contains only previous indices {3: 0}
                # Second run of loop lands on 4 which means diff = 3
                # This exists already at index number_set[difference]
                return [number_set[difference], i]
            number_set[num_i] = i
        return []