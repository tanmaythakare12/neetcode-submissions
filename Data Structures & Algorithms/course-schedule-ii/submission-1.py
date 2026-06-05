class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # prereq = {c: [] for c in range(numCourses)}
        # for crs, pre in prerequisites:
        #     prereq[crs].append(pre)

        # output = []
        # visit, cycle = [], set()

        # def dfs(crs):
        #     if crs in cycle:
        #         return False
        #     if crs in visit:
        #         return True

        #     cycle.add(crs)
        #     for pre in prereq[crs]:
        #         if dfs(pre) == False:
        #             return False
        #     cycle.remove(crs)
        #     visit.append(crs)
        #     # output.append(crs)
        #     return True

        # for c in range(numCourses):
        #     if dfs(c) == False:
        #         return []
        # return visit
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
        return res if len(res)==numCourses else []