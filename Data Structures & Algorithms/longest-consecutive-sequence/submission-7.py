class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0

        for num in hashset:
            if num - 1 not in hashset: # Therefore num starts the sequence
                length = 1
                while num + length in hashset:
                    length += 1
                longest = max(length, longest) # Updates longest - if there is another sequence
                                               # that was found first it may be shorter than newest one
        return longest # Return longest sequence after checking every number
        