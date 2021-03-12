import tkinter as tk

HEIGHT, WIDTH = 500, 500

x0 = (HEIGHT//2)-25
y0 = (WIDTH//2)-25
x1 = (HEIGHT//2)+25
y1 = (WIDTH//2)+25
stop = 0

def dessiner(x0, x1, y0, y1):
    canvas.create_rectangle(x0, y0, x1, y1, fill="red")
    return


def suivant(event, x0, x1, y0, y1):
    if x0 < event.x < x1 and y0 < event.y < y1 and x1-x0 > 20:
        x0 = (x0+5)
        x1 = (x1-5)
        y0 = (y0+5)
        y1 = (y1-5)
    elif y1-y0 < 100 and (0 < event.x < x0 or x1 < event.x < 500 or 0 < event.y < y0 or y1 < event.y < 500):
        x0 = (x0-5)
        x1 = (x1+5)
        y0 = (y0-5)
        y1 = (y1+5)
    return (x0, x1, y0, y1)


def pause():
    return stop == 0


racine = tk.Tk()

canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=WIDTH)
b_pause = tk.Button(racine, text="Pause", command=pause)
b_pause.grid(column=0, row=1)
canvas.grid(column=0, row=0)

canvas.bind("<Button-1>", suivant)

while pause():
    dessiner()

racine.mainloop()
