class MyCalendar {
private:
    // vector of pairs
    std::vector<std::pair<int,int>> events;

public:
    MyCalendar() {
        cout << "constructed";
    }

    bool book(int startTime, int endTime) {
        for (const auto& event : events) {
            if (startTime < event.second && endTime > event.first) {
                // If current startTime is before event end and end time is after event start
                // - in other words, this is not an event that starts before and ends before current event
                // then it overlaps and return false
                return false;
            }
        }
        // if event is outside of any event interval just add it 
        events.push_back({startTime, endTime});
        return true;
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(startTime,endTime);
 */