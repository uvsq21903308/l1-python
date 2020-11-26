import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

racine = tk.Tk()
canvas = tk.Canvas(racine, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

# Début de votre code
x0 = 100
x1 = CANVAS_WIDTH - 100
y = CANVAS_HEIGHT / 2
line = canvas.create_line(x0, y, x1, y)
oval1 = canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50)
oval2 = canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
oval3 = canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
canvas.grid()
# Fin de votre code

racine.mainloop()
