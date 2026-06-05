from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp=[1]*(len(nums))
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i]>nums[j]:
        #             dp[i]=max(dp[i],1+dp[j])
        # return max(dp)
        sub=[]
        for n in nums:
            idx=bisect_left(sub,n)
            if idx==len(sub):
                sub.append(n)
            else:
                sub[idx]=n
        return len(sub)