################################### INCLUDE ####################################

import utils

############################## PRIVATE FUNCTIONS ###############################

# Renvoie le tableau [0, 1, 2, ..., n]
def _smaller_n(n): 
	res = []
	i = 0
	while i <= n:
		res.append(i)
		i += 1
	return res

# Renvoie un tableau avec -1 si i n'est pas premier et i si il l'est
def _find_prime(n): 
    primes = _smaller_n(n)
    primes[0] = -1
    primes[1] = -1
    for i in range(2, utils.isqrt(len(primes)) + 1): 
        for j in range(i + 1, len(primes)): 
            if primes[i] != -1 and primes[j] % primes[i] == 0: 
                primes[j] = -1
    return primes

############################### PUBLIC FUNCTION ################################

# Renvoie le tableau des nombre premier plus petit que n
def eratosthene(n):
    tmp = _find_prime(n)
    res = []
    for i in range (len(tmp)): 
        if tmp[i] != -1: 
            res.append(tmp[i])
    return res

################################################################################
