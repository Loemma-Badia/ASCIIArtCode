#### Imports et définition des variables globales

# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)

#### Fonctions secondaires

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici
    LA=[]
    occ=1
    for letter in range(1,len(s)):
        if s[letter]==s[letter-1]:
            occ+=1
        else:
            LA.append((s[letter-1],occ))
            occ=1
    LA.append((s[::len(s)],occ))
    return LA

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    
    # votre code ici
    # cas de base
    if s=='':
        return []

    # recherche nombre de caractères identiques au premier

    ref = s[0]
    i= 1
    while i < len(s) and s[i] == ref:
        i+=1

    return [(ref, i)] + artcode_r(s[i:])

#### Fonction principale

def main():
    print(artcode_i('gggfhhhhhhggg'))
    print(artcode_r('~~~~~@@@---@@@~~~~~'))
#[('g', 3), ('f', 1), ('h', 6), ('g', 3)]
#[('~', 5), ('@', 3), ('-', 3), ('@', 3), ('~', 5)]

if __name__ == "__main__":
    main()
