################################### INCLUDE ####################################

import MillerRabin
import random

############################## PRIVATE FUNCTION ################################

# Genere un nombre premier entre min et max
def _generate(min, max):
	rand = 0
	while (True):
		rand = random.randint(min, max)
		if MillerRabin.is_prime(rand):
			break
	return rand

############################### PUBLIC FUNCTION ################################

# multiplie deux nombre premier entre eux
def generator(min=1<<15, max=1<<20):
	n = 2
	res = 1
	for _ in range(n):
		rand = _generate(min, max)
		res *= rand
	return res

################################################################################
