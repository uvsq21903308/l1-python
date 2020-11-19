def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    liste_syracuse = []
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        liste_syracuse.append(n)
    return liste_syracuse        


# print(syracuse(3))

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    for i in range(3, n_max + 1):
        liste_syracuse = syracuse(i)
        if liste_syracuse[-1] == 1:
            x = True
        else:
            x = False
    return x
        

# print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    liste_syracuse = syracuse(n)
    y = len(liste_syracuse)
    return y


# print("Le temps de vol de", 3, "est", tempsVol(3))

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    t_vol = []
    for i in range(1, n_max + 1):
        t_vol.append(tempsVol(i))
    return t_vol



# print(tempsVolListe(100))

def tempsVolMax(n_max):
    """ Retourne le temps maximum parmis tout les temps de 1 à n_max """
    t_max = tempsVolListe(n_max)
    t_max.sort()
    z = t_max[-1]
    y = 0
    x = 0
    for i in range(1, n_max + 1):
        while z < y:
            liste = tempsVolListe(i)
            liste.sort()
            y = liste[-1]
            x += 1
    return x


print(tempsVolMax(10000))
