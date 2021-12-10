#feel free to rename this file, lcgcracker sounds lame :(

def primeFactors(n):
	primes = []
	while n % 2 == 0:
		n /= 2
		primes.append(2)
	factor = 3
	while n > 1:
		if n % factor == 0:
			primes.append(factor)
			n /= factor
		else:
			factor += 2
	return primes

#cool trick I came up with to calculate all factors quickly.
#doing it the brute force way took like 5 seconds for big numbers.
#numbers are not in order.
def factors(n):
	primes = primeFactors(n)
	count = len(primes)
	out = set()
	for i in range(0,2**count):
		factor = 1
		for j in range(0, count):
			factor *= primes[j] if i%2 else 1
			i /= 2
		out.add(factor)
	return out
