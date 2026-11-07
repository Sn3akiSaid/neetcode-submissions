class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = 0
        last = len(nums) - 1 #
        cycle = nums[last] - nums[first]

        while first < last:
            mid = (first+last)//2
            if nums[mid] > nums[last]:
                first = mid + 1
            elif nums[mid] < nums[first]:
                last = mid
            # or first < mid < last
            else:
                last = first
        mid = (first+last)//2
        return nums[mid]