import tkinter as tk
import random

# Affectation variable.
HEIGHT = 256
WIDTH = 256

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_pixel(i, j, color):
    pixel = canvas.create_line(i, j, i + 1, j, fill=color)

def ecran_aleatoire():
    for i in range(256):
        for j in range(256):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            draw_pixel(i, j, get_color(r, g, b))


def degrade_gris():
    for i in range(256):
        for j in range(256):
            draw_pixel(i, j, get_color(i, i, i))


def degrade_2D():
    for i in range(256):
        for j in range(256):
            draw_pixel(i, j, get_color(i, 1, j))


# Affectation racine.
racine = tk.Tk()
racine.title("Mon dessin")

#Création fenêtre canvas:
canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid(column=1, row=1, rowspan=3)

# Boutton renvoie à la focntion ecran_aleatoire:
b_ale = tk.Button(racine, text="Aléatoire", fg="blue", command=ecran_aleatoire)
b_ale.grid(column=0, row=1)

# Boutton renvoie à la focntion degrade_gris:
b_gris = tk.Button(racine, text="Dégragé gris", fg="blue", command=degrade_gris)
b_gris.grid(column=0, row=2)

# Boutton renvoie à la fonction degrade_2D:
but_croix = tk.Button(racine, text="Dégradé 2D", fg="blue", command=degrade_2D)
but_croix.grid(column=0, row=3)

# Boucle Tkinter.
racine.mainloop()
