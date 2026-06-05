class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxlen=0
        maxans=""
        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if maxlen<r-l+1:
                    maxlen=r-l+1
                    maxans=s[l:r+1]
                l-=1
                r+=1
            l=i
            r=i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if maxlen<r-l+1:
                    maxlen=r-l+1
                    maxans=s[l:r+1]
                l-=1
                r+=1
        return maxans