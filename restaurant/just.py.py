import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Image, PhotoImage 
from  joje import *
#ddddd
i ={
    '1' : {
        'name' : '★Joje Ordack★',
        'rating' : 5,
        'review' : 47,   
        'price'  : 1.5,
        'des':'This is Iranian Food, which most used in north of IRAN Elit reprehen derit exce pteur dolor labore ipsum veniam exercitation deserunt.',
        'img':'restaurant/img/index.gif'
        },
    '2' : {
        'name' :  '★ye chiz khoob★',
        'rating' : 5,
        'review' : 47,   
        'price'  : 1.5,
        'des':'This is Iranian Food, which most used in north of IRAN Elit reprehen derit exce pteur dolor labore ipsum veniam exercitation deserunt.',
        'img':'restaurant/img/index.gif'
        }
 #   '2' : {}
 #   '3' : {}

}

abc = {'bg':'#FFEB3B'}
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
note.add(drink, text='Drink')
note.add(reciept, text='Reciept')
# ################## Food Tab ################## #
for j in range(len(i)):
    f1 = tk.Frame(food, cnf=label_cnf)
    f1.grid(row=j, column=0)





    name = i['1']['name']
    tk.Label(f1, text=name, cnf=abc ,anchor='w',width=10).grid(row=0, column=0, sticky=tk.W)



    rating = i ['1']['rating']*'★'+'('+str(i['1']['review'])+')'
    tk.Label(f1, text=rating, cnf=abc,font='fixedsys',anchor='nw').grid(row=1, column=0,sticky=tk.W)


    des = i['1']['des']
    tk.Message(f1,
        text=des,
        font='fixedsys',
        width=200).grid(row=2, column=0, columnspan=2, pady=5)

    price =str(i ['1']['price'])+'$'
    tk.Label(f1, text=price, cnf=abc,font='fixedsys').grid(row=0, column=1,sticky=tk.W)



    img = PhotoImage(file=i['1']['img'])
    tk.Label(f1,image=img ,borderwidth=6, relief="groove",highlightcolor="red").grid(row=0,column=2,rowspan=4, padx=5, stick=tk.S, pady=5)
    ########################################################################################################################################
root.mainloop()