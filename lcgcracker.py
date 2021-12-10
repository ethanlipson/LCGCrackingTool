#!/usr/bin/env python3
#feel free to rename this file, lcgcracker sounds lame :(

import sys

#I'm using standard input to read numbers,
#but we could add functionality for arguments.
def main():
	givens=[]
	for line in sys.stdin:
		givens.append(int(line))
	solveLCG(givens)

def solveLCG(givens):
	#now for the tricky bit...

	#subtract equations to get N[k] === X[k]*a mod M
	N=[]
	X=[]
	for i in range(2,len(givens)):
		N.append(givens[i]-givens[1])
		X.append(givens[i-1]-givens[0])

	print(list(zip(N,X)))

	pass


def primes(n):
	out = []
	while n % 2 == 0:
		n //= 2
		out.append(2)
	f = 3
	while f * f <= n:
		if n % f == 0:
			out.append(f)
			n //= f
		else:
			f += 2
	if n != 1:
		out.append(n)
	return out

#cool trick I came up with to calculate all factors quickly.
#doing it the brute force way took like 5 seconds for big numbers.
#numbers are not in order.
def factors(n):
	prime = primes(n)
	count = len(prime)
	out = set()
	for i in range(0,2**count):
		factor = 1
		for j in range(0, count):
			factor *= prime[j] if i%2 else 1
			i /= 2
		out.add(factor)
	return out

def lcm(nums):
	n_primes = list(map(primes,nums))
	print(n_primes)
	out = 1
	while any(n_primes):
		large = list(map(lambda x: x[-1] if x else 1, n_primes))
		m = max(large)
		out *= m

		print(large)

		for l in n_primes:
			if len(l) > 0 and l[-1] == m:
				l.pop()
	return out

if __name__ == '__main__':
	main()