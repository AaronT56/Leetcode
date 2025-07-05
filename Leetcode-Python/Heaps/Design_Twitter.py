from collections import defaultdict
import heapq
class Twitter:
    def __init__(self):
        self.count = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        # So we are taking some user, and finding the ten most recent tweets in their
        # feed. This includes their own tweets (line above). We take each follower, and
        # check if they have any tweets. Note that when they post tweets, an associated
        # count was added to the tweetMap dictionary. This indicates the order of tweets
        # by recency. We will use this to find the 10 most recent tweets from the user
        # and their followers.
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # This will be the most recent tweet from a given user.
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
        
        heapq.heapify(minHeap)
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0: 
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followeeId]:
            self.followMap[followerId].remove(followeeId)
