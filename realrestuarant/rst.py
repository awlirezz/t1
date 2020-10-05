import tkinter as tk
from tkinter import PhotoImage
import tkinter.ttk as ttk

from config import *

# $$$$$$$$$$$$$$$$$$$ Food Information $$$$$$$$$$$$$$$$$$$ #
i = {
    0: {'name': 'BaqaliQatoq',
          'rating': 5,
          'review': 47,
          'price': 1.5,
          'des':'This is Iranian Food, which most used in north of IRAN Elit reprehen derit exce pteur dolor labore ipsum veniam exercitation deserunt.',
          'img': 'img\\cart.gif'},
    1: {'name': 'SabziQormeh',
          'rating': 4,
          'review': 72,
          'price': 1,
          'des':'This is Iranian Food, which most used in north of IRAN Elit reprehen derit exce pteur dolor labore ipsum veniam exercitation deserunt.',
          'img': 'img\\cart.gif'}
}

d = {
    0: {'name': 'BaqaliQatoq',
          'rating': 5,
          'review': 47,
          'price': 1.5,
          'des':'This is Iranian Food, which most used in north of IRAN Elit reprehen derit exce pteur dolor labore ipsum veniam exercitation deserunt.',
          'img': 'img\\cart.gif'},
    1: {'name': 'SabziQormeh',
          'rating': 4,
          'review': 72,
          'price': 1,
          'des':'This is Iranian Food, which most used in north of IRAN Elit reprehen derit exce pteur dolor labore ipsum veniam exercitation deserunt.',
          'img': 'img\\cart.gif'}
}

image = {}
img = {}
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
note.add(drink, text='Drinks')
note.add(reciept, text='Recipt')
# ################## Food Tab ################## #

for j in range(len(i)):
    f1 = tk.Frame(food,bg='#ffc107')
    f1.grid(row=j, column=0)

    name = i[j]['name']
    tk.Label(f1,
        text=name,
        width=13,
        cnf=label_cnf,
        anchor='w').grid(row=0, column=0, sticky=tk.W)

    rating = i[j]['rating'] * '★' + '(' + str(i[j]['review']) +')'
    tk.Label(f1,
        text=rating,
        font='fixedsys',
        anchor='nw').grid(row=1, column=0, sticky="nw", padx=10, pady=5)

    f1_5 = tk.Frame(f1, bg='#ffc107')
    f1_5.grid(row=1, column=1)

    image[j] = PhotoImage(file='img\\cart.gif').subsample(7)
    tk.Label(f1_5, image=image[j], bg='#ffc107', fg='#ffffff').grid(row=0, column=0)
    tk.Label(f1_5, text=2, font=('times', 15), bg='#ffc107').grid(row=0, column=1, sticky=tk.S)
    tk.Button(f1_5, text='+').grid(row=0, column=2)
    tk.Button(f1_5, text='-').grid(row=0, column=3)

    des = i[j]['des']
    tk.Message(f1,
        text=des,
        font='fixedsys',
        width=200).grid(row=2, column=0, columnspan=2, pady=5)

    price = str(i[j]['price']) + '$' 
    tk.Label(f1,
        text=price,
        font='fixedsys').grid(row=0, column=1)

    img[j] = PhotoImage(file=i[j]['img'])
    tk.Label(f1,
        image=img[j],
        borderwidth=4,
        relief="sunken",
        highlightcolor="red").grid(row=0, column=2, rowspan=4, padx=5, stick=tk.S, pady=5)


############################################################################################################################################################

for a in range(len(d)):
    f1 = tk.Frame(drink,bg='#ffc107')
    f1.grid(row=j, column=0)

    name = d[a]['name']
    tk.Label(f1,
        text=name,
        width=13,
        cnf=label_cnf,
        anchor='w').grid(row=0, column=0, sticky=tk.W)

    rating = d[a]['rating'] * '★' + '(' + str(d[a]['review']) +')'
    tk.Label(f1,
        text=rating,
        font='fixedsys',
        anchor='nw').grid(row=1, column=0, sticky="nw", padx=10, pady=5)

    f1_5 = tk.Frame(f1, bg='#ffc107')
    f1_5.grid(row=1, column=1)

    image[a] = PhotoImage(file='img\\cart.gif').subsample(7)
    tk.Label(f1_5, image=image[a], bg='#ffc107', fg='#ffffff').grid(row=0, column=0)
    tk.Label(f1_5, text=2, font=('times', 15), bg='#ffc107').grid(row=0, column=1, sticky=tk.S)
    tk.Button(f1_5, text='+').grid(row=0, column=2)
    tk.Button(f1_5, text='-').grid(row=0, column=3)


    price = str(d[a]['price']) + '$' 
    tk.Label(f1,
        text=price,
        font='fixedsys').grid(row=0, column=1)






root.mainloop()