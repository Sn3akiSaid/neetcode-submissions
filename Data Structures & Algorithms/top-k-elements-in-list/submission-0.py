class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashset = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashset[num] = hashset.get(num, 0) + 1

        for num, cnt in hashset.items():
            # At index cnt append corresponding value num
            # num occurs cnt number of times
            freq[cnt].append(num)

        res = []
        
        for i in range(len(freq) - 1, 0, -1):
            # Start from highest to lowest frequency
            for num in freq[i]:
                # Go through every frequency index
                # Add the corresponding value num to res
                res.append(num)
                # Check that the length matches the number k
                if len(res) == k:
                    return res
        