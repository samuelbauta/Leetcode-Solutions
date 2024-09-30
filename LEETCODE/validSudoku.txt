# June 16 941am Fathers Day
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) # hashset for cols
        rows = collections.defaultdict(set) # hashset for rows
        squares = collections.defaultdict(set) # hashset for squares

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # check for blanks edge case
                    continue
                if (board[r][c] in rows[r] or # check for duplicates across every row
                    board[r][c] in cols[c] or # check for duplicates down every column
                    board[r][c] in squares[(r // 3, c // 3)]): # check for duplicates in each 3x3 square
                    return False
                cols[c].add(board[r][c]) # if you made it this far then add the value to every corresponding
                rows[r].add(board[r][c]) # row and column and 3x3 square
                squares[(r // 3, c // 3)].add(board[r][c])

        return True # if you made it without any duplicates then return true


                
