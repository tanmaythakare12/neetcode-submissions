class Node:
    def __init__(self):
        self.children={}
        self.islast=False
    
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root=Node()
        def addword(word):
            curr=root
            for c in word:
                if c not in curr.children:
                    curr.children[c]=Node()
                curr=curr.children[c]
            curr.islast=True
        
        for w in words:
            addword(w)
        res=set()
        visit=set()
        def dfs(r,c,node,word):
            if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or (r,c) in visit or board[r][c] not in node.children:
                return
            visit.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.islast:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c-1,node,word)
            visit.remove((r,c))

        for r in range(len(board)):
            for c in range(len(board[0])):
                dfs(r,c,root,"")
        return list(res)
