class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen=0
        startl=0
        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if maxlen<r-l+1:
                    maxlen=r-l+1
                    startl=l
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if maxlen<r-l+1:
                    maxlen=r-l+1
                    startl=l
                l-=1
                r+=1
        return s[startl:startl+maxlen]