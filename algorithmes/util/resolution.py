################################### INCLUDE ####################################

import pivot_de_gauss as pdg

############################## PRIVATE FUNCTIONS ###############################

# Calcule la transposé de la matrice
def _transpose(mat):
	nb_col = len(mat[0])
	nb_line = len(mat)
	transpose = [[0 for j in range(nb_line)] for i in range(nb_col)]
	for i in range(nb_line):
		for j in range(nb_col):
			transpose[j][i] = mat[i][j]
	return transpose

# Enleve l'identité de la matrice
def _remove_id(mat):
	nb_line = len(mat)
	res = []
	for i in range(nb_line):
		res.append(mat[i][nb_line :])
	return res

# Ajoute l'identité a la matrice
def _add_id(mat):
	nb_col = len(mat[0])
	nb_lin = len(mat)
	for i in range(nb_col):
		mat.append([])
		for j in range(nb_col):
			if j == i:
				mat[nb_lin + i].append(1)
			else:
				mat[nb_lin + i].append(0)
	return mat

# Verifie si il y a une colonne vide
def _is_col_zero(mat):
	for i in range(len(mat[0])):
		for j in range(len(mat)):
			if mat[j][i] == 1:
				break
		if j == len(mat) - 1 and mat[j][i] == 0:
				return (True, i)
	return (False, 0)

# Supprime la colonne i de la matrice
def _remove_col(mat, id):
    res = []
    for i in range(len(mat)):
        line = []
        for j in range(len(mat[0])):
            if j != id:
                line.append(mat[i][j])
        res.append(line)
    return res 

# Retourne le vecteur qui vaut 1 a index et 0 sinon
def _get_line(index, len):
	res = []
	for i in range(len):
		if index == i:
			res.append(1)
		else:
			res.append(0)
	return [res]

# Ajoute les colonne vide
def _add_col_vide(mat, col_vide): 
	if col_vide == []:
		return _transpose(mat)

	for i in range(len(mat)):
		for num_col in col_vide:
			beg = mat[i][:num_col]
			end = mat[i][num_col:]
			mat[i] = beg + [0] + end

	res = []
	for num_col in col_vide:
		beg = mat[:num_col]
		end = mat[num_col:]
		res = beg + _get_line(num_col, len(mat[0])) + end

	return _transpose(res)

############################### PUBLIC FUNCTION ################################

# Trouve les solution du systeme
def resolution(mat):
	res = []
	mat = pdg.pivot_de_gauss(mat)
	(bol, num_col) = _is_col_zero(mat)
	col_vide = []
	while (bol == True):
		col_vide.append(num_col)
		mat = _remove_col(mat, num_col)
		(bol, num_col) = _is_col_zero(mat)
	mat = _remove_id(mat)
	mat = _add_id(mat)
	return _add_col_vide(mat, col_vide)

################################################################################
