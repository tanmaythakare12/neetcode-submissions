class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj={i:[] for i in range(len(points))}
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                adj[i].append((dist,j))
                adj[j].append((dist,i))
        minheap=[(0,0)]
        visit=set()
        res=0
        while len(visit)<len(points):
            dist,cur=heapq.heappop(minheap)
            if cur in visit:
                continue
            res+=dist
            visit.add(cur)
            for ne in adj[cur]:
                heapq.heappush(minheap,ne)
        return res