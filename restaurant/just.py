import tkinter as tk
import tkinter.ttk as ttk

from  joje import *

i ={
    '1' : {'name' :  'ye chiz khoob',
         'rating' : 5,
         'review' : 47,   
         'price'  : 1.5
         'img':'image'.'PycharmProjects/t1/restaurant/img' },
 #   '2' : {}
 #   '3' : {}

}

abc = {'bg':'#FFEB3B'}
root = tk.Tk()

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
f1 = tk.Frame(food, cnf=label_cnf)
f1.grid(row=0, column=0)



name = i ['1']['name']
tk.Label(f1, text=name, cnf=abc).grid(row=0, column=0)



rating = i ['1']['rating']*'★'+'('+str(i['1']['review'])+')'
tk.Label(f1, text=rating, cnf=label_cnf).grid(row=1, column=0)



price =str(i ['1']['price'])+'$'
tk.Label(f1, text=price, cnf=label_cnf).grid(row=2, column=0)

root.mainloop()

