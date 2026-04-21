class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix # set res[i] to prefix

            prefix *= nums[i] # Multiply prefix by current number from nums
        # This will return res = [1, 1*nums[0], 1*nums[0]*nums[1], 1*nums[0]*nums[1]*nums[2], ...]

        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            # Go backwards in array
            res[i] *= suffix # Multiply prefix by the current postfix starting at 1 

            suffix *= nums[i] # Make the suffix for the next run a product of prev suffix * current num
        
        return res
        # return res = [1*nums[last], 1*nums[0]*nums[second_last], ...]