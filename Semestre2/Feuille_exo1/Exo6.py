import tkinter as tk

HEIGHT, WIDTH = 500, 500
couleur = ['black']


def changement_de_couleur(event):
    if 0 < event.x < 50 and 0 < event.y < 50:
        canvas.itemconfigure(cercle_c, fill='green')
        couleur.append('green')
    elif 50 < event.x < 100 and 0 < event.y < 50:
        canvas.itemconfigure(cercle_c, fill='yellow')
        couleur.append('yellow')
    elif 100 < event.x < 150 and 0 < event.y < 50:
        canvas.itemconfigure(cercle_c, fill='blue')
        couleur.append('blue')
    else:
        canvas.itemconfigure(cercle_c, fill='black')
        couleur.append('black')
    return


def comeback():
    canvas.itemconfigure(cercle_c, fill=couleur[-2])
    couleur.pop()
    return


racine = tk.Tk()

# Canvas:
canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=WIDTH)
canvas.grid(row=0, column=1)

# Button:
b_cancel = tk.Button(racine, text="Annuler", command=comeback)
b_cancel.grid(row=0, column=0)

# Carre:
carre_r = canvas.create_rectangle(0, 0, 50, 50, fill="green")
carre_b = canvas.create_rectangle(50, 0, 100, 50, fill="yellow")
carre_w = canvas.create_rectangle(100, 0, 150, 50, fill="blue")

# Cerle central
cercle_c = canvas.create_oval(
    WIDTH//2 - 50, HEIGHT//2 - 50, WIDTH//2 + 50, HEIGHT//2 + 50,
    fill='black')

# Changement de couleur
canvas.bind("<Button-1>", changement_de_couleur)

racine.mainloop()
