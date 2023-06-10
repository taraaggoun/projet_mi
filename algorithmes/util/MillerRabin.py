################################### INCLUDE ####################################

import random

############################## PRIVATE FUNCTIONS ###############################

# Test de Primalité de n
# Si il renvoie Faux on est sure que ça le nombre est pas premier
# Si il renvoie Vrai, il y a une chance sur deux que il soit premier
def _millerrabin(n):
	if n <= 2: return True

	if n % 2 == 0: return False

	s = 0
	t = n - 1
	while 1:
		if t % 2 == 1: break
		t //= 2
		s += 1

	a = random.randint(2, n - 1)
	b = pow(a, t, n)
	
	if b == 1: return True

	for _ in range(s):
		if b == n - 1: return True
		if b == 1: return False
		b *= b
		b %= n

	return False

############################### PUBLIC FUNCTIONS ###############################

def is_prime(n):
    # 20 fois pour reduire la probabilité que le nombre ne soit pas premier
    # meme si il renvoie vrai
    nb_test = 20
    for _ in range(nb_test):
        if not _millerrabin(n):
            return False
    return True

################################################################################
