############################## PRIVATE FUNCTIONS ##############################

# Ajoute deux lignes dans F2
def _xor_lines(line1, line2):
    if len(line1) != len(line2):
        print("Erreur: les lignes n'ont pas la meme taille")
        exit(1)
    res = []
    for i in range (len(line1)):
        res.append(line1[i] ^ line2[i])
    return res

# Echange les lignes i et j dans des matrice
def _switch_lines(mat, i, j): 
    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat) or i == j: 
        print("Erreur: mauvais indices dans l'echange de lignes")
        exit(1)

    line_tmp = mat[i]
    mat[i] = mat[j]
    mat[j] = line_tmp

    return mat

############################### PUBLIC FUNCTION ################################

# Pivot de gauss
def pivot_de_gauss(mat):
    for i in range (len(mat)):
        if mat[i][i] != 1:
            for j in range (i + 1, len(mat)):
                if mat[j][i] == 1:
                    _switch_lines(mat, i, j)
                    break
        for j in range (len(mat)):
            if i == j:
                continue
            if mat[j][i] == 1:
                mat[j] = _xor_lines(mat[i], mat[j])
    return mat

################################################################################
