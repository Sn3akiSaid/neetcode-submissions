class KthLargest {
    int k;
    vector<int>& nums;
    // Min Heap, smallest on top
    priority_queue<int, vector<int>, greater<int>> numsQu;
public:
    KthLargest(int k, vector<int>& nums) : k(k), nums(nums) {
        for (int num : nums) {
                numsQu.push(num);
                // Maintain the heap the size of k
                // As it is min-heap and size k, the top of it
                // will always be the smallest of the three biggets
                // i.e. k-th largest value
                if (numsQu.size() > k) numsQu.pop();
            }
    }

    int add(int val) {
        numsQu.push(val);
        // If size bigger than k, remove smallest num
        if (numsQu.size() > k) numsQu.pop();
        return numsQu.top();
    }

    

};
