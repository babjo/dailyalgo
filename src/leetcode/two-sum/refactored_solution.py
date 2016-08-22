'''
시간복잡도 : O(n)
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {num : idx for idx, num in enumerate(nums)}
        for idx, num in enumerate(nums):
            if (target-num) in d and d[target-num] != idx:
                return [idx, d[target-num]]
    
print Solution().twoSum([3,2,4], 6)