import tkinter as tk
import tkinter.ttk as ttk
import hashlib
import json


def read_json(address):
    with open(address)as file:
        return json.load(file)


def write_json(address,data):
    with open(address,'w',encoding= 'utf-8')as file:
        json.dump(data,file,ensure_ascii=False, indent=4)    



def to_sha1(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest()




def register():
    input_user = form_user.get()
    input_pass = to_sha1(form_pass.get())           
    form_user.set('')
    form_pass.set('')  
    file = read_json('names.json')
    data = {'usernames':input_user,'password':input_pass}
    file.append(data) 
    write_json('names.json',file) 


def login():
    pass    





root = tk.Tk()
root.title('Bank')




note =ttk.Notebook()




register_form = tk.Frame()
login_form = tk.Frame()


note.add(register_form, text='Regisater')
note.add(login_form, text='Log In')
note.grid(row=0,column=0)

tk.Label(register_form,text= 'Username').grid(row=0,column=0)
tk.Label(register_form,text= 'Password:').grid(row=1,column=0)

form_user=tk.StringVar()
form_pass=tk.StringVar()
tk.Entry(register_form,textvariable= form_user).grid(row=0,column=1)
tk.Entry(register_form,textvariable= form_pass,show='*').grid(row=1,column=1)

tk.Button(register_form,text='Register',command=register ).grid(row=2,column=0,columnspan=2,sticky=tk.W+tk.E)

############################################################################################
tk.Label(login_form,text= 'Username').grid(row=0,column=0)
tk.Label(login_form,text= 'Password:').grid(row=1,column=0)

login_user=tk.StringVar()
login_pass=tk.StringVar()
tk.Entry(login_form,textvariable=login_user).grid(row=0,column=1)
tk.Entry(login_form,textvariable=login_pass,show='*').grid(row=1,column=1)

tk.Button(login_form,text='login',command=login).grid(row=2,column=0,columnspan=2,sticky=tk.W+tk.E)




root.mainloop()