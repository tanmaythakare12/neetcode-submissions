class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def bfs(q,res):
            direct=[(1,0),(0,1),(-1,0),(0,-1)]
            while q:
                r,c=q.popleft()
                for dr,dc in direct:
                    nr=dr+r
                    nc=dc+c
                    if nr<0 or nr>=len(heights) or nc<0 or nc>=len(heights[0]) or heights[nr][nc]<heights[r][c] or res[nr][nc]==True:
                        continue
                    res[nr][nc]=True
                    q.append((nr,nc))
            return res
                

        pac=[[False]*len(heights[0]) for _ in range(len(heights))]
        atl=[[False]*len(heights[0]) for _ in range(len(heights))]


        pacific=deque()
        atlantic=deque()
        for r in range(len(heights)):
            pacific.append((r,0))
            pac[r][0]=True
            atlantic.append((r,len(heights[0])-1))
            atl[r][len(heights[0])-1]=True
        for c in range(len(heights[0])):
            pacific.append((0,c))
            pac[0][c]=True
            atlantic.append((len(heights)-1,c))
            atl[len(heights)-1][c]=True

        bfs(pacific,pac)
        bfs(atlantic,atl)
        ans=[]
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if pac[r][c] and atl[r][c]:
                    ans.append((r,c))
        return ans

