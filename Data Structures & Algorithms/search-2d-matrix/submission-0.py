class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top = 0
        bot = ROWS-1


        while top <= bot :
            row = (top+bot)//2
            if target > matrix[row][-1]:
                top = row + 1
            
            elif target < matrix[row][0]:
                bot = row - 1
            
            else:
                break
        
        if not(top<= bot):
            return False

        #search the row [horizontal]

        left = 0
        right = COLS - 1

        while left <= right:
            cols = left + (right-left)//2
            if target == matrix[row][cols]:
                return True
            elif target > matrix[row][cols]:
                left = cols + 1
            
            else:
                right = cols - 1
        


        return False