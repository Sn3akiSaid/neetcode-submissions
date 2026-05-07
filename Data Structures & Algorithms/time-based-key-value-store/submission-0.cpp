class TimeMap {
public:
    // Per key storing a map sorted by timestamp with (timestamp, value) 
    // {name : {timestamp : emotion}}
    std::unordered_map<string, std::map<int, string>> mMap;

    TimeMap() {}

    void set(string key, string value, int timestamp) {
        // Insert value as a pair
        mMap[key].insert({timestamp, value});
    }
    
    string get(string key, int timestamp) {
        // Don't scan everything, only find key with largest timestamp <= given timestamp
        // First timestamp greater than requested timestamp
        auto it = mMap[key].upper_bound(timestamp);
        // If iterator points to first timestamp greater than target
        // then all timestamps greater than requested one
        if (it == mMap[key].begin()) {
            // no value exists
            return "";
        }
        else {
            // move one step back and return that value (second from prev key,value pair)
            return prev(it)->second;
        }

        // Conditional statement can be rewritten as below using ternary operator
        // return it == m[key].begin() ? "" : prev(it)->second;
    }
};
