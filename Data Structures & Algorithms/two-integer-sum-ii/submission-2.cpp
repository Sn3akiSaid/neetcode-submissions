class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        // Alt solution using two pointers
        int left = 0;
        int right = numbers.size() - 1;

        while(left < right)
        {
            int curSum = numbers[left] + numbers[right];

            if (curSum > target)
            { // Move right pointer left if sum is too large
                right--;
            }
            else if (curSum < target)
            { // Move right pointer left if sum is too large
              // else if here makes sure left pointer only moves once nums from right are eliminated
                left++;
            }
            else
            { // curSum == target
                return {left + 1, right + 1};
            }
        }
        return {};
    }
};
