n = input()
inputs = []
start_row = map(int, raw_input().split())
for unused in range(1, n):
	new_row = map(int, raw_input().split())
	for idx, e in enumerate(new_row):
		if idx == 0:
			new_row[idx] += start_row[0]
		elif idx == len(new_row)-1:
			new_row[idx] += start_row[idx-1]
		else:
			new_row[idx] = max([new_row[idx] + start_row[idx-1], new_row[idx] + start_row[idx]])
	start_row = new_row

print max(new_row)