class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            # Check that previous values repeat
            if i > 0 and val == nums[i - 1]:
                continue # End if repeated number

            j = i + 1 # Start to the right of i
            k = len(nums) - 1 # Start at end of list
            target = -nums[i] 
            while j < k: # Making sure left and right pointers don't cross over
                curSum = nums[j] + nums[k] 
                if curSum > target: # Too big
                    k -= 1 # Reduce biggest pointer (move right pointer right)
                elif curSum < target: # Too small
                    j += 1 # Increase smallest pointer (move left pointer right)
                else: # a + b + c = 0
                    res.append([val, nums[j], nums[k]]) 
                    j += 1 # Move left pointer to the right, to avoid repetition
                    while nums[j] == nums[j - 1] and j < k: # While left pointer keeps repeating and is not at k
                        j += 1 # Keep shifting left pointer
                        # Don't need to also shift k to check for duplicates,
                        # because that will go back to the if statement that shifts it left
                        # if it is still the same, then it's still too big and will shift left again
        return res