import tkinter as tk
from time import sleep

def stop(side):
    global flag
    if side == 'left':
        flag = True
    else:
        flag = False


def start():
    pass
    while True:
        sleep(1)
        if flag:
            timer['right'] -= 1
        else:
            timer['left'] -= 1
     print(timer)

root = tk.Tk()
timer = {'left': 1200
    ,
         'right': 1200}
flag = True
tk.Label(root, text='Left Player').grid(row=0, column=0)

tk.Label(root, text='Right Player').grid(row=0, column=3)

l_timer = tk.StringVar()
l_timer.set('20:00')
tk.Label(root, textvariable=l_timer).grid(row=1, column=0)

r_timer = tk.StringVar()
r_timer.set('20:00')

tk.Label(root, textvariable=r_timer).grid(row=1, column=3)

tk.Button(root, text='Stop', command=stop).grid(row=2, column=0)

tk.Button(root, text='Stop', command=stop).grid(row=2, column=3)

tk.Button(root, text='Start').grid(row=3, column=2)

tk.Button(root, text='Cancel', command=root.destroy).grid(row=4, column=2)

root.mainloop()
