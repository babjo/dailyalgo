class Solution(object):
	def largestDivisibleSubset(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		cached = {-1 : set()}
		for num in sorted(nums):
			largest = {num}
			for key, value in cached.items():
				if num % key == 0 and len(largest) < len(value | {num}):
					largest = value | {num}
			cached[num] = largest
			
		return list(max(cached.values(), key=len))

print Solution().largestDivisibleSubset([1,2,4,8])
print Solution().largestDivisibleSubset([1,2,3])
print Solution().largestDivisibleSubset([1])
print Solution().largestDivisibleSubset([1,2])
print Solution().largestDivisibleSubset([])
print Solution().largestDivisibleSubset([1,2,4,8,9,72])
print Solution().largestDivisibleSubset([1,2,3])