class Solution(object):
	def optimal(self, keys, freq):
		N = len(keys)
		Matrix = [[0 for x in range(N+1)] for y in range(N+2)] 
		
		for idx, e in enumerate(freq):
			Matrix[idx+1][idx+1] = e

		for diagonal in range(1, N):
			for i in range(1, N-diagonal+1):
				j = i + diagonal
				Matrix[i][j] = min([Matrix[i][k-1] + self.sum(freq, i, k-1) + freq[k-1] + Matrix[k+1][j] + self.sum(freq, k+1, j) for k in range(i, j+1)])
		
		return Matrix[1][N]
		
	def sum(self, freq, i, j):
		s = 0
		for k in range(i-1, j):
			s += freq[k]
		return s

print Solution().optimal([10, 12, 20], [34, 8, 50])
print Solution().optimal([2, 4, 6, 8], [0.1, 0.4, 0.2, 0.3])