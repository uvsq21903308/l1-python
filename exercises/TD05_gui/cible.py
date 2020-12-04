import tkinter as tk

# Affectation variable.
HEIGHT, WIDTH = 500, 500

# Affectation racine.
racine = tk.Tk()
racine.title("Cible")

# Création canvas:
canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid(column=0, row=0)

# Création des cercles:

# Boucle tkinter.
racine.mainloop()