################################### INCLUDES ###################################

import sys

sys.path.insert(0, 'util/')

import utils

############################## PRIVATE FUNCTIONS ##############################

# Renvoie si racine de n si n est un carré -1 sinon
def _is_square(n):
    if n < 0 : return -1
    root = utils.isqrt(n)
    if n == root * root:
        return (1, root)
    return (-1, root)

# Retourne a et b tel que n = ab
def _find_a_b(n): 
    (b, root) = _is_square(n)
    if b == 1: 
        return (root, root)
    for u in range (1, ((n + 1) // 2) + 1):
        r = root + u
        (b, s) = _is_square((r * r) - n)
        if b == 1: 
            return (r - s, r + s)
    return (n, 1)

############################### PUBLIC FUNCTION ################################

# Trouve tout les diviseurs de n sous forme d un dictionnaire
def all_divider(n, facteurs={}):
    (a, b) = _find_a_b(n)
    if a == n or b == n:
        facteurs[n] = facteurs.get(n, 0) + 1
    else:
        utils.merge_dicts(facteurs, all_divider(a, facteurs))
        utils.merge_dicts(facteurs, all_divider(b, facteurs))
    return facteurs

################################################################################
