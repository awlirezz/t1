import tkinter as tk
from datetime import datetime


def say():
    numbers.append(len(numbers)+1)
    d =datetime.now()
    a.config(text=d.strftime("%B/%d/%Y"))
    a1.config(text=d.strftime("%H:%M:%S %p"))
    a2.config(text=d.strftime("%A"))
    a3.config(text='Your Turn:'+str(numbers[-1]))

root = tk.Tk()

numbers = []

a=tk.Label(root, text ='')
a.grid(row=0,column=0)

a1=tk.Label(root, text ='')
a1.grid(row=1,column=0)

a2=tk.Label(root, text ='')
a2.grid(row=2,column=0)

a3=tk.Label(root, text ='')
a3.grid(row=3,column=0)

b=tk.Button(root,text = 'Get turn!',command=say)
b.grid(row=4,column=0)

tp = tk.Toplevel(root)

b1=tk.Button(tp,text = 'Deo-Boy!',command=say)
b1.grid(row=0,column=1)


b2=tk.Button(tp,text = 'MR.Savage!',command=say)
b2.grid(row=0,column=2)


b3=tk.Button(tp,text = 'Tfue!',command=say)
b3.grid(row=0,column=3)

b4=tk.Label(tp,text='op1')
b4.grid(row=1,column=1)


b5=tk.Label(tp,text='op2')
b5.grid(row=1,column=2)


b6=tk.Label(tp,text='op3')
b6.grid(row=1,column=3)






root.mainloop()