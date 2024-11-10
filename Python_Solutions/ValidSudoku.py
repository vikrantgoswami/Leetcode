class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for i in range(9)]
        cols = [[] for i in range(9)]
        squares = [[] for i in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3*3 + c//3)]):
                    return False
                rows[r].append(board[r][c])
                cols[c].append(board[r][c])
                squares[((r//3 *3)+c//3)].append(board[r][c])

        return True
