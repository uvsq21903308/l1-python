carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 7, 13]]


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    space = " "
    m_spc = max(carre[0])
    for k in range(4):
        r = max(carre[k])
        if r > m_spc:
            m_spc = r
    tot_spc = len(str(m_spc))

    for i in range(4):
        for j in range(4):
            x = carre[i][j]
            if len(str(x)) == tot_spc:
                print(x, end=" ")
            else:
                print(space * (tot_spc - len(str(x))) + str(x), end=" ")
        print()
    return


# afficheCarre(carre_mag)
# afficheCarre(carre_pas_mag)


def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si
        toutes les lignes ont la même somme, et -1 sinon """
    add = 0
    add1 = 0
    add2 = 0
    add3 = 0
    for i in range(4):
        add += carre[0][i]
    for i in range(4):
        add1 += carre[1][i]
    for i in range(4):
        add2 += carre[2][i]
    for i in range(4):
        add3 += carre[3][i]
    if add == add1 and add == add2 and add == add3:
        x = add
    else:
        x = -1
    return x


# print(testLignesEgales(carre_mag))
# print(testLignesEgales(carre_pas_mag))


def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si
        toutes les colonnes ont la même somme, et -1 sinon """
    add = 0
    add1 = 0
    add2 = 0
    add3 = 0
    for i in range(4):
        add += carre[i][0]
    for i in range(4):
        add1 += carre[i][1]
    for i in range(4):
        add2 += carre[i][2]
    for i in range(4):
        add3 += carre[i][3]
    if add == add1 and add == add2 and add == add3:
        x = add
    else:
        x = -1
    return x


# print(testColonnesEgales(carre_mag))
# print(testColonnesEgales(carre_pas_mag))


def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si
        les 2 diagonales ont la même somme, et -1 sinon """
    add = 0
    add1 = 0
    for i in range(4):
        add += carre[i][i]
    for j in range(4):
        add1 += carre[j][3-j]
    if add == add1:
        x = add
    else:
        x = -1
    return x


# print(testDiagonalesEgales(carre_mag))
# print(testDiagonalesEgales(carre_pas_mag))


def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    diagonales = testDiagonalesEgales(carre)
    colonnes = testColonnesEgales(carre)
    lignes = testLignesEgales(carre)
    if lignes == colonnes and lignes == diagonales:
        ret = True
    else:
        ret = False
    return ret


# print(estCarreMagique(carre_mag))
# print(estCarreMagique(carre_pas_mag))


def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2,
        où n est la taille du carré, et False sinon """
    n = len(carre[0])
    list_n = []
    ret = 0
    for i in range(1, (n ** 2)):
        list_n.append(i)
    for j in range(len(carre)):
        l_int = carre[j]
        for k in range(len(l_int)):
            valeur = l_int[k]
            if valeur in list_n:
                list_n.remove(valeur)
    if list_n == []:
        ret = True
    else:
        ret = False
    return ret


# print(estNormal(carre_mag))
# print(estNormal(carre_pas_mag))
