class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Indices
        first = 0
        last = len(nums) - 1

        while first <= last:
            #mid = (first + last) // 2
            # Safe version that prevents overflow, adds the difference required to get to the middle instead of adding both numbers directly
            mid = first + (last - first) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                first = mid + 1
            else:
                last = mid - 1
        return -1