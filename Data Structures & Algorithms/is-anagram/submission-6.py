class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashset_s, hashset_t = {}, {}
        
        for i in range(len(s)):
            # Make each char the key
            # Increment each value of key to by + 1
            hashset_s[s[i]] = hashset_s.get(s[i], 0) + 1 # if key not exist yet use 0
            hashset_t[t[i]] = hashset_t.get(t[i], 0) + 1
        return hashset_t == hashset_s