n = 100
x1 = [2,0,-2,0,3]
x2 = [0,5,-3,0,3]
x3 = [0,0,5,-1,8]
x4 = [0,-1,0,5,8]

best = 0

for a in range(0, n):
	for b in range(0, n-a):
		for c in range(0, n-b-a):
			d = n - c-b-a
			s = 1
			if (a*x1[4] + b*x2[4] + c*x3[4] + d*x4[4]) != 500:
				continue
			for i in range(4):
				r = a*x1[i] + b*x2[i] + c*x3[i] + d*x4[i]
				if r <= 0:
					s = 0
					break
				s *= r
			new_best = max(best, s)
			if new_best > best:
				best = new_best
			

print(best)