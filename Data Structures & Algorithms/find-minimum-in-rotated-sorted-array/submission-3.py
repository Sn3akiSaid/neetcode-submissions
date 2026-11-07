class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = 0
        last = len(nums) - 1 # Index

        while first < last:
            mid = (first+last)//2
            if nums[mid] > nums[last]:
                first = mid + 1
            else: # can just reduce the two branches into one
                last = mid
        mid = (first+last)//2
        return nums[mid]