import itertools

# 5 0
# -7 -3 -2 5 8

inputs = map(int, raw_input().split())
N = inputs[0]
S = inputs[1]
nums = map(int, raw_input().split())
count = 0
for i in range(1, N+1):
	for com in itertools.combinations(nums, i):
		if S == sum(com):
			count += 1

print count