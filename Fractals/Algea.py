def algea(fractal, n):
	if n == 0:
		return fractal
	else:
		if fractal[0] == "A":
			return algea("A", n-1) + algea("B", n-1)
		else:
			return algea("A", n-1)

for i in range(9):
	print "n =", i, algea("A", i)