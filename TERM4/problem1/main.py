import tkinter as tk
from tkinter import ttk
from crud import crud




def register():
    cnx,cursor = crud.connect()
    if cnx != None:
        crud.create(
        cnx,cursor,
        first_name.get().lower(),
        last_name.get().lower(),
        phone.get(),
        sex.get(),
       )


root = tk.Tk()


note = ttk.Notebook()
c = tk.Frame()
r = tk.Frame()
note.add(c,text = 'Create')
note.add(r,text = 'Read')
note.grid(row=0,column=0)


tk.Label(c, text="First Name:").grid(row=0, column=0)
first_name = tk.StringVar()
tk.Entry(c, textvariable=first_name).grid(row=0, column=1)

tk.Label(c, text="Last Name:").grid(row=1, column=0)
last_name = tk.StringVar()
tk.Entry(c, textvariable=last_name).grid(row=1, column=1)

tk.Label(c, text="Phone:").grid(row=2, column=0)
phone = tk.StringVar()
tk.Entry(c, textvariable=phone).grid(row=2, column=1)

tk.Label(c, text="Sex:").grid(row=3, column=0)
sex = tk.StringVar()
sex.set('f')
options = ['m', 'f', 'others']
tk.OptionMenu(c, sex, *options).grid(row=3, column=1,sticky=tk.W+tk.E)
tk.Button(c,
text='Register',
command=register).grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E)


root.mainloop()
