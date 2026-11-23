class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        def findArea(l, r, h1, h2):
            return (r - l) * min(h1, h2)

        while l < r:
            area = findArea(l, r, heights[l], heights[r])
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else: # height at l > height at r
                r -= 1
        return res