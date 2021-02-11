import tkinter as tk

HEIGHT, WIDTH = 500, 500
x0 = [(HEIGHT//2)-50]
y0 = [(WIDTH//2)-50]
x1 = [(HEIGHT//2)+50]
y1 = [(WIDTH//2)+50]
stop = [0]


def modifCarre(event):
    if (HEIGHT//2)-50 < event.x < (HEIGHT//2)+50 and (WIDTH//2)-50 < event.x < (WIDTH//2)+50 and stop[0] == 0:
        x0.append(x0[0]-10)
        x0.pop(0)
        x1.append(x1[0]-10)
        x0.pop(0)
        y0.append(y0[0]-10)
        x0.pop(0)
        y1.append(y1[0]-10)
        x0.pop(0)
        canvas.coords(carre, x0, y0, x1, y1)
    elif (HEIGHT//2)-50 > event.x > (HEIGHT//2)+50 and (WIDTH//2)-50 > event.x > (WIDTH//2)+50 and stop[0] == 0:
        x0.append(x0[0]+10)
        x0.pop(0)
        x1.append(x1[0]+10)
        x0.pop(0)
        y0.append(y0[0]+10)
        x0.pop(0)
        y1.append(y1[0]+10)
        x0.pop(0)
        canvas.coords(carre, x0, y0, x1, y1)
    pass


def pause():
    if stop[0] == 0:
        stop.clear()
        stop.append(1)
    else:
        stop.clear()
        stop.append(0)
    return


racine = tk.Tk()

canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=WIDTH)
b_pause = tk.Button(racine, text="Pause", command=pause)
carre = canvas.create_rectangle(
    x0, y0, x1, y1,
    fill="red")
b_pause.grid(column=0, row=1)
canvas.grid(column=0, row=0)
canvas.bind("<Button-1>", modifCarre)

racine.mainloop()
