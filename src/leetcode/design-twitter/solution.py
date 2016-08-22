from datetime import datetime
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId in self.d:
            self.d[userId][1].append((datetime.now(), tweetId))
        else:
            self.d[userId]=([], [(datetime.now(), tweetId)])


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        if userId in self.d:
            feed = self.d[userId][1][:]
            for followeeId in self.d[userId][0]:
                if followeeId in self.d:
                    feed += self.d[followeeId][1]
            return [y for x,y in sorted(feed, key=lambda pair: pair[0], reverse=True)][0:10]
        else:
            return []


    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.d:
            if followerId != followeeId and followeeId not in self.d[followerId][0]:
                self.d[followerId][0].append(followeeId)
        else:
            self.d[followerId] = ([followeeId], [])

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId in self.d:
            if followeeId in self.d[followerId][0]:
                self.d[followerId][0].remove(followeeId)

''' test case 1
twitter = Twitter()
twitter.postTweet(1, 5)
print twitter.getNewsFeed(1)
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print twitter.getNewsFeed(1)
twitter.unfollow(1, 2)
print twitter.getNewsFeed(1)
'''

# test case 2
twitter = Twitter()
twitter.postTweet(1, 1)
print twitter.getNewsFeed(1)
twitter.follow(2, 1)
print twitter.getNewsFeed(2)
twitter.unfollow(2, 1)
print twitter.getNewsFeed(2)