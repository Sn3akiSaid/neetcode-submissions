class Solution {
public:
    bool isAnagram(string s, string t) {
        // Obv check for length, cant be anagram if not equal length
        if (s.length() != t.length()){
            return false;
        }

        // // Basic sort from start to end of each string
        // sort(s.begin(), s.end());
        // sort(t.begin(), t.end());
        // // Bool return checking if s equivalent to t
        // return s==t;

        unordered_map<char, int> charactersS;
        unordered_map<char, int> charactersT;
        for (int i=0; i < s.length(); i++){
            // start from 0 to end of length of s, iterate by 1
            charactersS[s[i]]++; // increment s[i] char count in hash map
            charactersT[t[i]]++; //
        }
        return charactersS == charactersT;
    }
};

