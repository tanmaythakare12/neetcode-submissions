"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        map1={}
        map1[node]=Node(node.val)
        q=deque([node])
        while q:
            cur=q.popleft()
            for ne in cur.neighbors:
                if ne not in map1:
                    map1[ne]=Node(ne.val)
                    q.append(ne)
                map1[cur].neighbors.append(map1[ne])
        return map1[node]