import tkinter as tk

def pixelclic(event):
    

    
HEIGHT, WIDTH = 500, 500
x = 250
racine = tk.Tk()

canvas = tk.Canvas(racine, bg="black", height=HEIGHT, width=WIDTH)
canvas.grid()
for i in range(HEIGHT):
    canvas.create_line(x, 0, x, 500, fill="white")
canvas.bind("<Button-1>", pixelclic)

racine.mainloop()