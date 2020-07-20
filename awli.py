import tkinter as tk
from datetime import datetime


######################################################
                                                     #
def say():
    global n
    n += 1                                             #
    numbers.append(n + 1)                  #
    d = datetime.now()                               #
    a.config(text=d.strftime("%B/%d/%Y"))            #
    a1.config(text=d.strftime("%H:%M:%S %p"))        #
    a2.config(text=d.strftime("%A"))                 #
    a3.config(text='Your Turn:' + str(numbers[-1]))  #
                                                     #
                                                     #
######################################################
def op1():
    if numbers:                                      #
        b4.config(text=numbers.pop(0))                   #
                                                     #
                                                     #
                                                     #
def op2():
    if numbers:                                     #
        b5.config(text=numbers.pop(0))                   #
                                                     #
                                                     #
def op3():
    if numbers:                                     #
        b6.config(text=numbers.pop(0))                   #


######################################################
root = tk.Tk()                                       #
######################################################
n = -1                                              #
numbers = []                                        #
######################################################
a = tk.Label(root, text='')  #
a.grid(row=0, column=0)  #
#
a1 = tk.Label(root, text='')  #
a1.grid(row=1, column=0)  #
#
a2 = tk.Label(root, text='')  #
a2.grid(row=2, column=0)  #
#
a3 = tk.Label(root, text='')  #
a3.grid(row=3, column=0)  #
######################################################
b = tk.Button(root, text='Get turn!', command=say)   #
b.grid(row=4, column=0)                              #
                                                     #
tp = tk.Toplevel(root)                               #
                                                     #
b1 = tk.Button(tp, text='Operator1', command=op1)   #
b1.grid(row=0, column=1)                             #
                                                     #
                                                     #
b2 = tk.Button(tp, text='Operator2', command=op2)    #
b2.grid(row=0, column=2)                             #
                                                     #
                                                     #
b3 = tk.Button(tp, text='Operator3', command=op3)    #
b3.grid(row=0, column=3)                             #
######################################################
b4 = tk.Label(tp, text='__')                         #
b4.grid(row=1, column=1)  #
#
#
b5 = tk.Label(tp, text='__')  #
b5.grid(row=1, column=2)  #
#
#
b6 = tk.Label(tp, text='__')  #
b6.grid(row=1, column=3)  #
######################################################


root.mainloop()
