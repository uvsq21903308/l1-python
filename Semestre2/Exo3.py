import tkinter as tk


def recommencer():
    pass


HEIGHT, WIDTH = 500, 500
racine = tk.Tk()

canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
b_recommencer = tk.Button(racine, text="Redémarrer", command=recommencer)
trait1 = canvas.create_line(HEIGHT//3, 0, HEIGHT//3, WIDTH, fill="white")
trait2 = canvas.create_line((HEIGHT//3)*2, 0, (HEIGHT//3)*2, WIDTH, fill="white")
canvas.grid(column=0, row=0)

racine.mainloop()
