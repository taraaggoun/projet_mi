#!/usr/local/bin/python3

################################### INCLUDES ###################################

import re
import sys
import time

sys.path.insert(0, 'algorithmes/')
sys.path.insert(0, 'algorithmes/util/')

import utils
import Fermat
import generator
import Kraitchik
import MillerRabin
import DivisionsSuccessives

############################## PRIVATE FUNCTIONS ##############################

# Renvoie si la multiplication des facteurs est egale a n
def _is_good_factorisation(n, facteurs): 
    return utils.mult_in_dict(facteurs) == n

# Affiche les facteurs
def _print_facteurs(facteurs): 
    for key, value in facteurs.items(): 
        if(str(key)[0] != '-'):
            print("", end = ' ')
        print(str(key) + "^" + str(value))
# Aide
def _help():
    print("-" * 57)
    print("| Error: algorithm not found \t\t\t\t|")
    print("| Did you mean: \t\t\t\t\t|")
    print("|\t[ds] \t\t-> Divisions Successives \t|")
    print("|\t[fermat] \t-> Fermat \t\t\t|")
    print("|\t[kraitchik] \t-> Kraitchik \t\t\t|")
    print("-" * 57)
    sys.exit()

# Renvoie l'algorithme passer en parametre
def _get_algo(name): 
	name = name.lower()
	if name == "ds": 
		return DivisionsSuccessives
	if name == "fermat": 
		return Fermat
	if name == "kraitchik":
		return Kraitchik
	return _help()

# Verifie si n n'est pas 0 ou 1 et divise par -1 et 2 si nécessaire
def _divider_012(n):
	facteurs = {}
	if n == 0 or n == 1:
		return ({n: 1}, 1)
	if n < 0:
		n *= -1
		facteurs[-1] = 1
	while 1:
		if n % 2 == 1:
			break
		else:
			facteurs[2] = facteurs.get(2, 0) + 1
			n //= 2
	return (facteurs, n)

# Verifie si la chaine de caractere est un entier
def _is_integer(s):
    if s.isdigit():
        return True
    elif s[0] == '-' and s[1:].isdigit():
        return True
    elif re.match("^[-+]?[0-9]+$", s):
        return True
    else:
        return False

##################################### MAIN #####################################

def main(): 
	len_argv = len(sys.argv)
	if len_argv > 3 and len_argv < 1: 
		print("Error: Invalid number of arguments")
		print("Please enter:")
		print("\n\tpython3 Main.py [ *name of algo* ] [ *number* ]\n")
		return
	n = 0
	algo = DivisionsSuccessives # Par default
	if len_argv == 1:
		n = generator.generator()
		print("Le chiffre a factoriser est", n)
	if len_argv == 2:
		if not _is_integer(sys.argv[1]):	
			algo = _get_algo(sys.argv[1])
			n = generator.generator()
			print("Le chiffre a factoriser est", n)
		else:
			n = int(sys.argv[1])
	if len_argv == 3:
		if not _is_integer(sys.argv[2]):
			print("Error: argument 2 must be an integer")
			return
		n = int(sys.argv[2])
		algo = _get_algo(sys.argv[1])
  
	start_time = time.time()
	(facteurs, res) = _divider_012(n)
	if res != 1 and MillerRabin.is_prime(res):
		facteurs[res] = 1
	else:
		if res != 1:
			facteurs = utils.merge_dicts(facteurs, algo.all_divider(res))
		if len(facteurs) == 0: 
			print("Erreur: ")
			return
	print("------------ Factorisation ------------")
	_print_facteurs(facteurs)
	print("---------------- Stats ----------------")
	print("Temps: " + str(time.time() - start_time))
	print("Factorisation: " + str(_is_good_factorisation(n, facteurs)))

if __name__ == "__main__": 
    main()

################################################################################
