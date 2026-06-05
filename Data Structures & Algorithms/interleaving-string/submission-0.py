class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n=len(s1)
        m=len(s2)
        if len(s1)+len(s2)!=len(s3):
            return False
        dp=[[False]*(len(s1)+1) for _ in range(len(s2)+1)]
        dp[0][0]=True
        for i in range(1,len(s2)+1):
            if dp[i-1][0] and s2[i-1]==s3[i-1]:
                dp[i][0]=True
            else:
                break
        
        for j in range(1,len(s1)+1):
            if dp[0][j-1] and s1[j-1]==s3[j-1]:
                dp[0][j]=True
            else:
                break
        
        for i in range(1,len(s2)+1):
            for j in range(1,len(s1)+1):
                res=False
                if dp[i-1][j] and s2[i-1]==s3[i+j-1]:
                    res|=True
                if dp[i][j-1] and s1[j-1]==s3[i+j-1]:
                    res|=True
                dp[i][j]=res
        return dp[len(s2)][len(s1)]