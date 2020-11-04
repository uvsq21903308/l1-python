
def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    temps = temps[0] * 86400 + temps[1] * 3600 + temps[2] * 60 + temps[3]
    return temps

#temps = (3,23,1,34)
#print(type(temps))
#print(tempsEnSeconde(temps))  


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    temps = []
    jour_seconde = seconde // 86400 
    temps.append(jour_seconde)
    heure_seconde = (seconde - jour_seconde * 86400) // 3600
    temps.append(heure_seconde)
    minute_seconde = (seconde - (jour_seconde * 86400 + heure_seconde * 3600)) // 60
    temps.append(minute_seconde)
    reste = seconde - (jour_seconde * 86400 + heure_seconde * 3600 + minute_seconde * 60)
    temps.append(reste)
    return temps


#temps = secondeEnTemps(100000)
#print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")


#fonction auxiliaire ici

def afficheTemps(temps):
    """Renvoie un affichage du nombre de jours, heure, minutes et seconde avec la bonne syntaxe"""
    #Jours
    if temps[0] > 1:
        print(temps[0], "jours", end=" ")
    elif temps[0] == 1:
        print(temps[0], "jour", end=" ")
    #Heures
    if temps[1] > 1:
        print(temps[1], "heures", end=" ")
    elif temps[1] == 1:
        print(temps[1], "heure", end=" ")
    #Minutes
    if temps[2] > 1:
        print(temps[2], "minutes", end=" ")
    elif temps[2] == 1:
        print(temps[2], "minute", end=" ")
    #Secondes
    if temps[3] > 1:
        print(temps[3], "secondes", end=" ")
    elif temps[3] == 1:
        print(temps[3], "seconde", end=" ")
    print()
    return
    
#afficheTemps((1,0,14,23)) 

