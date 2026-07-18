class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        map1={0:1}
        currsum=0
        res=0
        for num in nums:
            currsum+=num
            diff=currsum-k
            res+=map1.get(diff,0)
            map1[currsum]=map1.get(currsum,0)+1
        return res

