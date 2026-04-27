class Solution {
public:
    bool isPalindrome(string s) {
        string new_str = "";
        int s_len = s.length();

        for (char c : s) {
            if(isalnum(c)) {
                new_str += tolower(c);
            }
        }
        return new_str == string(new_str.rbegin(), new_str.rend());
    }
};
