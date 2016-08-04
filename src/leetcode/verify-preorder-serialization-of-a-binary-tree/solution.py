class Solution(object):
	def isValidSerialization(self, preorder):
		"""
		:type preorder: str
		:rtype: bool
		"""
		count = 1
		l = preorder.split(',')
		i = 0
		while i < len(l):
			if l[i] == '#':
				count -= 1
			else :
				count += 1
			if i != len(l)-1 and count == 0 : return False
			i += 1

		return count == 0


print Solution().isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#")
print Solution().isValidSerialization("#,#,3,5,#")
print Solution().isValidSerialization("#,7,6,9,#,#,#")
print Solution().isValidSerialization("#,#,3,5,#");