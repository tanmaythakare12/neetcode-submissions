class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        fresh=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==2:
                    q.append((r,c,0))
                elif grid[r][c]==1:
                    fresh+=1
        direct=[(1,0),(0,1),(-1,0),(0,-1)]
        t=0
        while q:
            r,c,t=q.popleft()
            for dr,dc in direct:
                nr=r+dr
                nc=c+dc
                if nr<0 or nr>=len(grid) or nc<0 or nc>=len(grid[0]) or grid[nr][nc]!=1:
                    continue
                grid[nr][nc]=2
                fresh-=1
                q.append((nr,nc,t+1))
        return t if fresh==0 else -1