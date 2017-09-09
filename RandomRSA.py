import randomdotorg
import random
import math
from fractions import gcd


r = randomdotorg.RandomDotOrg('UnifyID')
print r.get_quota()

# 2 * 500  ~= 1,000 bits

# I'm aware this was discouraged, but I had a lot of extra time
# and wasn't sure how to generate such a pair without building
# the framework to check primality and such


# the following code was taken from stackoverflow.com/questions/4798654
# because I think python should have a library for modular inverse
# that doesn't require viusal c++ 9.0 to install

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x- (b // a) * y, y)

def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		return 0
	return x % m

def powermod(a, n, d):
	if d == 1:
		return a
	if d % 2 == 0:
		return (powermod(a,n, d/2)**2) % n
	return (a* (powermod(a,n, d/2)**2) % n) % n



# psuedocode from https://en.wikipedia.org/wiki/Fermat_primality_test, my implementation
def fermatPrimalityTest(n):
	r = 0
	d = n-1
	while d % 2 == 0:
		d /= 2
		r += 1

	for i in range(10):
		passing = False
		# this use of random is for testing purposes and has nothing to do with generation
		# therefore it will stay using python's random module
		a = random.randrange(2, n-1)

		x = powermod(a, n, d)
		if x == 1 or x == n-1:
			passing = True

		for j in range(r-1):
			x = powermod(x, n, 2)
			if x == 1:
				return False
			if x == n-1:
				passing = True

		if passing == False:
			return False
	return True


def isPrime(n):
	return fermatPrimalityTest(n)


def genPrime(bound1, bound2):
	p = r.randrange(bound1, bound2)
	if p % 2 == 0:
		p += 1

	count = 0
	while True:
		if isPrime(p):
			print p
			break
		count += 1
		p += 2
	return p


def genRSA():
	p = genPrime(2**512, 2**513)
	q = genPrime(2**512, 2**513)
	n = p * q
	totient = n / gcd(p,q)
	e = totient
	while totient % e == 0:
		e = genPrime(2, 2**100)
	d = modinv(e, n)

	print "public N:", n
	print "public e:", e
	print "private d:", d


genRSA()
