class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist=[]
        for x,y in points:
            d=x**2+y**2
            dist.append((d,[x,y]))
        heapq.heapify(dist)
        ans=[]
        while k and dist:
            d=heapq.heappop(dist)
            ans.append(d[1])
            k-=1
        return ans