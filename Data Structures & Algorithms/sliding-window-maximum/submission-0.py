class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        output=[]
        q=deque()
        for i in range(len(nums)):
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)

            if q[0]<=i-k:
                q.popleft()
            
            if i+1>=k:
                output.append(nums[q[0]])
            
        return output
            