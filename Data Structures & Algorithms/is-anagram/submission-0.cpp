class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }

        // Basic sort from start to end of each string
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        // Bool return checking if s equivalent to t
        return s==t;
        // unordered_set<string> characters_s;
        // unordered_set<string> characters_t;
        // for (string chs : s){
        //     characters_s.insert(chs);
        // }
        // for (string cht : t){
        //     characters_t.insert(cht);
        // }
        // if (characters_s == characters_t){
        //     return true;
        // }
        // return false;
    }
};
