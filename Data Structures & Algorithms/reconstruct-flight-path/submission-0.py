class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse=True)
        adj={}
        for u,v in tickets:
            if u not in adj:
                adj[u]=[]
            adj[u].append(v)
        
        stack=["JFK"]
        res=[]
        while stack:
            curr=stack[-1]
            if curr not in adj or len(adj[curr])==0:
                res.append(stack.pop())
            else:
                stack.append(adj[curr].pop())
        return res[::-1]

