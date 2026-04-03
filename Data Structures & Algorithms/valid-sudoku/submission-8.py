class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        val_to_col = defaultdict(set)
        val_to_row = defaultdict(set)
        val_to_square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in val_to_col[c] or
                    board[r][c] in val_to_row[r] or
                    board[r][c] in val_to_square[(r//3, c//3)]):
                    return False
                
                val_to_col[c].add(board[r][c])
                val_to_row[r].add(board[r][c])
                val_to_square[(r//3, c//3)].add(board[r][c])
        
        return True
