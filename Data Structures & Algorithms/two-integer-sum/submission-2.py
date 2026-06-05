class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        
        for i,n in enumerate(nums):
            val=target-n
            if val in hashmap:
                return [hashmap[val],i]
            hashmap[n]=i
