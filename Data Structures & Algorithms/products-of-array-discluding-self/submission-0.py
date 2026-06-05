class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prod=1
        # zeroc=0
        # for num in nums:
        #     if num==0:
        #         zeroc+=1
        #     else:
        #         prod*=num
        # if zeroc>1:
        #     return [0]*len(nums)
        
        # res=[0]*len(nums)
        # for i,c in enumerate(nums):
        #     if zeroc==1:
        #         if c!=0:
        #             res[i]=0
        #         else:
        #             res[i]=prod
        #     else:
        #         res[i]=prod//c
        # return res
        res=[0]*(len(nums))
        pref=1
        for i in range(len(nums)):
            res[i]=pref
            pref*=nums[i]
        postf=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postf
            postf*=nums[i]
        return res
