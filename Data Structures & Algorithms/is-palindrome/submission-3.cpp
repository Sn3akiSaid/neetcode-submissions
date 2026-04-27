class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size();
        while (l < r){
            while(l < r and not isalnum(s[l])){
                l++;
            }
            while(r > l and not isalnum(s[r])){
                r--;
            }
            if (tolower(s[l]) != tolower(s[r])){
                return false;
            }
            l++;
            r--;
        }
        return true;
    }
};
