class MyCalendar {
private:
    struct TreeNode {
        int start, end;
        TreeNode* left;  // Pointer to node going left
        TreeNode* right; // Pointer to node going right

        TreeNode(int start, int end) : start(start), end(end), left(nullptr), right(nullptr) {}
    };

    TreeNode* root; // Root node pointer

    bool insert(TreeNode* node, int start, int end) {
    // Dereference node pointer and use its start member
    // to compare if after current end
        if (end <= node->start) {
            // Check if dereferencing leads to nullptr to the left of tree
            if (!node->left) {
                // Allocate and initialise the pointer to the current start and end times
                // Root the current node
                node->left = new TreeNode(start, end);
                return true;
            }
            // if non empty, and not overlapping, add node
            // and insert range into existing tree at that node
            return insert(node->left, start, end);
        } 
        // Other case where current start is at/after previous end 
        else if (start >= node->end) {
            // Check if it leads to nullptr to the right of tree
            if(!node->right) { 
                node->right = new TreeNode(start, end);
                return true;
            }
            return insert(node->right, start, end);
        }
        // If there is an overlap
        return false;
    }

public:
    // Construct object with member initialiser list of a null root
    MyCalendar() : root(nullptr){}
    
    bool book(int startTime, int endTime) {
        // Check if at root
        if (!root) {
            // in that case, make a new node and set it as root
            root = new TreeNode(startTime, endTime);
            return true;
        }
        // Else if we are not at the initial root, but rather a node
        // further down the tree
        // call the function with root being the root of another node.
        return insert(root, startTime, endTime);
    }
};

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(startTime,endTime);
 */