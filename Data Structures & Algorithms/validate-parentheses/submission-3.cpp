class Solution {
public:
    bool isValid(string s) {
        std::stack<char> stackOfChars;
        std::unordered_map<char, char> closeToOpen =  {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        for (char c : s) {
            if (closeToOpen.count(c)) { // Count if instance of c in unordered_map (check if in)
                // not empty AND top of stack (LIFO - so final element) is value of c key
                if (!stackOfChars.empty() && stackOfChars.top() == closeToOpen[c]) {
                    stackOfChars.pop(); // Remove from stack
                }
                else { 
                    return false;
                }
            }
            else {
                stackOfChars.push(c); // Insert in stack if not inside already
            }
        }
    return stackOfChars.empty(); // Returns false if anything still in stack
    }
};
