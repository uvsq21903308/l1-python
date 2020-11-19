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
    for i in range(2,n_max + 1):
        list_test = syracuse
        while list_test[-1] == 1:
            syracuse(i)
            list_test = syracuse
    x = True
    return x 
    
    


print(testeConjecture(10000))