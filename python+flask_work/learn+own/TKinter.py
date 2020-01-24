import tkinter as tk
import pynput

window = tk.Tk()
back = tk.Frame(master=window, width=500, height=500, bg='black')
back.pack()

but = tk.Button(master=window, bg='green', text='my king',)
but.pack()

f = open('adma.tex', 'w')
    
window.mainloop()

