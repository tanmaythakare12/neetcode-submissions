class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def ispalindrome(word):
            l=0
            r=len(word)-1
            while l<r:
                if word[l]!=word[r]:
                    return False
                l+=1
                r-=1
            return True
        def backtrack(idx,subset):
            if idx==len(s):
                res.append(subset[:])
                return
            for i in range(idx,len(s)):
                if ispalindrome(s[idx:i+1]):
                    subset.append(s[idx:i+1])
                    backtrack(i+1,subset)
                    subset.pop()
        backtrack(0,[])
        return res