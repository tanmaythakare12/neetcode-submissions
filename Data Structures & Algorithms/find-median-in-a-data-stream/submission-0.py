class MedianFinder:

    def __init__(self):
        self.maxheap=[]
        self.minheap=[]
        self.count=0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap,-num)
        heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))
        if len(self.minheap)>len(self.maxheap):
            heapq.heappush(self.maxheap,-heapq.heappop(self.minheap))
    def findMedian(self) -> float:
        if len(self.minheap)==len(self.maxheap):
            return (self.minheap[0]-self.maxheap[0])/2
        else:
            return -self.maxheap[0]

        