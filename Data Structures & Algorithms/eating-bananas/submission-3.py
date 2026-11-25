class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        # k = [1, 2,..., 11]
        res = 0
        # l <= r ensures l can take on the same max value as r's min possible value
        # l < r forbids l and r to be the same value, terminating the loop early
        while l <= r:
            print("l:",l, "r:",r)
            k = (l + r) // 2
            print("k",k)
            # start with the median of the piles as our speed
            # now go through the piles themselves

            # start from 0 every time we try a new speed
            totalHr = 0
            for pile in piles:
                # add to the time the time it takes to eat the current pile
                totalHr += math.ceil(pile / k)
            # If the total time hasn't exceeded the max time h
            print("totalhr:", totalHr)
            if totalHr <= h:
                # make the result = to that speed k
                res = k
                # and look for a smaller speed
                r = k - 1
                print("r",r)
            # Else we have exceeded the max time allowed and must instantly
            # discard all possible speeds to the left of middle
            else:
                l = k + 1
                print("l",l)
        return res