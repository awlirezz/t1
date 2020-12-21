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
def check():
    cnx,cursor = crud.connect()
    if cnx != None:
        athletes = crud.read(cnx,cursor)
        tree.delete(*tree.get_children())
        for  athlete in athletes:
            tree.insert("",0,text = '',value=(athlete[1],athlete[2],athlete[3],athlete[4]))








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
tk.Button(r,
    text='Check',
    command=check).grid(row=0, column=0, columnspan=1)

tree = ttk.Treeview(r, selectmode ='browse')

verscrlbar = ttk.Scrollbar(r, orient ="vertical", command=tree.yview) 
verscrlbar.grid(row=1, column=3) 
tree.configure(xscrollcommand=verscrlbar.set) 

tree["columns"]=("one","two","three", "four")
tree.column("#0", width=1, stretch=tk.NO)
tree.column("one", width=70, minwidth=150, stretch=tk.NO)
tree.column("two", width=70)
tree.column("three", width=80, minwidth=50, stretch=tk.NO)
tree.column("four", width=50, minwidth=50, stretch=tk.NO)
tree.heading("#0",text="ID",anchor=tk.W)
tree.heading("one", text="FirstName",anchor=tk.W)
tree.heading("two", text="LastName",anchor=tk.W)
tree.heading("three", text="Phone",anchor=tk.W)
tree.heading("four", text="Sex",anchor=tk.W)
tree.grid(row=1, column=0, columnspan=3)



root.mainloop()
