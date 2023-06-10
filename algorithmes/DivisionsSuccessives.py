################################### INCLUDES ###################################

import sys

sys.path.insert(0, 'util/')

import utils
import crible_eratosthene as ce

############################### PRIVATE FUNCTION ###############################

# Recupere le plus petit diviseur de n premier
# Si il n'en a pas, n est premier
def _smaller_divider(primes, n): 
    for i in range (len(primes)): 
        if n % primes[i] == 0: 
            return primes[i]
    return n

############################### PUBLIC FUNCTION ################################

# Trouve tout les diviseurs de n sous forme d un dictionnaire
def all_divider(n):
    i = 0
    facteurs = {}
    diviseur = ce.eratosthene(utils.isqrt(n) + 1)
    while (i != n):
        i = _smaller_divider(diviseur, n)
        if i != 1:
            facteurs[i] = facteurs.get(i ,0) + 1
        n //= i
    if i == n and i != 1:
        if i in facteurs:
            facteurs[i] = facteurs.get(i ,0) + 1
    return facteurs

################################################################################
