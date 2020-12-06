import tkinter as tk

def pixelclic(event):
    if not pos:
        pos.append(event.x)
        pos.append(event.y)
    elif event.x > 250 and pos[0] > 250 and pos:
        canvas.create_line(pos[0], pos[1], event.x, event.y, fill='blue')
        pos.clear()
    elif event.x < 250 and pos[0] < 250 and pos:
        canvas.create_line(pos[0], pos[1], event.x, event.y, fill='blue')
        pos.clear()
    elif event.x > 250 and pos[0] < 250 and pos:
        canvas.create_line(pos[0], pos[1], event.x, event.y, fill='red')
        pos.clear()
    elif event.x < 250 and pos[0] > 250 and pos:
        canvas.create_line( event.x, event.y, pos[0], pos[1], fill='red')
        pos.clear()
    if event.x != pos[0] or event.y != pos[1] and pos:
        pos.clear()
        pos.append(event.x)
        pos.append(event.y)

    
HEIGHT, WIDTH = 500, 500
x = 250
pos = []
racine = tk.Tk()

canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid()
for i in range(HEIGHT):
    canvas.create_line(x, 0, x, 500, fill="white")
canvas.bind("<Button-1>", pixelclic)
racine.mainloop()