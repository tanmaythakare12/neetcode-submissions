class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols=[set() for _ in range(9)]
        rows=[set() for _ in range(9)]
        sqrs=[set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                
                pos=int(board[r][c])-1
                if pos in rows[r]:
                    return False
                rows[r].add(pos)

                if pos in cols[c]:
                    return False
                cols[c].add(pos)
                
                idx=(r//3)*3+c//3
                if pos in sqrs[idx]:
                    return False
                sqrs[idx].add(pos)
        return True