class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        def findArea(l, r, h1, h2):
            return (r - l) * min(h1, h2)
        while l < r:
            
            area = max(area, findArea(l, r, heights[l], heights[r]))

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return area