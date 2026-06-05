class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        [2] [2]

        '''
        res=[]
        def dfs(i,total,subset):
            if total==target:
                res.append(subset[:])
                return
            if total>target or i>=len(nums):
                return
            
            subset.append(nums[i])
            dfs(i,total+nums[i],subset)
            subset.pop()
            dfs(i+1,total,subset)
        
        dfs(0,0,[])
        return res