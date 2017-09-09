# import randomdotorg
import random
import math


# r = randomdotorg.RandomDotOrg('UnifyID')
# print r.get_quota()

# 2 * 500 * (around 200 expected from prime number theorem, go with 400 upper bound) ~= 400,000 bits

def isPrime(n):
	# for now we'll just test this
	# this will be replaced by a probablistic prime test
	# 	see https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
	# 		https://en.wikipedia.org/wiki/Fermat_primality_test
	for i in range(2, 1000):
		if n%i == 0:
			return False
	return True


def genPrime():
	p = random.randrange(2**512, 2**513)
	if p % 2 == 0:
		p += 1

	count = 0
	while True:
		if isPrime(p):
			print p
			break
		count += 1
		p += 2
		print count
	return p


def genRSA():
	p = genPrime()
	q = genPrime()

genRSA()
