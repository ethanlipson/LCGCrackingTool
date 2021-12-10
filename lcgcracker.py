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
	pass

def primes(n):
	out = []
	while n % 2 == 0:
		n /= 2
		out.append(2)
	f = 3
	while f * f <= n:
		if n % f == 0:
			out.append(f)
			n /= f
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

def lcm(a,b):
	a_p=primes(a)
	b_p=primes(b)
	out = 1
	while len(a_p) > 0 or len(b_p) > 0:
		a_l = a_p[-1] if len(a_p) else 1
		b_l = b_p[-1] if len(b_p) else 1

		if a_l >= b_l:
			a_p.pop()
		if a_l <= b_l:
			b_p.pop()

		out *= max(a_l,b_l)
	return out

if __name__ == '__main__':
	main()