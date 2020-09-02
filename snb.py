import tkinter as tk
from tkinter import Frame
import tkinter.ttk as ttk


def start():
    pass


def callback1(arg1, arg2, arg3):
    p1.set(n_p_1.get())


root = tk.Tk()

note = ttk.Notebook()
note.grid(row=0, column=0)

timer = tk.Frame()
patient = tk.Frame()

note.add(timer, text='Timer')
note.add(patient, text='Patient')

# ############### Timer First Row ############## #
p1 = tk.StringVar()
p1.set('Patient1')
tk.Label(timer, textvariable=p1).grid(row=0, column=0)
p2 = tk.StringVar()
p2.set('Patient2')
tk.Label(timer, textvariable=p2).grid(row=0, column=1)
p3 = tk.StringVar()
p3.set('Patient3')
tk.Label(timer, textvariable=p3).grid(row=0, column=2)
# ############## Timer Second Row ############## #
t1 = tk.StringVar()
t1.set('00:00:00')
tk.Label(timer, textvariable=t1).grid(row=1, column=0)
t2 = tk.StringVar()
t2.set('00:00:00')
tk.Label(timer, textvariable=t2).grid(row=1, column=1)
t3 = tk.StringVar()
t3.set('00:00:00')
tk.Label(timer, textvariable=t3).grid(row=1, column=2)
# ########### Timer Third Row Buttons ########## #
tk.Button(timer, text='Start', command=start).grid(row=2, column=0)
tk.Button(timer, text='Start', command=start).grid(row=2, column=1)
tk.Button(timer, text='Start', command=start).grid(row=2, column=2)
# ######## Timer Last Row Cancel Button ######## #
tk.Button(timer, text='Cancel', command=root.destroy).grid(row=3, column=0, columnspan=3, sticky=tk.E + tk.W)
# ############ Patient 1 Name Timer ############ #
patient1 = tk.LabelFrame(patient, text='Patient1')
patient1.grid(row=0, column=0, padx=10)

tk.Label(patient1, text='Name').grid(row=0, column=0)
tk.Label(patient1, text='Timer').grid(row=1, column=0)
n_p_1 = tk.StringVar()
n_p_1.trace('w', callback1)
tk.Entry(patient1, textvariable=n_p_1).grid(row=0, column=1)
# ------------------Timer-------------------- #
h_p_1 = tk.StringVar()
h_p_1.set('12')
m_p_1 = tk.StringVar()
m_p_1.set('30')
s_p_1 = tk.StringVar()
s_p_1.set('30')
f1 = tk.Frame(patient1)
f1.grid(row=1, column=1)
tk.Spinbox(f1,
           from_=0,
           to=23,
           wrap=True,
           textvariable=h_p_1,
           width=2,
           state="readonly").grid(row=0, column=0)
tk.Spinbox(f1,
           from_=0,
           to=59,
           wrap=True,
           textvariable=m_p_1,
           width=2,
           state="readonly").grid(row=0, column=1)
tk.Spinbox(f1,
           from_=0,
           to=59,
           wrap=True,
           textvariable=s_p_1,
           width=2,
           state="readonly").grid(row=0, column=2)
root.mainloop()
