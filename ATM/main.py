import tkinter as tk
import tkinter.ttk as ttk
from tkinter import Toplevel, messagebox
import hashlib
import json
import datetime
import random




#def #################################################################################
def get_datetime():
    frm = "%A, %H:%M:%S, %B-%d-%Y"
    return datetime.datetime.now().strftime(frm)


def read_json(address):
    with open(address)as file:
        return json.load(file)


def write_json(address,data):
    with open(address,'w',encoding= 'utf-8')as file:
        json.dump(data,file,ensure_ascii=False, indent=4)    



def to_sha1(password):
    return hashlib.sha1(password.encode('utf-8')).hexdigest()


def get_card_number():
    last = read_json('names.json')
    if not last:
        return random.randint(6000000000000000,7000000000000000)
    else:
        return last [-1]['card_number']+random.randint(1000,9999)    

def register():
    input_user = form_user.get()
    file = read_json('names.json')
    all_users = []
    for person in file:
        all_users.append(person['username'])
    if not input_user :
        messagebox.showerror("Username Error", "Please Enter a Username!")
    elif input_user not in all_users :  
        if not form_pass.get():  
           messagebox.showerror("Username Error", "Please Enter a Username!")
        else:
            input_pass = to_sha1(form_pass.get())

            form_user.set("")
            form_pass.set("")
            file = read_json('names.json')
            data = {
            "username": input_user,
            "password": input_pass,
            "created_at": get_datetime(),
            "card_number": get_card_number(),
            "balance" :1000,
            }     
            file.append(data)
            write_json('names.json', file)
    else:
        messagebox.showerror("Username Error", "This Username is already in use!")


def find_person(file, username):
    for person in file:
            if person['username'] == username:
                return person
    messagebox.showerror("Username Error", "Entered Invalid Username")
    return None

def login():
    username = login_user.get() 
    password = to_sha1(login_pass.get())
    file = read_json('names.json')
    person = find_person(file, username)
    if person is None:
        pass
    else:
        if person["password"] == password:
            top.deiconify()
            root.withdraw()

        else:
            messagebox.showerror("Password Error", "Entered Invalid Password")

#root ##########################################################################################
root = tk.Tk()
root.title('Bank')
top = tk.Toplevel()
top.title("Main Menu")
top.withdraw()
note =ttk.Notebook()
register_form = tk.Frame()
login_form = tk.Frame()
note.add(register_form, text='Regisater')
note.add(login_form, text='Log In')
note.grid(row=0,column=0)
#register ########################################################################################################################
tk.Label(register_form,text= 'Username').grid(row=0,column=0)
tk.Label(register_form,text= 'Password:').grid(row=1,column=0)
form_user=tk.StringVar()
form_pass=tk.StringVar()
tk.Entry(register_form,textvariable= form_user).grid(row=0,column=1)
tk.Entry(register_form,textvariable= form_pass,show='*').grid(row=1,column=1)
tk.Button(register_form,text='Register',command=register ).grid(row=2,column=0,columnspan=2,sticky=tk.W+tk.E)
#login ########################################################################################################################
tk.Label(login_form,text= 'Username').grid(row=0,column=0)
tk.Label(login_form,text= 'Password:').grid(row=1,column=0)

login_user=tk.StringVar()
login_pass=tk.StringVar()
tk.Entry(login_form,textvariable=login_user).grid(row=0,column=1)
tk.Entry(login_form,textvariable=login_pass,show='*').grid(row=1,column=1)

tk.Button(login_form,text='login',command=login).grid(row=2,column=0,columnspan=2,sticky=tk.W+tk.E)

#top ########################################################################################################################
tk.Button(top,text='Transfer',command=login).grid(row=0,column=0,sticky=tk.W+tk.E)
tk.Button(top,text='Deposite',command=login).grid(row=0,column=1,sticky=tk.W+tk.E)
tk.Button(top,text='Balance',command=login).grid(row=1,column=0,sticky=tk.W+tk.E)
tk.Button(top,text='Change Password',command=login).grid(row=1,column=1,sticky=tk.W+tk.E)
tk.Button(top,text='+1000',command=root.destroy).grid(row=2,column=0,columnspan=2,sticky=tk.W+tk.E)
tk.Button(top,text='EXIT',command=root.destroy).grid(row=3,column=0,columnspan=2,sticky=tk.W+tk.E)





root.mainloop()