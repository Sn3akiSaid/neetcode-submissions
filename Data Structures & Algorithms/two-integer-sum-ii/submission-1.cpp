class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target)
    {
        // Alternative solution in C++ using hashmap
        unordered_map<int, int> mp; // mp is unordered map with int keys and int values, equiv to defaultdict(int) in Python

        for(int i = 0; numbers.size(); i++) // .size() equiv to len() in Python
        {
            int diff = target - numbers[i];
            // cout << mp.count(diff);
            if (mp.count(diff))
            { // If the complement exists in the map, return the map 
              // and index
                return {mp[diff], i + 1};
            }
            // Otherwise, store current num in map with the value being the index
            mp[numbers[i]] = i + 1;
        }
        return {}; // Return empty list if no pairs.
    }
};
