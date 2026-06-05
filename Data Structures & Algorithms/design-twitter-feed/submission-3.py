class Twitter:

    def __init__(self):
        self.followm={}
        self.tweet={}
        self.count=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweet:
            self.tweet[userId]=[]
        self.tweet[userId].append([self.count,tweetId])
        self.count-=1
    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        minheap=[]
        if userId not in self.followm:
            self.followm[userId]=set()
        self.followm[userId].add(userId)
        for followId in self.followm[userId]:
            if followId not in self.tweet:
                continue
            idx=len(self.tweet[followId])-1
            count,tweetId=self.tweet[followId][idx]
            heapq.heappush(minheap,[count,tweetId,followId,idx-1])
        while minheap and len(res)<10:
            count,tweetId,followId,idx=heapq.heappop(minheap)
            res.append(tweetId)
            if idx>=0:
                count,tweetId=self.tweet[followId][idx]
                heapq.heappush(minheap,[count,tweetId,followId,idx-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followm:
            self.followm[followerId]=set()
        self.followm[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followm and followeeId in self.followm[followerId]:
            self.followm[followerId].remove(followeeId)

