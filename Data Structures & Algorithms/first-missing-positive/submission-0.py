class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numset=set(nums)
        miss=1
        while miss in numset:
            miss+=1
        return miss