class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxHeap;

        for (auto& stone : stones) {
            maxHeap.push(stone);
        }

        while ( maxHeap.size() > 1 )  {
            int stone1 = maxHeap.top();
            maxHeap.pop();
            int stone2 = maxHeap.top();
            maxHeap.pop();
            
            if (stone2 < stone1) {
                maxHeap.push(stone1 - stone2);
            } // Else stone1 == stone2 -> do nothing else.
        }
        // Push 0, will sink to bottom of heap if other weight present
        maxHeap.push(0);
        // Returns top element, weight of remaining stone or 0
        return maxHeap.top();
    }
};
