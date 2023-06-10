################################### INCLUDE ####################################

import math

############################### PUBLIC FUNCTIONS ###############################

# Fusionne deux dictionnaire
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        merged_dict[key] = merged_dict.get(key, 0) + value
    sorted_dict = dict(sorted(merged_dict.items()))
    return sorted_dict

# Renvoie la multiplication de tout les elements de dict
def mult_in_dict(dict):
	res = 1
	for key, value in dict.items(): 
		res *= pow(key, value)
	return res

# Affiche une matrice
def print_mat(mat): 
    for i in range (len(mat)):
        for j in range (len(mat[i])):
            print(str(mat[i][j]), end=" ")
        print()

# Renvoie la partie entiere inferieur de la racine carré
def isqrt(n):
    if n < 0:
        print("Error: isqrt defined for positif integer")
    if n == 0:
        return 0
    x = n
    y = (n + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

#Renvoie le pgcd de a et b
def pgcd(a, b):
    if b == 0:
        return a
    else:
        return pgcd(b, a % b)


# Renvoie quel B pour tester la B-friablialite
def find_b(n): 
	if n < 10: return 100
	res = math.log(n) * math.log(math.log(n))
	res = math.sqrt(res)
	res /= 2
	res = math.exp(res)
	return 100 if res < 100 else res

################################################################################
