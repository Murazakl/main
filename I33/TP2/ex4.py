def euler_phi(n):
	Zn = 0
	i = 0
	while i < n:
		a, b = i, n
		while b > 0:
			a, b = b, a % b
		if a == 1:
			Zn += 1
		i += 1
	return Zn

print(euler_phi(57))