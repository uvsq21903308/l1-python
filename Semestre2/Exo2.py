import tkinter as tk

HEIGHT, WIDTH = 500, 500
cpt = [1]
pos = []
verif = [1]
stop = [0]


def pause():
    """Fonction qui permet de mettre en pause le programme"""
    if stop[0] == 0:
        b_pause.config(text="Restart")
        stop.clear()
        stop.append(1)
    elif stop[0] == 1:
        b_pause.config(text="Pause")
        stop.clear()
        stop.append(0)
    return


def dessinClic(event):
    if stop[0] == 0 and verif[0] == 1:
        if not pos:
            pos.append(event.x)
            pos.append(event.y)
        elif cpt[0] == 1:
            canvas.create_line(
                pos[0], pos[1], event.x, event.y,
                fill='blue')
            pos.clear()
            cpt.clear()
            cpt.append(0)
        elif cpt[0] != 1:
            canvas.create_line(
                pos[0], pos[1], event.x, event.y,
                fill='red')
            pos.clear()
            cpt.clear()
            cpt.append(1)
            verif.clear()
            verif.append(0)
    elif stop[0] == 0:
        verif.clear()
        verif.append(1)
        canvas.delete("all")
    return



racine = tk.Tk()

canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=WIDTH)
b_pause = tk.Button(racine, text="Pause", command=pause)
b_pause.grid(column=0, row=1)
canvas.grid(column=0, row=0)

canvas.bind("<Button-1>", dessinClic)

racine.mainloop()
