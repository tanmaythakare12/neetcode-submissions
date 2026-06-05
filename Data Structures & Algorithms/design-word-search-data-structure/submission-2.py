class Node:
    def __init__(self):
        self.children={}
        self.islast=False

class WordDictionary:

    def __init__(self):
        self.root=Node()

    def addWord(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=Node()
            curr=curr.children[c]
        curr.islast=True

    def search(self, word: str) -> bool:
        def dfs(idx,root):
            curr=root
            for i in range(idx,len(word)):
                c=word[i]
                if c==".":
                    for ch in curr.children.values():
                        if dfs(i+1,ch):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr=curr.children[c]
            return curr.islast
        return dfs(0,self.root)