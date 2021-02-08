import tkinter as tk


def pixelclic(event):
    if event.x < HEIGHT//3 and len(cpt_croix) < 2:
        canvas.create_line((event.x - 50), (event.y - 50), (event.x + 50), (event.y + 50), fill="blue")
        canvas.create_line((event.x - 50), (event.y + 50), (event.x + 50), (event.y - 50), fill="blue")
        canvas.create_rectangle((event.x - 50), (event.y - 50), (event.x + 50), (event.y + 50), outline="blue")
        cpt_croix.append(1)
        cpt_carre.append(1)
    elif HEIGHT//3 < event.x < (HEIGHT//3)*2 and len(cpt_carre) < 3:
        canvas.create_rectangle((event.x - 50), (event.y - 50), (event.x + 50), (event.y + 50), fill="green")
        cpt_carre.append(1)
    elif (HEIGHT//3)*2 < event.x and len(cpt_cercle) < 3:
        canvas.create_oval((event.x - 50), (event.y - 50), (event.x + 50), (event.y + 50), fill="red")
        cpt_cercle.append(1)
    return


def recommencer():
    canvas.delete("all")
    cpt_carre.clear()
    cpt_cercle.clear()
    cpt_croix.clear()
    trait1 = canvas.create_line(HEIGHT//3, 0, HEIGHT//3, WIDTH, fill="white")
    trait2 = canvas.create_line((HEIGHT//3)*2, 0, (HEIGHT//3)*2, WIDTH, fill="white")
    return


HEIGHT, WIDTH = 500, 500
racine = tk.Tk()
cpt_croix = []
cpt_cercle = []
cpt_carre = []

canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
b_recommencer = tk.Button(racine, text="Redémarrer", command=recommencer)
trait1 = canvas.create_line(HEIGHT//3, 0, HEIGHT//3, WIDTH, fill="white")
trait2 = canvas.create_line((HEIGHT//3)*2, 0, (HEIGHT//3)*2, WIDTH, fill="white")
canvas.grid(column=0, row=0)
b_recommencer.grid(column=0, row=1)
canvas.bind("<Button-1>", pixelclic)

racine.mainloop()
