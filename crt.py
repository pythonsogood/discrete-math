from functools import reduce


def CRT(*args: tuple[int, int]) -> int:
	"""
		Calling example (as 4.5.18 (f)):
			CRT((1003, 17369), (2974, 5472))
			outputs: 52993822
	"""
	M = reduce(lambda a, b: a * b, (i[1] for i in args))
	an = [i[0] for i in args]
	mn = [i[1] for i in args]
	Mn = [M // m for m in mn]
	Mn1 = [next((x for x in range(mn[i]) if (x * Mn[i]) % mn[i] == 1), -1) for i in range(len(args))]
	return sum([an[i] * Mn[i] * Mn1[i] for i in range(len(args))]) % M
