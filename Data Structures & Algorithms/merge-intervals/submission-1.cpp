class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        // First submission
        vector<vector<int>> res;
        
        sort(intervals.begin(), intervals.end(), [](auto& x, auto& y){
            return x[0] < y[0];
            // Don't need lambda here
        });

        res.push_back(intervals[0]);

        // Start from first element
        for (auto& interval : intervals) {

            int lastEnd = res.back()[1]; // .back() returns ref to last interval in res
            // [1] picks the 2nd element of that interval vector

            if (interval[0] <= lastEnd) { 
            // if current start same or before last end -> overlap
            // update that end value with the latest of the current and previous end times
                res.back()[1] = max(lastEnd, interval[1]);
            }
            else {
            // If the current start point is after last end point
            // Add the current interval
                res.push_back(interval);
            }
        }
        return res;
    }
};
