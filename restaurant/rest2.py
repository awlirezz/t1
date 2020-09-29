import tkinter as tk
from tkinter import PhotoImage
import tkinter.ttk as ttk

from restn1 import *

# $$$$$$$$$$$$$$$$$$$ Food Information $$$$$$$$$$$$$$$$$$$ #
i = {
    '1': {'name': 'BaqaliQatoq',
          'rating': 5,
          'review': 47,
          'price': 1.5,
          'des':'This is Iranian Food, which most used in north of IRAN Elit reprehen derit exce pteur dolor labore ipsum veniam exercitation deserunt.',
          'img': 'images/baqali.gif'},

}

# -------------------------------------------------------- #

root = tk.Tk()
root.title('Restauran Menu System')
note = ttk.Notebook()
note.grid(row=0 , column=0)
# ################ NoteBook Tabs ############### #
food = tk.Frame()
drink = tk.Frame()
reciept = tk.Frame()
# ---------------------------------------------- #
note.add(food, text='Foods')
note.add(drink, text='Foods')
note.add(reciept, text='Foods')
# ################## Food Tab ################## #
f1 = tk.Frame(food,bg='#ffc107',
)
f1.grid(row=0, column=0)

name = i['1']['name']
tk.Label(f1,
    text=name,
    cnf=label_cnf,
    anchor='w').grid(row=0, column=0, sticky=tk.W)

rating = i['1']['rating'] * '★' + '(' + str(i['1']['review']) +')'
tk.Label(f1,
    text=rating,
    font='fixedsys',
    anchor='nw').grid(row=1, column=0, sticky="nw", padx=10, pady=5)

des = i['1']['des']
tk.Message(f1,
    text=des,
    font='fixedsys',
    width=200).grid(row=2, column=0, columnspan=2, pady=5)

price = str(i['1']['price']) + '$' 
tk.Label(f1,
    text=price,
    font='fixedsys').grid(row=0, column=1)

img = PhotoImage(file=i['1']['img'])
tk.Label(f1,
    image=img,
    borderwidth=4,
    relief="sunken",
    highlightcolor="red").grid(row=0, column=2, rowspan=4, padx=5, stick=tk.S, pady=5)

root.mainloop()
