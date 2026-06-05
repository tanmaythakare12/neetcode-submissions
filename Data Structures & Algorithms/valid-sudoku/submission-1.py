class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=[[0]*9 for _ in range(9)]
        rows=[[0]*9 for _ in range(9)]
        sqrs=[[0]*9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                
                pos=int(board[r][c])-1
                if rows[r][pos]==1:
                    return False
                rows[r][pos]=1

                if cols[c][pos]==1:
                    return False
                cols[c][pos]=1
                
                idx=(r//3)*3+c//3
                if sqrs[idx][pos]==1:
                    return False
                sqrs[idx][pos]=1

        return True