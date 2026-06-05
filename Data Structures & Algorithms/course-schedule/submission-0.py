class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={n:[] for n in range(numCourses)}
        for u,v in prerequisites:
            adj[v].append(u)
        indeg={n:0 for n in range(numCourses)}
        for u,v in prerequisites:
            indeg[u]+=1
        q=deque()
        for u in indeg:
            if indeg[u]==0:
                q.append(u)
        res=[]
        while q:
            node=q.popleft()
            res.append(node)
            for ne in adj[node]:
                indeg[ne]-=1
                if indeg[ne]==0:
                    q.append(ne)
        return len(res)==numCourses
