class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res=[]
        cols=set()
        diag=set()
        antidiag=set()
        board=[["."]*n for i in range(n)]
        def backtrack(row, cols, diag, antidiag):
            if row==n:
                res.append(["".join(rows) for rows in board])
                return
            
            for c in range(n):
                if c in cols or row+c in diag or row-c in antidiag:
                    continue
                cols.add(c)
                diag.add(row+c)
                antidiag.add(row-c)
                board[row][c]="Q"
                backtrack(row+1,cols,diag,antidiag)
                cols.remove(c)
                diag.remove(row+c)
                antidiag.remove(row-c)
                board[row][c]="."
        backtrack(0,cols,diag,antidiag)
        return res