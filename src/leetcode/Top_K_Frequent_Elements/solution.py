from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [key for value, key in sorted([(value, key) for (key, value) in Counter(nums).items()], reverse=True)[:k]]
        

print Solution().topKFrequent([1,1,1,2,2,3,4], 2)
print Solution().topKFrequent([1], 1)