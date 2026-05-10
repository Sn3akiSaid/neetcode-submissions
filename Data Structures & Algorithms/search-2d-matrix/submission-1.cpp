class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int ROWS = matrix.size(); // Number of rows
        int COLUMNS = matrix[0].size(); // Number of columns

        int top = 0, bot = ROWS - 1; // top and bottom

        // Look for row containing target
        while ( top <= bot) {
            // Middle row in matrix
            int row = (top + bot) / 2;
            // target greater than last element of middle row
            if (target > matrix[row][COLUMNS - 1]) {
                // Discard bottom rows by shifting top to middle
                top = row + 1;
            }
            // target smaller than smallest val in current row
            else if (target < matrix[row][0]) {
                // Discard top rows by shifting bot to middle
                bot = row - 1;
            }
            // Target found - break out of loop
            else break;
        }
        // If we didn't break out of loop without finding the target value in any row
        if (!( top <= bot )) return false;
        // If above is not the case
        // run search on current row
        int row = ( top + bot ) / 2;
        int l = 0, r = COLUMNS - 1;

        while (l <= r) {
            int mid = ( l + r ) / 2;
            if (target > matrix[row][mid]) {
                // Remove vals left of middle
                l = mid + 1;
            }
            else if (target < matrix[row][mid]) {
                // Remove vals right of middle
                r = mid - 1;
            }
            else return true;
        }
        return false;
    }
};
