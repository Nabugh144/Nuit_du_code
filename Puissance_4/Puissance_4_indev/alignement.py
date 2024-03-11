grille = [
    [None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None],
    [None, None, None, "j" , None,  "r", None],
    [None, None,  "r", "j" , "r" , None, None],
    [None, None,  "r", "r" , "j" , None, None],
    [None, "j" ,  "r", "j" , "j" , "j" , None]]


# fonction qui détermine si il y a un alignement de 4 pions
def detection_alignement(grille, joueur):
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j] == joueur:
                if (detection_ligne(grille, joueur, i, j) or
                   detection_colonne(grille, joueur, i, j) or
                   detection_diago1(grille, joueur, i, j) or
                   detection_diago2(grille, joueur, i, j)):
                    return True
    return False


# fonction qui détecte les lignes
def detection_ligne(grille, joueur, i, j):
    for _ in range(3):
        i += 0
        j += 1
        if not (i < len(grille) and j < len(grille[0]) and grille[i][j] == joueur):
            return False
    return True

# fonction qui détecte les colonnes
def detection_colonne(grille, joueur, i, j):
    for _ in range(3):
        i += 1
        j += 0
        if not (i < len(grille) and j < len(grille[0]) and grille[i][j] == joueur):
            return False
    return True

# fonctions qui détecte les diagonales
def detection_diago1(grille, joueur, i, j):
    for _ in range(3):
        i += 1
        j += 1
        if not (0 <= i < len(grille) and 0 <= j < len(grille[0]) and grille[i][j] == joueur):
            return False
    return True

def detection_diago2(grille, joueur, i, j):
    for _ in range(3):
        i += -1
        j += 1
        if not (0 <= i < len(grille) and 0 <= j < len(grille[0]) and grille[i][j] == joueur):
            return False
    return True


if detection_alignement(grille, "r"):
    print("le joueur rouge à gagné")
    
if detection_alignement(grille, "j"):
    print("le joueur jaune à gagné")