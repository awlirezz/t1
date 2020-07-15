import tkinter as tk





root = tk.Tk()
a=tk.Label(root,text='Come here boy',bg='red',font=('times',20))
a.grid(row=0,column=0,rowspan=3,sticky=tk.S+tk.N)

a1=tk.Label(root,text='Dep-Boy',bg='blue',font=('times',20))
a1.grid(row=0,column=1,columnspan=3,sticky=tk.W+tk.E)


a2=tk.Label(root,text='Tfue',bg='yellow',font=('times',20))
a2.grid(row=1,column=1,rowspan=2,sticky=tk.S+tk.N)


a3=tk.Label(root,text='Mr.Savage',bg='green',font=('times',20))
a3.grid(row=1,column=2,rowspan=2,sticky=tk.S+tk.N)


a4=tk.Label(root,text='Buga',bg='red',font=('times',20))
a4.grid(row=1,column=3)


a5=tk.Label(root,text='Dr.tfi',bg='blue',font=('times',20))
a5.grid(row=2,column=3)




root.mainloop()



