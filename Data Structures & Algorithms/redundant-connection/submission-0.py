class DSU:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    def findparent(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.findparent(self.parent[u])
        return self.parent[u]
    def unionbyrank(self,u,v):
        pu=self.findparent(u)
        pv=self.findparent(v)
        if self.rank[pu]>self.rank[pv]:
            self.parent[pv]=pu
        elif self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu=DSU(len(edges)+1)
        for u,v in edges:
            if dsu.findparent(u)==dsu.findparent(v):
                return [u,v]
            else:
                dsu.unionbyrank(u,v)
        return [-1,-1]