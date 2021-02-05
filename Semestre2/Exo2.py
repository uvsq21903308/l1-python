import tkinter as tk


def pause():
    b_pause.config(text="Restart")
    return


HEIGHT, WIDTH = 500, 500

racine = tk.Tk()

canvas = tk.Canvas(racine, bg="white", height=HEIGHT, width=WIDTH)
b_pause = tk.Button(racine, text="pause", command=pause)
b_pause.grid(column=0, row=1)
canvas.grid(column=0, row=0)

racine.mainloop()