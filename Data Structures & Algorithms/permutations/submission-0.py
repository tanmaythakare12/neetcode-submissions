class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        status=[False]*len(nums)
        def backtrack(subset,status):
            if len(subset)==len(nums):
                res.append(subset[:])
                return
            for i in range(len(nums)):
                if not status[i]:
                    status[i]=True
                    subset.append(nums[i])
                    backtrack(subset,status)
                    subset.pop()
                    status[i]=False
        backtrack([],status)
        return res