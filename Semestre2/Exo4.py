import tkinter as tk


def modifCarre():
    if cpt < 2:
    elif cpt >
    pass


def pause():
    pass


HEIGHT, WIDTH = 500, 500

racine = tk.Tk()

canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=WIDTH)
b_pause = tk.Button(racine, text="Pause", command=pause)
carre = canvas.create_rectangle(
    (HEIGHT//2)-50, (WIDTH//2)-50, (HEIGHT//2)+50, (WIDTH//2)+50,
    fill="red")
b_pause.grid(column=0, row=1)
canvas.grid(column=0, row=0)
# canvas.bind("<Button-1>", dessinClic)

racine.mainloop()
