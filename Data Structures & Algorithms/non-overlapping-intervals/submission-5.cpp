class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {

        vector<vector<int>> res;

        sort(intervals.begin(), intervals.end());

        res.push_back(intervals[0]);

        for (auto& interval : intervals) {
            // DEBUG:
            // cout << "(" <<interval[0] << ", " << interval[1] << ")";
            
            int lastEnd = res.back()[1];
            int currStart = interval[0];
            int currEnd = interval[1];

            if ( currStart >= lastEnd ) { // Check if not overlapping
                res.push_back(interval); // Add interval to new array
            } 
            else if (currEnd <= lastEnd) {
                // Check if another element has an end time that is before the previous endtime
                // This way we find an earlier (smaller) end time
                // Less chance of overlap with a following interval
                // Minimize # of intervals that need to be deleted 
                res.back() = interval;
            }
        }

        // DEBUG:
        // for (auto& i : res) {
        //     cout << "(" <<i[0] << ", " << i[1] << ")";
        // }

        // Find diff between original array and non-overlapping array
        int minRemoval = intervals.size() - res.size();
        return minRemoval;
    }
};
