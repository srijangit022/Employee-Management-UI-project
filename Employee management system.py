from customtkinter import *
from PIL import Image
from customtkinter import CTkImage
from tkinter import messagebox

def login():
    if usernameEntry.get()=='' or userPassword.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif usernameEntry.get()=='Srijan' and userPassword.get()=='1204':
        messagebox.showinfo('Success','Login is Successful')
    else:
        messagebox.showerror('ERROR','Wrong Info')

root = CTk()
root.geometry('1024x665')
root.resizable(0,0)
root.title('LOGIN PAGE')
image = CTkImage(Image.open('employee-management login page.jpg'),size = (1024,665))
imageLabel = CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text='EMPLOYEE MANAGEMENT SYSTEM',bg_color='#A0E9FC',text_color='black',font=('Goudy Old Style',20,'bold'))
headinglabel.place(x=20,y=100)

usernameEntry = CTkEntry(root,placeholder_text='Enter Your Username',width=180)
usernameEntry.place(x=60,y=200)
userPassword=CTkEntry(root,placeholder_text='Enter Your Password',width=180,show='*')
userPassword.place(x=60,y=250)

loginButton=CTkButton(root,text='Login',cursor='hand2')
loginButton.place(x=75,y=300)


root.mainloop()