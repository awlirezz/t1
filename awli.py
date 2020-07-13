import tkinter as tk
from datetime import datetime


def say():
    numbers.append(len(numbers)+1)
    d =datetime.now()
    a.config(text=d.strftime("%B-%d-%Y"))
    a1.config(text=d.strftime("%H:%M:%S %p"))
    a2.config(text=d.strftime("%A"))
    a3.config(text=numbers[-1])

root = tk.Tk()

numbers = []

a=tk.Label(root, text ='')
a.pack()

a1=tk.Label(root, text ='')
a1.pack()

a2=tk.Label(root, text ='')
a2.pack()

a3=tk.Label(root, text ='')
a3.pack()

b=tk.Button(root,text = 'Get turn!',command=say)
b.pack()

root.mainloop()