class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # j = 0
        
        # k = left + 1
        res = []
        nums.sort()
        # print(sorted_nums)

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                threeSum = val + nums[j] + nums[k]
                curSum = nums[j] + nums[k]
                if curSum > target:
                    k -= 1
                elif curSum < target:
                    j += 1
                else:
                    res.append([val, nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res