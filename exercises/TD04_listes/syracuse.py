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
        

print(testeConjecture(10000))