class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap=[]
        for s in stones:
            heapq.heappush(maxheap,-s)
        while len(maxheap)>1:
            s1=heapq.heappop(maxheap)
            s2=heapq.heappop(maxheap)
            if s1<s2:
                heapq.heappush(maxheap,s1-s2)
        return abs(maxheap[0]) if maxheap else 0
            