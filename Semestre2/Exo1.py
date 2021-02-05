import tkinter as tk


def modifCouleur(event):
    if cpt[0] == 1:
        canvas.itemconfigure(rectangle, fill="blue")
        cpt.clear()
        cpt.append(0)
    else:
        canvas.itemconfigure(rectangle, fill="red")
        cpt.clear()
        cpt.append(1)
    return


def recommencer():
    canvas.itemconfigure(rectangle, fill="red")
    return

HEIGHT, WIDTH = 500, 500
cpt = [0]
racine = tk.Tk()

canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
b_recommencer = tk.Button(racine, text="Recommencer", command=recommencer)
rectangle = canvas.create_rectangle(HEIGHT//2-50, WIDTH//2-50, HEIGHT//2+50, WIDTH//2+50, fill="red")
b_recommencer.grid(column=0, row=1)
canvas.grid(column=0, row=0)

canvas.bind("<Button-1>", modifCouleur)
racine.mainloop()