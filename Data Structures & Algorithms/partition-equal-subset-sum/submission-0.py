class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summ=sum(nums)
        if summ%2!=0:
            return False
        target=summ//2
        dp=[[False]*(target+1) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][0]=True
        if nums[0]<=target:
            dp[0][nums[0]]=True
        for i in range(1,len(nums)):
            for j in range(1,target+1):
                nottake=dp[i-1][j]
                take=False
                if nums[i]<=j:
                    take=dp[i-1][j-nums[i]]
                dp[i][j]=take or nottake
        return dp[len(nums)-1][target]