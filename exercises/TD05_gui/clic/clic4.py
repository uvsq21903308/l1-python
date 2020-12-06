import tkinter as tk

def vide(convas):
    if prec[-1] == 1:
        canvas.itemconfigure(carre, fill="black")
        prec.append(2)
    else:
        canvas.itemconfigure(carre, fill="blue")
        prec.append(1)
    if len(prec) == 11:
        racine.destroy()
    return

HEIGHT, WIDTH = 500, 500
x = 250
prec = [1]
racine = tk.Tk()

canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid()
carre = canvas.create_rectangle(HEIGHT // 4, HEIGHT // 4, HEIGHT // 4 * 3, HEIGHT // 4 * 3, fill="blue", outline="white")
# Scanvas.bind("<Button-1>", vide)
canvas.bind("<Button-1>", vide)
racine.mainloop()