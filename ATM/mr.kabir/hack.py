import tkinter as tk
from tkinter import Frame
import tkinter.ttk as ttk


def callback1(arg1, arg2, arg3):
    p1.set(n_p_1.get())

def tabdil():
     if 
       





letter:{  
    'a':'4',
    'b':'6',
    'c':'<',
    'd':'|)'}




root = tk.Tk()


note = ttk.Notebook()
note.grid(row=0, column=0)



persian = tk.Frame()
hack = tk.Frame()

note.add(hack, text='Hack')
note.add(persian, text='Persian')






p1 = tk.StringVar()
p1.set('first1')
Name = tk.LabelFrame(persian, text='Name')
tk.Label(hack, textvariable=p1).grid(row=0, column=0)
tk.Label(persian, text='Name').grid(row=0, column=0)
n_p_1 = tk.StringVar()
n_p_1.trace('w', callback1)
tk.Entry(persian, textvariable=n_p_1).grid(row=0, column=1)


root.mainloop()
