import tkinter as tk

def pixelclic(event):
    if event.x < 150:
        canvas.create_oval(event.x, event.y, event.x + 100, event.y + 100, fill="blue")
    elif event.x > 250:
        canvas.create_oval(event.x, event.y, event.x + 100, event.y + 100, fill="red")

    
HEIGHT, WIDTH = 500, 500
x = 250
racine = tk.Tk()

canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid()
for i in range(HEIGHT):
    canvas.create_line(x, 0, x, 500, fill="white")
canvas.bind("<Button-1>", pixelclic)

racine.mainloop()