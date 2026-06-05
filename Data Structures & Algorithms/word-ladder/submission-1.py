class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        pattern={}
        for word in wordList:
            for i in range(len(word)):
                pat=word[:i]+"*"+word[i+1:]
                if pat not in pattern:
                    pattern[pat]=[]
                pattern[pat].append(word)
        q=deque([beginWord])
        cnt=1
        visit=set()
        visit.add(beginWord)
        while q:
            for _ in range(len(q)):
                word=q.popleft()
                if word==endWord:
                    return cnt
                for i in range(len(word)):
                    pat=word[:i]+"*"+word[i+1:]
                    for ne in pattern[pat]:
                        if ne not in visit:
                            visit.add(ne)
                            q.append(ne)
            cnt+=1
        return 0