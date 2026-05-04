class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::map<int, int> hashMap; // key is the list element, val is the index

        for (int i = 0 ; i < nums.size(); i++) {
            int diff = target - nums[i];
            // .find() uses key_type
            if (hashMap.find(diff) != hashMap.end()) {
                return {hashMap[diff], i};
            }
            // Use .insert() method to add k,v pairs
            hashMap.insert({nums[i], i});
        }
        // No pairs
        return {};
    }
};
