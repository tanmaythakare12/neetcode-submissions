class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # ROWS, COLS = len(grid), len(grid[0])
        # # visit = set()

        # def dfs(r, c):
        #     if (r < 0 or r == ROWS or c < 0 or
        #         c == COLS or grid[r][c] == 0 
        #     ):
        #         return 0
        #     grid[r][c]=0
        #     return (1 + dfs(r + 1, c) +
        #                 dfs(r - 1, c) +
        #                 dfs(r, c + 1) +
        #                 dfs(r, c - 1))

        # area = 0
        # for r in range(ROWS):
        #     for c in range(COLS):
        #         area = max(area, dfs(r, c))
        # return area
        area=0
        def dfs(r,c):
            if r<0 or r>=len(grid) or c<0 or c>=len(grid[0]) or grid[r][c]==0:
                return 0
            grid[r][c]=0
            res=1
            res+=dfs(r+1,c)
            res+=dfs(r-1,c)
            res+=dfs(r,c+1)
            res+=dfs(r,c-1)
            return res
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                area=max(area,dfs(r,c))
        return area
