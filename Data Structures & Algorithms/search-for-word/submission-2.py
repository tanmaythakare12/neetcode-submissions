class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r,c,i):
            if i==len(word):
                return True
            if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or board[r][c]!=word[i] or board[r][c]==".":
                return False
            board[r][c]="."
            res=False
            for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr=r+dr
                nc=c+dc
                res=res or dfs(nr,nc,i+1)
            board[r][c]=word[i]
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(r,c,0):
                    return True
        return False