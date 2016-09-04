import itertools
import collections

class Solution(object):
	def palindromePairs(self, words):
		"""
		:type words: List[str]
		:rtype: List[List[int]]
		"""
		d = { word : idx for idx, word in enumerate(words)}

		results = []
		for idx, word in enumerate(words):
			for i in range(0, len(word)+1):
				word1, word2 = word[0:i], word[i:]
		
				if self.isPalindrome(word2):
					reversed_word1 = word1[::-1]
					if (reversed_word1 in d) and d[reversed_word1] != idx:
						results.append([idx, d[reversed_word1]])

				if self.isPalindrome(word1):
					reversed_word2 = word2[::-1]
					if (reversed_word2 in d) and d[reversed_word2] != idx and word1:
						results.append([d[reversed_word2], idx])

		return results

	def isPalindrome(self, t):
		return t[::-1] == t


print Solution().palindromePairs(["bat", "tab", "cat"])
print Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])