class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size();

        // Go through sorted list by moving pointers 
        while (l < r) {
            // Set middle after every pointer move
            int m = l + (r - l) / 2;
            // Number in middle is bigger than targeted number
            if (nums[m] > target) {
                // Scrap right side by setting right pointer to m
                r = m;
            } else { // Number in middle is smaller than target
                // Scrap left side by moving left pointer to middle + 1
                l = m + 1;
            }
        }
        // if the left pointer has moved and the number is the target
        // return the previous number index l - 1, otherwise return -1
        return (l > 0 && nums[l - 1] == target) ? l - 1 : -1;
    }
};