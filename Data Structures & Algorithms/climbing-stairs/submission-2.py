class Solution:
    def climbStairs(self, n: int) -> int:
        # if n<=1:
        #     return n
        # dp=[0]*(n+1)
        # dp[1]=1
        # dp[2]=2
        # for i in range(3,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]
        memo={}
        def dfs(steps):
            if steps<=2:
                return steps
            if steps in memo:
                return memo[steps]
            memo[steps]=dfs(steps-1)+dfs(steps-2)
            return memo[steps]
        return dfs(n)
        