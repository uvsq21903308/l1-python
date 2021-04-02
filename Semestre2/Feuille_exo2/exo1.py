import tkinter as tk
import random as rd

HEIGHT, WIDTH = 400, 600

x, y = 300, 200
balle = []
demarrer = 0
rond = 0
id_after = 0


def start(b):
    global demarrer
    if demarrer == 0:
        demarrer = 1
        bt_start.configure(text="Arrêter")
        mouvement(b)
    elif demarrer == 1:
        demarrer = 0
        bt_start.configure(text="Démarrer")
        canvas.after_cancel(id_after)


def creer_balle():
    """Dessine un cercle, remplie, bleu au milieux du canvas et retourne
    une liste contenant les identifiant de la balles
    et deux entier choisit aléatoirement"""
    global rond
    rond = canvas.create_oval((x-10, y-10), (x+10, y+10), fill="blue")
    nb_al1 = rd.randint(1, 7)
    nb_al2 = rd.randint(1, 7)
    [rond, nb_al1, nb_al2]
    return [rond, nb_al1, nb_al2]


def mouvement(b):
    global id_after
    canvas.move(b[0], b[1], b[2])
    print(canvas.coords(balle[0]))
    id_after = canvas.after(50, lambda: mouvement(b))
    rebond2(b)


def rebond1(b):
    x0, y0, x1, y1 = canvas.coords(b[0])
    if x0 < 0 or x1 > 600:
        b[1] = -b[1]
    if y0 < 0 or y1 > 400:
        b[2] = -b[2]


def rebond2(b):
    x0, y0, x1, y1 = canvas.coords(b[0])
    if x0 < 0:
        canvas.itemconfigure(rond, x0+600, y0, x1, y1)
    if x1 > 600:
        canvas.itemconfigure(rond, x0, y0, x1-600, y1)
    if y0 < 0:
        canvas.itemconfigure(rond, x0, y0+600, x1, y1)
    if y1 > 400:
        canvas.itemconfigure(rond, x0, y0, x1, y1-600)


racine = tk.Tk()

canvas = tk.Canvas(racine, bg='black', height=HEIGHT, width=WIDTH)
bt_start = tk.Button(racine, text='Démarrer', command=lambda: start(balle))
canvas.grid(row=0, column=0)
bt_start.grid(row=1, column=0)

balle = creer_balle()
racine.mainloop()
