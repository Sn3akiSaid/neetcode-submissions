class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0
        while k < (len(nums)):

            if nums[k] == val:
                nums.pop(k) # Removes that element and shortens list
                # [1, 1, 2, 3, 4] -> [1, 2, 3, 4]
                k -= 1
            k += 1

        return k