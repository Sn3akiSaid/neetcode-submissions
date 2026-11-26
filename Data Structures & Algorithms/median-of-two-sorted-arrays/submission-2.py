class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Clean BRUTE FORCE solution
        # O(n*m) because of the additional sorting
        merged = nums1 + nums2
        sortedlist = sorted(merged)

        # or similarly 
        # merged = nums1 + nums2
        # merged.sort()

        l, r = 0, len(sortedlist) - 1
        print("len",r + 1)
        median = (l + r) // 2
        if (r + 1) % 2 == True:
            
            print("median", median)
            return sortedlist[median]
        else:
            evenmedian = (sortedlist[median] + sortedlist[median + 1]) / 2
            return evenmedian