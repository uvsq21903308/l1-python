import tkinter as tk

def pixelclic(event):
    canvas.create_line(event.x, event.y, event.x + 1, event.y, fill="red")
    
HEIGHT, WIDTH = 500, 500
racine = tk.Tk()

canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid()
canvas.bind("<Button-1>", pixelclic)

racine.mainloop()