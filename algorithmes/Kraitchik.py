################################### INCLUDES ###################################

import sys

sys.path.insert(0, 'util/')

import utils
import kraitchik
import resolution
import MillerRabin
import crible_eratosthene as ce
import crible_quadratique as cq

############################## PRIVATE FUNCTIONS ##############################

# Renvoie la matrice avec 
# sur les colonnes les x_k et sur les lignes les nb premiers
def _create_mat(x_k, primes):
	mat = []
	for prime in primes:
		line = []
		for value in x_k.values():
			if prime in value:
				if value[prime] % 2 != 0:
					line.append(1)
					continue
			line.append(0)
		mat.append(line)
	return mat

# Recupere les entier B-friable et la decomposition en facteur de leur carre
def _find_friables(n, primes, k):
	sqrt_n = utils.isqrt(n) + 1
	friables = []
	all_facteurs = {}
	cmp = 0
	i = 0
	while (cmp <= k):
		q_x = kraitchik.polynome(sqrt_n + i, n)
		(bool, facteurs) = cq.is_friable(q_x, primes)
		if bool == True:
			friables.append(sqrt_n + i)
			all_facteurs[sqrt_n + i] = facteurs
			cmp += 1
		i += 1
	return (friables, all_facteurs)

# Prend v au carre et renvoie v
def _sqrt_v(v2):
	v = {}
	for elt in v2:
		for key, value in elt.items():
			v[key] = v.get(key, 0) + value
	for key in v.keys():
		v[key] //= 2
	return v

# Trouve 2 diviseur de n
def _find_2_divider(n, primes, k):
	(x_k, q_x_k) = _find_friables(n, primes, k)
	mat = _create_mat(q_x_k, primes)
	sols = resolution.resolution(mat)
	(fct1, fct2) = (1, 1)
	for sol in sols:
		u = []
		v2 = []
		for i in range(len(sol)):
			if sol[i] == 1:
				u.append(x_k[i])
				v2.append(q_x_k[x_k[i]])
		v = _sqrt_v(v2)
		(fct1, fct2) = kraitchik.Kraitchik(n, u, v)
		if (fct1 != 1 and fct1 != n) or (fct2 != 1 and fct2 != n):
			break
	fct1 = 1 if fct1 == 1 or fct1 == n else fct1
	fct2 = 1 if fct2 == 1 or fct2 == n else fct2
	return (fct1, fct2)

# Trouve deux diviseur non triviaux de n
def _divider(n):
	b = utils.find_b(n)
	primes = ce.eratosthene(b)
	k = len(primes) + 1
	(fct1, fct2) = (1, 1)
	while(1):
		(fct1, fct2) = _find_2_divider(n, primes, k)
		if fct1 != 1 or fct2 != 1:
			break
		k += 1
	return (fct1, fct2)	
  

############################### PUBLIC FUNCTION ################################

# Trouve tout les diviseurs de n sous forme d un dictionnaire
def all_divider(n, facteurs={}):
	(fct1, fct2) = _divider(n)
	if fct1 != 1:
		if MillerRabin.is_prime(fct1):
			facteurs[fct1] = facteurs.get(fct1, 0) + 1
		else :
			facteurs = all_divider(fct1, facteurs)
		if MillerRabin.is_prime(n // fct1):
			facteurs[n // fct1] = facteurs.get(n // fct1, 0) + 1
		else :
			facteurs = all_divider(n // fct1, facteurs)
	elif fct2 != 1:
		if MillerRabin.is_prime(fct2):
			facteurs[fct2] = facteurs.get(fct2, 0) + 1
		else :
			facteurs = all_divider(fct2, facteurs)
		if MillerRabin.is_prime(n // fct2):
			facteurs[n // fct2] = facteurs.get(n // fct2, 0) + 1
		else :
			facteurs = all_divider(n // fct2, facteurs)
	return facteurs

################################################################################
