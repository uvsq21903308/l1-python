import tkinter as tk

HEIGHT, WIDTH = 600, 600
color = [0]


def changPos(event):
    if event.x < HEIGHT//3:
        canvas.move(line1, (-10), 0)
        canvas.move(line2, (-10), 0)
        if color[0] == 0:
            canvas.itemconfigure(line1, fill="blue")
            canvas.itemconfigure(line2, fill="red")
            color.clear()
            color.append(1)
        else:
            canvas.itemconfigure(line1, fill="red")
            canvas.itemconfigure(line2, fill="blue")
            color.clear()
            color.append(0)
    elif HEIGHT//3 < event.x < (HEIGHT//3)*2:
        canvas.move(line1, (+10), 0)
        canvas.move(line2, (-10), 0)
        if color[0] == 0:
            canvas.itemconfigure(line1, fill="blue")
            canvas.itemconfigure(line2, fill="red")
            color.clear()
            color.append(1)
        else:
            canvas.itemconfigure(line1, fill="red")
            canvas.itemconfigure(line2, fill="blue")
            color.clear()
            color.append(0)
    elif (HEIGHT//3)*2 < event.x:
        canvas.move(line1, (+10), 0)
        canvas.move(line2, (+10), 0)
        if color[0] == 0:
            canvas.itemconfigure(line1, fill="blue")
            canvas.itemconfigure(line2, fill="red")
            color.clear()
            color.append(1)
        else:
            canvas.itemconfigure(line1, fill="red")
            canvas.itemconfigure(line2, fill="blue")
            color.clear()
            color.append(0)
    return


def restart():
    canvas.coords(
        line1,
        HEIGHT//3, 0, HEIGHT//3, WIDTH)
    canvas.itemconfigure(line1, fill="red")
    canvas.coords(
        line2,
        (HEIGHT//3)*2, 0, (HEIGHT//3)*2, WIDTH)
    canvas.itemconfigure(line2, fill="blue")
    color.clear()
    color.append(0)


racine = tk.Tk()

canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=WIDTH)
b_restart = tk.Button(racine, text="Pause", command=restart)
line1 = canvas.create_line(
        HEIGHT//3, 0, HEIGHT//3, WIDTH,
        fill="red")
line2 = canvas.create_line(
        (HEIGHT//3)*2, 0, (HEIGHT//3)*2, WIDTH,
        fill="blue")
b_restart.grid(column=0, row=1)
canvas.grid(column=0, row=0)

canvas.bind("<Button-1>", changPos)

racine.mainloop()
