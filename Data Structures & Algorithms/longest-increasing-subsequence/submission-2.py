from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp=[1]*(len(nums))
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i]>nums[j]:
        #             dp[i]=max(dp[i],1+dp[j])
        # return max(dp)
        def bisectn(sub,n):
            l=0
            r=len(sub)-1
            ans=len(sub)
            while l<=r:
                mid=l+(r-l)//2
                if sub[mid]>=n:
                    ans=mid
                    r=mid-1
                else:
                    l=mid+1
            return ans
        sub=[]
        for n in nums:
            idx=bisectn(sub,n)
            if idx==len(sub):
                sub.append(n)
            else:
                sub[idx]=n
        return len(sub)