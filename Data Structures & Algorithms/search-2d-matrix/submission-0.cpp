class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        // First brute force try
        int x, y;
        for (const auto& row : matrix ) {
            for (const auto& column : row) {
                if (column == target) return true;
            }
        }
        return false;
    }
};
