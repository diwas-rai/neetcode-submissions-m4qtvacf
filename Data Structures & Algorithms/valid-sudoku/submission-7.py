class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        coord_to_col = defaultdict(set)
        coord_to_row = defaultdict(set)
        coord_to_square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                if (board[r][c] in coord_to_col[c] or
                    board[r][c] in coord_to_row[r] or
                    board[r][c] in coord_to_square[(r//3, c//3)]):
                    return False
                
                coord_to_col[c].add(board[r][c])
                coord_to_row[r].add(board[r][c])
                coord_to_square[(r//3, c//3)].add(board[r][c])
                print(coord_to_square[0,0])
        
        return True
