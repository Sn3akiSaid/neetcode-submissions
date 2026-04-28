class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;
        int newStart = newInterval[0];
        int newEnd = newInterval[1];

        for (int i = 0; i < intervals.size(); i++) {
            if ( newEnd < intervals[i][0] ) { // newInterval ends before current interval starts
                res.push_back(newInterval); // Adds newInterval to result list
                copy(intervals.begin() + i, intervals.end(), back_inserter(res)); // Copies remaining intervals and appends them in res by sending the intervals to push_back
                // back_inserter pushes intervals to the back of the list in this case, creating additional space without overwriting
                return res;
            }
            else if ( newStart > intervals[i][1] ) {
                // newInterval starts after current interval
                res.push_back(intervals[i]); // Add current interval
            }
            else {
                // Overlaps with current interval
                newInterval[0] = min(newInterval[0], intervals[i][0]); // Take smallest of the starting points and reassign the startpoint
                newInterval[1] = max(newInterval[1], intervals[i][1]); // Take biggest of the ending points and reassign the endpoint
            }
        }
        res.push_back(newInterval); // Add the newInterval 
        return res;
    }
};
