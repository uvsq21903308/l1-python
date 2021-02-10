import tkinter as tk

HEIGHT, WIDTH = 500, 500

racine = tk.Tk()

canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=WIDTH)
b_cancel = tk.Button(racine, text="Annuler")
canvas.grid(row=0, column=1)
b_cancel.grid(row=0, column=0)
racine.mainloop()
