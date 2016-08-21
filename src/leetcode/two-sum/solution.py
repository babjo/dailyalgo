'''
시간복잡도 : O(n^2)
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, num in enumerate(nums):
            if (target-num) in nums and idx != nums.index(target-num):
                return [idx, nums.index(target-num)]
                
                

print Solution().twoSum([3,2,4], 6)