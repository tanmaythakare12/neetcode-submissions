class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj={i:[] for i in range(n)}
        for u,v,c in flights:
            adj[u].append((v,c))
        dist=[float("inf")]*n
        dist[src]=0
        q=deque([(src,0,0)])
        while q:
            node,cost,step=q.popleft()
            if step>k:
                continue
            for ne,w in adj[node]:
                if dist[ne]>cost+w:
                    dist[ne]=cost+w
                    q.append((ne,cost+w,step+1))
        
        return dist[dst] if dist[dst]!=float("inf") else -1