import tkinter as tk
import tkinter.ttk as ttk


root = tk.Tk()



note = ttk.Notebook()
note.grid(row=0,column=0)

timer = tk.Frame()
patient = tk.Frame()



note.add(timer,text='Timer')
note.add(patient,text='Patient')
p1=tk.StringVar()
p1.set('patient1')
tk.Label(timer,textvariable=p1).grid(row=1,column=0)

p2=tk.StringVar()
p2.set('patient2')
tk.Label(timer,textvariable=p2).grid(row=1,column=2)

p3=tk.StringVar()
p3.set('patient3')
tk.Label(timer,textvarible=p3).grid(row=1,column=4)

p4=tk.StringVar()
p4.set('timer1')
tk.Label(timer,textvariable=p4).grid(row=2,column=0)

p5=tk.StringVar()
p5.set('timer2')
tk.Label(timer,textvariable=p5).grid(row=2,column=2)

p6=tk.StringVar()
p6.set('timer3')
tk.Label(timer,textvariable=p6).grid(row=2,column=4)











root.mainloop()