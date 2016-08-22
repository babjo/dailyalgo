#-*- coding: utf-8 -*-
from datetime import datetime
import collections
import heapq
import itertools

'''
리팩토링 지점
1. map에서 key 확인하는 if문 없애기 => collections.defaultdict(callable)
2. list에서 key 확인하는 if문 없애기 => 자료구조 set
3. 여러 배열을 하나의 배열로 모으고 정렬하기 => heapq.merge, sorted(itertools.chain(*iterables))
'''

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = collections.defaultdict(list)
        self.followees = collections.defaultdict(set)


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.tweets[userId].append((datetime.now(), tweetId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        tweets = sorted(itertools.chain(*(self.tweets[followeeId] for followeeId in self.followees[userId] | {userId})), key=lambda pair: pair[0], reverse=True)
        return [tweet for timestampe, tweet in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        self.followees[followerId].discard(followeeId)

twitter = Twitter()
twitter.postTweet(1, 5)
print twitter.getNewsFeed(1)
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print twitter.getNewsFeed(1)
twitter.unfollow(1, 2)
print twitter.getNewsFeed(1)


