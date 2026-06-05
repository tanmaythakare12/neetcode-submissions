class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        a-b=target
        a+b=sum
        a=(target+sum)//2
        '''
        summ=sum(nums)
        if (target+summ)%2!=0 or summ<abs(target):
            return 0
        ntar=(target+summ)//2
        dp=[[0]*(ntar+1) for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0]=1
        for i in range(1,len(nums)+1):
            for j in range(ntar+1):
                if nums[i-1]==0:
                    dp[i][j]=2*dp[i-1][j]
                else:
                    nottake=dp[i-1][j]
                    take=0
                    if nums[i-1]<=j:
                        take=dp[i-1][j-nums[i-1]]
                    dp[i][j]=take+nottake
        return dp[len(nums)][ntar]