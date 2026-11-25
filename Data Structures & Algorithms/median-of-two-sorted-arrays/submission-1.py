class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

    # LMAO tried some stupid sorting algorithm, forgot theres .sort()
        # if not nums1 or not nums2:
        #     return 0
        # sortedlist = []

        # while nums1 or nums2:
        #     if (nums1 and nums2) and (nums1[0] < nums2[0]):
        #         print("nums1", nums1, "sortedlist", sortedlist)
        #         sortedlist.append(nums1.pop(0))
        #     # elif (nums1 and nums2) and (nums2[0] < nums1[0]):
        #     #     print(sortedlist, nums2)
        #     #     sortedlist.append(nums2.pop(0))
        #     else:
        #         print("nums2", nums2, "sortedlist", sortedlist)
        #         sortedlist.append(nums2.pop(0))

        # 
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
            