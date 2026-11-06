class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        rows = len(matrix) # 3 rows

        top = 0
        bottom = rows - 1 # set index to 2
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bottom = row - 1
            else:
                #else target found
                break

        # case where top and bottom pointers are invalid
        # crossed out all rows and none contained target
        if not (top <= bottom):
            return False

        # Take the new top and bottom to find the middle row
        row = (top + bottom) // 2
        left = 0
        right = cols - 1

        while left <= right:
            mid_of_row = (left + right) // 2
            if matrix[row][mid_of_row] < target:
                left = mid_of_row + 1
            elif matrix[row][mid_of_row] > target:
                right = mid_of_row - 1
            else:
                return True
        return False

