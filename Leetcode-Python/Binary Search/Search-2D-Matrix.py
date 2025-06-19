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
            # Why cols in both cases? To get to the next row we have to go through a cetain
            # number of columsn right? So we just divide by number of columns and floor to 
            # get row. As for columns it will just be the remainder that we didnt take with
            # row.
            row = m // cols # This gives us how many full rows we've passed — i.e., which
            # row we are in.
            col = m % cols

            if matrix[row][col] < target:
                l = m + 1

            if matrix[row][col] > target:
                r = m - 1
            
            if matrix[row][col] == target:
                return True
        return False