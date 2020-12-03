import tkinter as tk
import random

HEIGHT = 300
WIDTH = 300

def desCercle():
    """ Fonction qui dessine un cercle à une position aléatoire de Canvas"""
    canvas.create_oval((100, 100), (300, 300), fill="blue") 


def desCarre():
    
    return


def desCroix():
    return


racine = tk.Tk()
racine.title("Mon dessin")

#Création fenêtre canvas:
canvas = tk.Canvas(racine, bg="black", bd=302, relief="flat", height=HEIGHT, width=WIDTH)
canvas.grid(column=1, row=1, rowspan=3)

# Boutton choisir couleur:
choix_couleur = tk.Button(racine, text="Choisir une couleur", bg="tomato3", padx=10, pady=20, font=("30"))
choix_couleur.grid(column=1, row=0)

# Boutton former un cercle:
cercle = tk.Button(racine, text="Cercle", padx=20, bg="Royalblue2", font=("30"), command=desCercle)
canvas.create_oval((50, 50), (150, 150), fill="blue") 
cercle.grid(column=0, row=1)

# Boutton former un carre:
carre = tk.Button(racine, text="Carré", padx=20, bg="orange", font=("30"), command=desCarre)
carre.grid(column=0, row=2)

# Boutton former un croix:
croix = tk.Button(racine, text="Croix", padx=20, bg="gold", font=("30"), command=desCroix)
croix.grid(column=0, row=3)

# Boucle Tkinter.
racine.mainloop()
