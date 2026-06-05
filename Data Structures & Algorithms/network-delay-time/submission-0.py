class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={i:[] for i in range(1,n+1)}
        for u,v,t in times:
            adj[u].append((v,t))
        dist=[float("inf")]*(n+1)
        dist[k]=0
        heap=[(0,k)]
        while heap:
            t,u=heapq.heappop(heap)
            if dist[u]<t:
                continue
            for v,w in adj[u]:
                if dist[v]>w+t:
                    dist[v]=w+t
                    heapq.heappush(heap,(w+t,v))
        res=max(dist[1:])
        return res if res!=float("inf") else -1
