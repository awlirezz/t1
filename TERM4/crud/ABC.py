import tkinter as tk


def register():
    






root = tk.Tk()

tk.Label(root, text="First Name:").grid(row=0, column=0)
first_name = tk.StringVar()
tk.Entry(root, textvariable=first_name).grid(row=0, column=1)

tk.Label(root, text="Last Name:").grid(row=1, column=0)
last_name = tk.StringVar()
tk.Entry(root, textvariable=last_name).grid(row=1, column=1)

tk.Label(root, text="Phone:").grid(row=2, column=0)
phone = tk.StringVar()
tk.Entry(root, textvariable=phone).grid(row=2, column=1)

tk.Label(root, text="Sex:").grid(row=3, column=0)
sex = tk.StringVar()
sex.set('f')
options = ['m', 'f', 'others']
tk.OptionMenu(root, sex, *options).grid(row=3, column=1,sticky=tk.W+tk.E)
tk.Button(root,
text='Register',
command=register).grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E)


root.mainloop()