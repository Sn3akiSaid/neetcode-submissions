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

        if(intervals.empty()) return 0; // Empty so 0 rooms

        // Sort based on starting times using lambda
        sort(intervals.begin(), intervals.end(), [](auto& x, auto& y) {
            return x.start < y.start;
        });
        // int- stored elements, vector<int> - underlying container of ints, greater<int> - comparator (small values first)
        priority_queue<int, vector<int>, greater<int>> minHeap;

        for (const auto& interval : intervals) {
            if (!minHeap.empty() && minHeap.top() <= interval.start) { // Not empty AND top of heap (earliest end time) is before or at cur interval start
                minHeap.pop(); // Remove that time from top of heap (reuse room)
            }
            // Empty heap or top of heap is within current interval
            minHeap.push(interval.end); // Add the end of current interval
        }
        return minHeap.size(); // minHeap is overlapping end times, so return amount of times this happens
    }
};