from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Min and max speeds
        # Somewhat initializing an array k = [1,...,max(p)]
        l, r = 1, max(piles)
        res = r
        # Binary search of the k value reduces complexity to
        # O(log(p)*p)
        while l <= r:
            
            k = (l + r) // 2

            totalHours = 0
            for pile in piles:
                # check how many hours it takes
                # per pile at current speed k
                totalHours += ceil(float(pile) / k)
            # less than max allowed
            if totalHours <= h:
                # Set result to that speed
                res = k
                # and move pointer to mid of list
                # because we might have another minimum that is valid res
                r = k - 1
            # The time taken is greater
            else:
                # so increase the minimum rate to after mid of list
                l = k + 1
        return res