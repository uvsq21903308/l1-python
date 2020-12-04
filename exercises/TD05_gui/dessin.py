import tkinter as tk
import random

# Affectation variable.
HEIGHT = 800
WIDTH = 800
couleur = ["blue"]
objet = []

# Affectation fonction.
def desCercle():
    """ Fonction qui dessine un cercle à une position aléatoire de Canvas"""
    x = random.randint(50, (WIDTH - 50))
    y = random.randint(50, (HEIGHT - 50))
    canvas.create_oval((x - 50), (y - 50), (x + 50), (y + 50), fill=couleur[0])
    objet.append(canvas.find_closest(x, y))
    return


def desCarre():
    """ Fonction qui dessine un carre à une position aléatoire de Canvas"""
    x = random.randint(50, (WIDTH - 50))
    y = random.randint(50, (HEIGHT - 50))
    canvas.create_rectangle((x - 50), (y - 50), (x + 50), (y + 50), fill=couleur[0])
    objet.append(canvas.find_closest(x, y))
    return


def desCroix():
    """ Fonction qui dessine une croix à une position aléatoire de Canvas"""
    x = random.randint(50, (WIDTH - 50))
    y = random.randint(50, (HEIGHT - 50))
    canvas.create_line((x - 50), (y - 50), (x + 50), (y + 50), fill=couleur[0])
    objet.append(canvas.find_closest(x, y))
    canvas.create_line((x - 50), (y + 50), (x + 50), (y - 50), fill=couleur[0])
    objet.append(canvas.find_closest(x, y))
    return


def demCouleur():
    """Fonction qui demande à l'utilisateur quel couleur soit-il utiliser pour son dessin"""
    couleur.clear()
    couleur.append(input("Rentrer la couleur qui vous convient."))
    return  


def undo():
    for i in range(int(len(objet))):
        canvas.delete(objet[i])
    return

# Affectation racine.
racine = tk.Tk()
racine.title("Mon dessin")

#Création fenêtre canvas:
canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid(column=1, row=1, rowspan=3, columnspan=2)

# Boutton choisir couleur:
choix_couleur = tk.Button(racine, text="Choisir une couleur", bg="tomato3", padx=10, pady=20, font=("30"), command=demCouleur)
choix_couleur.grid(column=1, row=0)

# Boutton undo:
choix_couleur = tk.Button(racine, text="Undo", bg="RosyBrown1", padx=10, pady=20, font=("30"), command=undo)
choix_couleur.grid(column=2, row=0)

# Boutton former un cercle:
but_cercle = tk.Button(racine, text="Cercle", padx=20, bg="Royalblue2", font=("30"), command=desCercle)
but_cercle.grid(column=0, row=1)

# Boutton former un carre:
but_carre = tk.Button(racine, text="Carré", padx=20, bg="orange", font=("30"), command=desCarre)
but_carre.grid(column=0, row=2)

# Boutton former un croix:
but_croix = tk.Button(racine, text="Croix", padx=20, bg="gold", font=("30"), command=desCroix)
but_croix.grid(column=0, row=3)

# Boucle Tkinter.
racine.mainloop()
