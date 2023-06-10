############################### PUBLIC FUNCTION ################################

# Renvoie si n est B-friable
def is_friable(n, primes): 
	facteurs = {}
	cur = n
	for prime in primes:
		while cur % prime == 0:
			cur = cur // prime
			if prime in facteurs:
				facteurs[prime] += 1
			else :
				facteurs[prime] = 1
			if cur == 1:
				return (True, facteurs)
	return (False, {})

################################################################################
