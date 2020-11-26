import tkinter as tk
import random

def desCercle():
    x0 = 500
    y0 = 500
    x1 = 500
    y1 =  500
    canvas.create_oval(x0, y0, x1, y1, fill="blue")
    return




racine = tk.Tk()
racine.title("Mon dessin")
canvas = tk.Canvas(racine, bg="black", bd=302, relief="flat")
choix_couleur = tk.Button(racine, text="Choisir une couleur", bg="tomato3", padx=10, pady=20, font=("30"))
cercle = tk.Button(racine, text="Cercle", padx=20, bg="Royalblue2", font=("30"), command=desCercle)
carre = tk.Button(racine, text="Carré", padx=20, bg="orange", font=("30"))
croix = tk.Button(racine, text="Croix", padx=20, bg="gold", font=("30"))

canvas.grid(column=1, row=1, rowspan=3)
choix_couleur.grid(column=1, row=0)
cercle.grid(column=0, row=1)
carre.grid(column=0, row=2)
croix.grid(column=0, row=3)

racine.mainloop()
