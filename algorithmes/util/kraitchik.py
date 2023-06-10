################################### INCLUDES ###################################

import utils

############################## PRIVATE FUNCTION ################################

# multiplie tout les elements d'un tableau
def _mult_in_tab(tab):
    res = 1
    for elt in tab:
        res *= elt
    return res

############################### PUBLIC FUNCTIONS ###############################

# Renvoie l'image par le polynome de Kraitchik
def polynome(x, n):
    return (x * x) - n

# Renvoie les facteur de n
def Kraitchik(n, suite_u, suite_v):
    u = _mult_in_tab(suite_u)
    v = utils.mult_in_dict(suite_v)
    facteurs = []
    facteurs.append(utils.pgcd((u - v), n))
    facteurs.append(utils.pgcd((u + v), n))
    return facteurs

################################################################################
