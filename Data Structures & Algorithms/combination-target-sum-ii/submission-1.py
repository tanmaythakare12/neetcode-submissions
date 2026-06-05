class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def dfs(i,total,subset):
            if total==target:
                res.append(subset[:])
                return
            if total>target or i>=len(candidates):
                return
            subset.append(candidates[i])
            dfs(i+1,total+candidates[i],subset)
            subset.pop()

            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,total,subset)
        dfs(0,0,[])
        return res 