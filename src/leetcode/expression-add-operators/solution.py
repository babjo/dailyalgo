class Solution(object):
	def addOperators(self, num, target):
		self.result = []
		self.dfs(num, target, 1, '', 0)
		return self.result

	def dfs(self, num, target, pre, path, value):
		if len(num) == 0 and value == target:
			self.result.append(path)
			
		candidates = [(num[:start], num[start:]) for start in range(1, len(num)+1)]
		for candidate in candidates:
			to_calc = candidate[0]
			rest = candidate[1]
			if len(to_calc) > 1 and to_calc[0] == '0': break

			if len(path) == 0:
				# start path
				self.dfs(rest, target, int(to_calc), to_calc, int(to_calc))
			else:
				# +
				self.dfs(rest, target, int(to_calc), path+'+'+to_calc, value+int(to_calc))
				# -
				self.dfs(rest, target, -int(to_calc), path+'-'+to_calc, value-int(to_calc))
				# *
				self.dfs(rest, target, pre*int(to_calc), path+'*'+to_calc, (value-pre)+pre*int(to_calc))
				
print Solution().addOperators("123", 6)
print Solution().addOperators("00", 0)
print Solution().addOperators("3456237490", 9191)
print Solution().addOperators("105", 5)
print Solution().addOperators("232", 8)