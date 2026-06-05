class DSU:
    def __init__(self,n):
        self.n=n
        self.comp=n
        self.parent=[i for i in range(self.n)]
        self.rank=[0]*self.n
    def findparent(self,u):
        if self.parent[u]!=u:
            self.parent[u]=self.findparent(self.parent[u])
        return self.parent[u]
    def unionbyrank(self,u,v):
        pu=self.findparent(u)
        pv=self.findparent(v)
        if pu==pv:
            return
        self.comp-=1
        if self.rank[pu]>self.rank[pv]:
            self.parent[pv]=pu
        elif self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)>n-1:
            return False
        dsu=DSU(n)
        for u,v in edges:
            if dsu.findparent(u)==dsu.findparent(v):
                return False
            else:
                dsu.unionbyrank(u,v)
        return dsu.comp==1
