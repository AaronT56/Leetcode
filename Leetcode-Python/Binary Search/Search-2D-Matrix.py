class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l = 0
        r = len(matrix[0]) * len(matrix) - 1

        # get middle row, middle element
        while l <= r:
            # Think of these as getting the number of rows passed
            # and how far into the row you are. If you have passed one row
            # Then flooring will give the index of the row you are on. 
            # If you divide and take remainder you will have how far you are into the
            # row. So you can treat this like a flat array
            m = l + ((r-l) // 2)
            row = m // cols
            col = m % cols

            if matrix[row][col] < target:
                l = m + 1

            if matrix[row][col] > target:
                r = m - 1
            
            if matrix[row][col] == target:
                return True
        return False