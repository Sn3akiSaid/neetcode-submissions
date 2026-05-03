class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        // If divisible by groupSize instant false
        if (hand.size() % groupSize != 0) return false;

        // This problem can be done with map or unordered_map
        std::unordered_map<int, int> seenNums;
        for (int num : hand) seenNums[num]++; 
        
        sort(hand.begin(), hand.end());

        for (int num : hand) cout << num;

        // Iterate through the numbers themselves, not element index
        for (int num : hand) {
            // If current number is in map
            if (seenNums[num] > 0) {
                // iterate from current num up to groupSize away from it
                // example: num = 1, groupSize = 4 -> go through 1,2,3,4
                for (int i = num; i < num + groupSize; i++) {
                    // If the current number is not present 
                    if (seenNums[i] == 0) return false; // Can't build group
                    // if still in map decrease its appearance value
                    seenNums[i]--;
                }
            } // after a couple runs this will eventually exhaust
              // the presence of the remaining numbers from the map 
        }
        // Once all numbers have been exhausted and the groupSize has been reached
        return true;
    }
};
