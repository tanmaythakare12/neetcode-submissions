class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj={i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit=set()
        def bfs(root):
            q=deque([root])
            visit.add(root)
            while q:
                node=q.popleft()
                for ne in adj[node]:
                    if ne not in visit:
                        visit.add(ne)
                        q.append(ne)
                     
        cnt=0
        for i in range(n):
            if i not in visit:
                bfs(i)
                cnt+=1
        return cnt
        
