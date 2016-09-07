# https://www.acmicpc.net/problem/1764

nums = map(int, raw_input().split())
N = nums[0]
M = nums[1]
total = N + M

cache = {}
result = []
for i in range(0, total):
	if i < N:
		cache[raw_input()] = 0
	else:
		name = raw_input()
		if name in cache:
			result.append(name)

print len(result)
for e in sorted(result):
	print e