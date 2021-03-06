import tkinter as tk

HEIGHT, WIDTH = 500, 500
stop = [0]
cpt = [0]
racine = tk.Tk()


def modifCouleur(event):
    """Fonction qui permet de modifier là couleur du carré seulement si le curseur est sur celui si"""
    if (HEIGHT//2-50) < event.x < (HEIGHT//2+50) and (WIDTH//2-50) < event.y < (WIDTH//2+50) and stop[0] == 0:
        if cpt[0] == 1:
            canvas.itemconfigure(rectangle, fill="blue")
            cpt.clear()
            cpt.append(0)
        else:
            canvas.itemconfigure(rectangle, fill="red")
            cpt.clear()
            cpt.append(1)
    else:
        stop.clear()
        stop.append(1)
    return


def recommencer():
    """Fonction qui permet de réintilliser là couleur de rectangle et de pouvoir de nouveau changer sa couleur """
    canvas.itemconfigure(rectangle, fill="red")
    stop.clear()
    stop.append(0)
    return


canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
b_recommencer = tk.Button(racine, text="Recommencer", command=recommencer)
rectangle = canvas.create_rectangle(HEIGHT//2-50, WIDTH//2-50, HEIGHT//2+50, WIDTH//2+50, fill="red")
b_recommencer.grid(column=0, row=1)
canvas.grid(column=0, row=0)

canvas.bind("<Button-1>", modifCouleur)
racine.mainloop()