#Fonction pour rentrer un temps par l'utilisateur
def demandeTemps():
    """Renvoie les jours, heures, minutes et secondes que l'utilisateur à rentrer en vérifiant que ce soit les bonnes"""
    temps = []
    #Jour
    jour = int(input("Rentrer une valeur à jour!"))
    temps.append(jour)
    #Heure
    heure = int(input("Rentrer une valeur à heure!"))
    if heure > 23:
        temps.pop(0)
        print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
        jour = int(input("Rentrer une valeur à jour"))
        temps.append(jour)
        print("Modifier maintenant votre valeur d'heure.")
        heure = int(input("Rentrer une valeur à heure!"))
    temps.append(heure)
    #Minute
    minute = int(input("Rentrer une valeur à minute!"))
    if minute > 59 and minute < 1439 :
        temps.pop(1)
        print("Ce nombre est trop élevé!""\n""Modifier votre valeur de heure.")
        heure = int(input("Rentrer une valeur à heure!"))
        if heure > 23:
            temps.pop(0)
            print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
            jour = int(input("Rentrer une valeur à jour"))
            temps.append(jour)
            print("Modifier maintenant votre valeur d'heure.")
            heure = int(input("Rentrer une valeur à heure!"))
        temps.append(heure)
        print("Modifier maintenant votre valeur d'heure.")
        minute = int(input("Rentrer une valeur à heure!"))
    elif minute > 1439 :
        temps.pop(0)
        print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
        jour = int(input("Rentrer une valeur à jour!"))
        temps.append(jour)
        print("Modifier maintenant votre valeur d'heure et de minute.")
        temps.pop(1)
        heure = int(input("Rentrer une valeur à heure!"))
        if heure > 23:
            temps.pop(0)
            print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
            jour = int(input("Rentrer une valeur à jour"))
            temps.append(jour)
            print("Modifier maintenant votre valeur d'heure.")
            heure = int(input("Rentrer une valeur à heure!"))
        temps.append(heure)
        minute = int(input("Rentrer une valeur à minute!"))
    temps.append(minute)
    #Seconde
    secondes = int(input("Rentrer une valeur à seconde!"))
    if secondes > 59 and secondes < 3599 :
        temps.pop(2)
        print("Ce nombre est trop élevé!""\n""Modifier votre valeur de minute.")
        minute = int(input("Rentrer une valeur à minute"))
        if minute > 59 and minute < 1439 :
            temps.pop(1)
            print("Ce nombre est trop élevé!""\n""Modifier votre valeur de heure.")
            heure = int(input("Rentrer une valeur à heure!"))
            if heure > 23:
                temps.pop(0)
                print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
                jour = int(input("Rentrer une valeur à jour"))
                temps.append(jour)
                print("Modifier maintenant votre valeur d'heure.")
                heure = int(input("Rentrer une valeur à heure!"))
            temps.append(heure)
            print("Modifier maintenant votre valeur d'minute.")
            minute = int(input("Rentrer une valeur à minute!"))
        elif minute > 1439 :
            temps.pop(0)
            print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
            jour = int(input("Rentrer une valeur à jour!"))
            temps.append(jour)
            print("Modifier maintenant votre valeur d'heure et de minute.")
            temps.pop(1)
            heure = int(input("Rentrer une valeur à heure!"))
            if heure > 23:
                temps.pop(0)
                print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
                jour = int(input("Rentrer une valeur à jour"))
                temps.append(jour)
                print("Modifier maintenant votre valeur d'heure.")
                heure = int(input("Rentrer une valeur à heure!"))
            temps.append(heure)
        minute = int(input("Rentrer une valeur à minute!"))
        temps.append(minute)
        print("Modifier maintenant votre valeur de seconde.")
        secondes = int(input("Rentrer une valeur à seconde!"))
    elif secondes > 3599 and secondes < 86399 :
        temps.pop(1)
        print("Ce nombre est trop élevé!""\n""Modifier votre valeur d'heure.")
        heure = int(input("Rentrer une valeur à heure"))
        if heure > 23:
            temps.pop(0)
            print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
            jour = int(input("Rentrer une valeur à jour"))
            temps.append(jour)
            print("Modifier maintenant votre valeur d'heure.")
            heure = int(input("Rentrer une valeur à heure!"))
        temps.append(heure)
        print("Modifier maintenant votre valeur de minute et de seconde.")
        temps.pop(2)
        minute = int(input("Rentrer une valeur à minute!"))
        if minute > 59 and minute < 1439 :
            temps.pop(1)
            print("Ce nombre est trop élevé!""\n""Modifier votre valeur de heure.")
            heure = int(input("Rentrer une valeur à heure!"))
            if heure > 23:
                temps.pop(0)
                print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
                jour = int(input("Rentrer une valeur à jour"))
                temps.append(jour)
                print("Modifier maintenant votre valeur d'heure.")
                heure = int(input("Rentrer une valeur à heure!"))
            temps.append(heure)
            print("Modifier maintenant votre valeur d'heure.")
            minute = int(input("Rentrer une valeur à heure!"))
        elif minute > 1439 :
            temps.pop(0)
            print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
            jour = int(input("Rentrer une valeur à jour!"))
            temps.append(jour)
            print("Modifier maintenant votre valeur d'heure et de minute.")
            temps.pop(1)
            heure = int(input("Rentrer une valeur à heure!"))
            if heure > 23:
                temps.pop(0)
                print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
                jour = int(input("Rentrer une valeur à jour"))
                temps.append(jour)
                print("Modifier maintenant votre valeur d'heure.")
                heure = int(input("Rentrer une valeur à heure!"))
            temps.append(heure)
            minute = int(input("Rentrer une valeur à minute!"))
        temps.append(minute)
        secondes = int(input("Rentrer une valeur à secondes!"))
    elif secondes > 86399:
        print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
        temps.pop(0)
        jour = int(input("Rentrer une valeur à jour!"))
        temps.append(jour)
        print("Modifier maintenant votre valeur d'heure et de minute, de seconde.")
        temps.pop(1)
        heure = int(input("Rentrer une valeur à heure"))
        if heure > 23:
            temps.pop(0)
            print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
            jour = int(input("Rentrer une valeur à jour"))
            temps.append(jour)
            print("Modifier maintenant votre valeur d'heure.")
            heure = int(input("Rentrer une valeur à heure!"))
        temps.append(heure)
        minute = int(input("Rentrer une valeur à minute!"))
        if minute > 59 and minute < 1439 :
            temps.pop(1)
            print("Ce nombre est trop élevé!""\n""Modifier votre valeur de heure.")
            heure = int(input("Rentrer une valeur à heure!"))
            if heure > 23:
                temps.pop(0)
                print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
                jour = int(input("Rentrer une valeur à jour"))
                temps.append(jour)
                print("Modifier maintenant votre valeur d'heure.")
                heure = int(input("Rentrer une valeur à heure!"))
            temps.append(heure)
            print("Modifier maintenant votre valeur d'heure.")
            minute = int(input("Rentrer une valeur à heure!"))
        elif minute > 1439 :
            temps.pop(0)
            print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
            jour = int(input("Rentrer une valeur à jour!"))
            temps.append(jour)
            print("Modifier maintenant votre valeur d'heure et de minute.")
            temps.pop(1)
            heure = int(input("Rentrer une valeur à heure!"))
            if heure > 23:
                temps.pop(0)
                print("Ce nombre est trop élevé!""\n""Modifier votre valeur de jour.")
                jour = int(input("Rentrer une valeur à jour"))
                temps.append(jour)
                print("Modifier maintenant votre valeur d'heure.")
                heure = int(input("Rentrer une valeur à heure!"))
            temps.append(heure)
            minute = int(input("Rentrer une valeur à minute!"))
        temps.append(minute)
        secondes = int(input("Rentrer une valeur à secondes!"))
    temps.append(secondes)
    return temps

#afficheTemps(demandeTemps())

def sommeTemps(temps1,temps2):
    temps1 = tempsEnSeconde(temps1)
    temps2 = tempsEnSeconde(temps2)
    adtemps = temps1 + temps2
    adtemps = secondeEnTemps(adtemps)
    afficheTemps(adtemps)
    return


#sommeTemps((2,3,4,25),(5,22,57,1))

def proportionTemps(temps,proportion):
    temps =  tempsEnSeconde(temps)
    x = temps * proportion
    x = secondeEnTemps(x)
    return x

afficheTemps(proportionTemps(proportion = 0.2, temps = (2,4,36,0)))
