class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        std::unordered_map<char, int> hash;
        int l = 0, res = 0;

        for (int r = 0; r < s.size(); r++) {
            // If that character is not found
            if (hash.find(s[r]) != hash.end()) {
                l = max(hash[s[r]] + 1, l);
            }
            // Save current char in map with position as val
            hash[s[r]] = r;
            res = max(res, r - l + 1);
        } 
        return res;
    }
};
