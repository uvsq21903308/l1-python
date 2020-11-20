carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [12, 2, 3, 13]]
carre_pas_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [12, 2, 7, 13]]


def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    space = " "
    for k in range(4):
        m_spc = max(carre[0])
        r = max(carre[k])
        if r > m_spc:
            m_spc = r
    tot_spc = len(str(m_spc))

    for i in range(4):
        for j in range(4):
            if len(str(carre[i][j])) == tot_spc:
                print(carre[i][j], end=" ")
            else:
                print(space * int((len(str(carre[i][j])) - tot_spc)) + str(carre[i][j]), end=" "))
        print()
    return
    

print(afficheCarre(carre_mag))
# afficheCarre(carre_pas_mag)