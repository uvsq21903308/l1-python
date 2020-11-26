import tkinter as tk

racine = tk.Tk()
racine.title("Mon dessin")
canvas = tk.Canvas(racine, bg="black")
choix_couleur = tk.Button(racine, text="Choisir une couleur")
cercle = tk.Button(racine, text="Cercle")
carre = tk.Button(racine, text="Carré")
croix = tk.Button(racine, text="Croix")

canvas.grid(column=1, row=1, rowspan=3)
choix_couleur.grid(column=1, row=0)
cercle.grid(column=0, row=1)
carre.grid(column=0, row=2)
croix.grid(column=0, row=3)

racine.mainloop()
