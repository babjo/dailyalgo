nums = map(int, raw_input().split())
C, R = nums[0], nums[1]
K = input()

if C * R < K:
	print 0
else:
	x, y = 1, 0
	i = 0
	sgn = 1
	C -= 1
	while i < K:
		if i <= K and K < i+R:
			y += sgn*(K - i)
			break
		else:
			y += sgn*R
			i += R
		R -= 1
		if i <= K and K < i+C:
			x += sgn*(K - i)
			break
		else:
			x += sgn*C
			i += C
		C -= 1
		sgn = -sgn

	print x, y