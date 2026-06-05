class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map1=set()
        for i in nums:
            if i in map1:
                return True
            map1.add(i)
        return False       