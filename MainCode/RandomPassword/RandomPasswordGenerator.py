import random
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import *
from tkinter import *
from tkinter.ttk import *
from ttkthemes import ThemedTk
import re
from cryptography.fernet import Fernet

#win = tk.Tk()
win = ThemedTk(theme="radiance")
win.title('Password Generator')

photo = PhotoImage(file = "Security-Password-1-icon.png")
win.iconphoto(False, photo)

pas = ''
tok = ''
dec = ''
#-------------------------------------<Password Generator>--------------------------------------------------------------
def generate():
    website = entry0.get()
    email = entry1.get()
    string = entry.get()
    username = entry2.get()
    string = string.capitalize()
    password = ''
    l = ['@','#','$','%','.']
    r = random.randint(0,4)
    password = string+str(random.randint(0,10000))+str(l[r])
    pas = password 

    if Regex(website,email):
        showinfo("Generated Password", f" Your Password :{password}")
        fp = open('password.txt', 'a')
        fp.write(website + '\t' + email + '\t' + Encrypt() + '\t' + username + '\n')
        fp.close()
    else:
        showwarning("Wrong credentials",f"You've entered wrong email or website")
 
#-----------------------------------------------<Regex>-----------------------------------------------------------------
def Regex(w,e):
    email1 = re.compile(r'''
    (\w{1,10}(\.)?\w{0,10})  
    (@)
    (gmail|hotmail|rediff|gla)
    (\.)?
    ([a-zA-z])?
    (\.)
    ([a-zA-z])''',re.I|re.VERBOSE)
    website1 = re.compile(r'''
    (www)?
    ([a-zA-Z]+)
    (.)
    ([a-zA-Z]+)
    ''',re.I|re.VERBOSE)
    if(re.search(email1,e) and re.search(website1,w)):
        return True
    else:
        return False
#----------------------------------------------<Encryption>-------------------------------------------------------------
def Encrypt():
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(b'pas')
    tok = token
    print(f.decrypt(token))
    return tok
#-------------------------------------------<Layout>--------------------------------------------------------------------
website = tk.Label(win, text="Enter the name of website: ")
website.grid(row=0,column=0,padx=8,pady=8)

entry0 = tk.Entry(win)
entry0.grid(row=0,column=1,padx=8)

email = tk.Label(win, text="Enter your Email: ")
email.grid(row=1,column=0,padx=8,pady=8)

entry1 = tk.Entry(win)
entry1.grid(row=1,column=1,padx=8)

label = tk.Label(win, text="Enter String to generate your password: ")
label.grid(row=2,column=0,padx=8,pady=8)

entry = tk.Entry(win)
entry.grid(row=2,column=1,padx=8)

email = tk.Label(win, text="Enter your Username: ")
email.grid(row=3,column=0,padx=8,pady=8)

entry2 = tk.Entry(win)
entry2.grid(row=3,column=1,padx=8)

button =ttk.Button(win,text="Generate",command=generate)
button.grid(row=4,column=0,columnspan=2,padx=8)

win.mainloop()