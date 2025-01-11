def gcd(a: int, b: int) -> int:
	return gcd(b % a, a) if a != 0 else b
