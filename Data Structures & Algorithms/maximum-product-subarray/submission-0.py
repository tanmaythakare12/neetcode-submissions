class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=1
        mini=1
        res=nums[0]
        for n in nums:
            temp=maxi*n
            maxi=max(maxi*n,mini*n,n)
            mini=min(temp,mini*n,n)
            res=max(res,maxi)
        return res