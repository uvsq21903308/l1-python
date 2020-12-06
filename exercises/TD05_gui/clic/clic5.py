import tkinter as tk

def cercle(event):
    if len(prec) < 9:
        oval.append(canvas.create_oval(event.x, event.y, event.x + 100, event.y + 100, fill="red"))
        prec.append(1)
    elif len(prec) == 9:
        for i in range(8):
            canvas.itemconfigure(oval[i], fill="yellow")
        prec.append(1)
    elif len(prec) == 10:
        for i in range(8):
            canvas.delete(oval[i])
        for j in range(9):
            prec.remove(1)
        oval.clear()
    return


HEIGHT, WIDTH = 500, 500
x = 250
prec = [1]
oval = []
racine = tk.Tk()

canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid()
canvas.bind("<Button-1>", cercle)
racine.mainloop()