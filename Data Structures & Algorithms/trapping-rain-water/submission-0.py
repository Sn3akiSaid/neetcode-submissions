class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        area = 0
        
        while l < r:
            if leftMax < rightMax:
                # move the left pointer
                l += 1
                # compare maxima
                leftMax = max(height[l], leftMax) 
                # find the height diff between maxima and current height
                area += leftMax - height[l] 
            else:
                # move the right pointer left
                r -= 1
                # compare maxima 
                rightMax = max(height[r], rightMax)
                # find height diff between maxima and current height
                area += rightMax - height[r]
        return area