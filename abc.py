import tkinter as tk
from tkinter import Frame
import tkinter.ttk as ttk


from abcl import *

i ={
    '1' : {'name' :  'ye chiz khoob',
         'rating' : 5,
         'review' : 47,
         'price'  : 2.5 },
 #   '2' : {}
 #   '3' : {}

}

asd={'bg' : '#ff6d00'}
asd1={'bg':'#64dd17'}
root = tk.Tk()
note = ttk.Notebook()
note.grid(row=0, column=0)

food=tk.Frame()
drink=tk.Frame()
receipt=tk.Frame()



note.add(food, text='Food')
note.add(drink, text='Drink')
note.add(receipt, text='Receipt')


f1 = tk.Frame(food,cnf=Label_cnf)
f1.grid(row=0, column=0)


# d1 = tk.Frame(drink)
# d1.grid(row=0, column=0)


# r1 = tk.Frame(receipt)
# r1.grid(row=0, column=0)




tk.Label(f1,text='Joje gang',cnf=asd).grid(row=0,column=0)

tk.Label(f1,text='    ⍟⍟⍟⍟     ',cnf=asd1).grid(row=1,column=0)

tk.Label(f1,text='    2.5$      ',cnf=asd1).grid(row=2,column=0)

img = PhotoImage(file = '')
root.mainloop()