class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={}
        for w in words:
            for c in w:
                adj[c]=set()
        indeg={c:0 for c in adj}
        for i in range(len(words)-1):
            word1=words[i]
            word2=words[i+1]
            minlen=min(len(word1),len(word2))
            if len(word1)>len(word2) and word1[:minlen]==word2[:minlen]:
                return ""
            for j in range(minlen):
                if word1[j]!=word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        indeg[word2[j]]+=1
                    break
            
        q=deque()
        for j in indeg:
            if indeg[j]==0:
                q.append(j)
        
        res=[]
        while q:
            cur=q.popleft()
            res.append(cur)
            for ne in adj[cur]:
                indeg[ne]-=1
                if indeg[ne]==0:
                    q.append(ne)
        
        if len(res)!=len(indeg):
            return ""
        return "".join(res)