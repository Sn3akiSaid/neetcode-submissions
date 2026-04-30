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
    int minMeetingRooms(vector<Interval>& intervals) {
        vector<pair<int, int>> time; // time is a vector of pairs (time, end events) <=> (first, second)

        // So time.first = time and time.second = end events

        for (const auto& interval : intervals) {
            time.push_back({interval.start, 1}); // Push back a pair of {start time, add one room}
            time.push_back({interval.end, -1}); // Push back a pair of {end time, remove one room}
        }

        sort(time.begin(), time.end(), [](auto& a, auto& b) { // a and b here inferred as time's type pair<int, int>
            // If two consecutive intervals start at same time
            // Then sort with by the number of end events -1 < +1
            // Otherwise sort by start times ascending
            return a.first == b.first ? a.second < b.second : a.first < b.first;
        });
    
        int res = 0, count = 0;
        for (const auto& t : time) {
            count += t.second; // Count the start/end events
            res = max(res, count); // max function here finds the first time we encounter a max num of rooms
            // and keeps it until a new maximum or no new maximum is found
        }
        return res;
    }
};
