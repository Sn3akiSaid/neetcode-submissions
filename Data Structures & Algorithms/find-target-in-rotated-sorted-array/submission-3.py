class Solution:
    
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r: #until l = r
            mid = l + (r - l) // 2
            
            # number in middle is greater than final number
            # so the list has been cycled and the pivot is in the right half
            if nums[mid] > nums[r]:
                # set the left pointer after the middle
                l = mid + 1
            
            # number in middle is less than or equal to final number
            # so pivot is in the left half
            else:
                r = mid
        # set the pivot to l - this is the minimum of the list
        pivot = l

        def binary(l: int, r: int) -> int:
        
            while l <= r:
                mid = l + (r - l) // 2
                # Check if the middle is the target
                if nums[mid] == target:
                    return mid
                # if target is after the middle
                elif nums[mid] < target:
                    # halve list from the left
                    l = mid + 1
                # only other case is target is before middle
                else:
                    # halve list from the right
                    r = mid - 1
            return -1

        # Check first list [ 0 : pivot - 1 ]
        res = binary(0, pivot - 1)
        # If the index was found, return it
        if res != -1:
            return res
        # Otherwise check the second list [pivot : len(nums) - 1]
        return binary(pivot, len(nums) - 1)

        
        
    