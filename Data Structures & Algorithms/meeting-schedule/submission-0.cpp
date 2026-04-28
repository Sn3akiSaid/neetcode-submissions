/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        // Sort with anonymous lambda O(nlogn)
        // Removes need for separate comparison function
        // auto& assigns types of x and y as the Interval object by reference
        // & alias of object, not copy
        sort(intervals.begin(), intervals.end(), [](const auto& x, const auto& y) {
            return x.start < y.start; // Sorts by interval start values of each Interval object
        });

        // Loop through intervals O(n)
        for (int i = 1; i < intervals.size(); i++ ) {
            // If the end of the previous interval is greater than start of current
            if ( intervals[i - 1].end > intervals[i].start ) {
                // Then those overlap, therefore false
                return false;
            }
        }
        return true;
    }
};
