class Twitter:

    def __init__(self):
        self.follow_dict = defaultdict(set) # store the userid and set of its followees(whom the user follows)
        self.tweets_dict = defaultdict(deque) # stores user id and list of its TweetIDs
        self.time_stamp=0
    def postTweet(self, userId: int, tweetId: int) -> None:
        if len(self.tweets_dict[userId])<11:
            self.follow_dict[userId].add(userId)
            self.tweets_dict[userId].append([self.time_stamp,tweetId])
            self.time_stamp+=1
        else:
            self.tweets_dict[userId].popleft()
            self.tweets_dict[userId].append([self.time_stamp,tweetId])
            self.time_stamp+=1
    def getNewsFeed(self, userId: int) -> List[int]:
        tweets_list =[]
        for i in self.follow_dict[userId]:
            tweets_list.extend(self.tweets_dict[i])
        max_heap = [[-x[0],x[1]] for x in tweets_list]
        heapq.heapify(max_heap)
        k=0
        l= len(max_heap)
        res=[]
        while k<10 and k<l:
            latest_tweetid = heapq.heappop(max_heap)
            res.append(latest_tweetid[1])
            k+=1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_dict[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)