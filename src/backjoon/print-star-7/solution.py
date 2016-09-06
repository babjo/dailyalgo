# print-star-7 https://www.acmicpc.net/problem/2444

import sys
n = input()
total_row = 2*n-1
for row in range(0, total_row):
	dis = abs(n - (row+1))
	for unsed in range(0, dis):
		sys.stdout.write(' '),
	for unsed in range(0, total_row-2*dis):
		sys.stdout.write('*'), # print a star
	print '' # newline