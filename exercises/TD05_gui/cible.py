import tkinter as tk

# Affectation variable.
HEIGHT, WIDTH = 500, 500
x = 10
couleur = ["blue", "green", "black", "yellow", "magenta", "red"]

# Affectation racine.
racine = tk.Tk()
racine.title("Cible")

# Création canvas:
canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid(column=0, row=0)

# Création des cercles:
for i in range((HEIGHT // 2) // x):
    x0, y0= (i * x), (i * x)
    x1, y1= (HEIGHT - i * x), (HEIGHT - i * x)
    canvas.create_oval(x0, y0, x1, y1, outline=couleur[i % 6], width = x)

# Boucle tkinter.
racine.mainloop()