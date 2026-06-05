class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        indeg=[[0]*n for _ in range(m)]
        direct=[(1,0),(0,1),(-1,0),(0,-1)]
        for r in range(m):
            for c in range(n):
                for dr,dc in direct:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<m and 0<=nc<n and matrix[nr][nc]<matrix[r][c]:
                        indeg[r][c]+=1
        q=deque()
        for r in range(m):
            for c in range(n):
                if indeg[r][c]==0:
                    q.append((r,c))
        res=0
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                for dr,dc in direct:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<m and 0<=nc<n and matrix[nr][nc]>matrix[r][c]:
                        indeg[nr][nc]-=1
                        if indeg[nr][nc]==0:
                            q.append((nr,nc))
            res+=1
        return res
