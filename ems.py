from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox





window=CTk()
window.geometry('930x580+100+100')
window.resizable(False,False)
window.title('Employee Management System')
window.configure(fg_color='#161D27')





#GUI
logo=CTkImage(Image.open('bg.5.jpg'),size=(930,150))
logolabel=CTkLabel(window,image=logo,text='')
logolabel.grid(row=0,column=0,columnspan=2)

leftFrame=CTkFrame(window,fg_color='#161D27')
leftFrame.grid(row=1,column=0)

idLabel=CTkLabel(leftFrame,text='ID',font=('arial',18,'bold'))
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky='w')

idEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftFrame,text='Name',font=('arial',18,'bold'))
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky='w')

nameEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
nameEntry.grid(row=1,column=1)

phLabel=CTkLabel(leftFrame,text='Phone',font=('arial',18,'bold'))
phLabel.grid(row=2,column=0,padx=20,pady=15,sticky='w')

phEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
phEntry.grid(row=2,column=1)

roleLabel=CTkLabel(leftFrame,text='Role',font=('arial',18,'bold'))
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky='w')

role_options=['Web Developer','Cloud Architect','Technical Writer','Network Engineer','DevOops Engineer','Data Scientist','Business Analyst','UI/UX Designer']
roleBox=CTkComboBox(leftFrame,values=role_options,width=180,font=('arial',15,'bold'),state='readonly')
roleBox.grid(row=3,column=1)
roleBox.set(role_options[0])

genderLabel=CTkLabel(leftFrame,text='Gender',font=('arial',18,'bold'))
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky='w')

gender_options=['Male','Female','Other']
genderBox=CTkComboBox(leftFrame,values=gender_options,width=180,font=('arial',15,'bold'),state='readonly')
genderBox.grid(row=4,column=1)
genderBox.set(gender_options[0])

salaryLabel=CTkLabel(leftFrame,text='Salary',font=('arial',18,'bold'))
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky='w')

salaryEntry=CTkEntry(leftFrame,font=('arial',15,'bold'),width=180)
salaryEntry.grid(row=5,column=1)


rightFrame=CTkFrame(window)
rightFrame.grid(row=1,column=1)

search_options=['ID','Name','Phone','Gender','Role','Salary']
searchBox=CTkComboBox(rightFrame,values=search_options,state='readonly')
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry=CTkEntry(rightFrame)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightFrame,text='Search',width=100)
searchButton.grid(row=0,column=2)

showallButton=CTkButton(rightFrame,text='Show All',width=100)
showallButton.grid(row=0,column=3,pady=5)


tree=ttk.Treeview(rightFrame,height=13)
tree.grid(row=1,column=0,columnspan=4)

tree['columns']=('ID','Name','Role','Phone','Salary','Gender')

tree.heading('ID',text='ID')
tree.heading('Name',text='Name')
tree.heading('Role',text='Role')
tree.heading('Phone',text='Phone')
tree.heading('Salary',text='Salary')
tree.heading('Gender',text='Gender')

tree.config(show='headings')

tree.column('ID',width=100)
tree.column('Name',width=160)
tree.column('Role',width=180)
tree.column('Phone',width=120)
tree.column('Salary',width=140)
tree.column('Gender',width=95)

style=ttk.Style()

style.configure('Treeview.Heading',font=('arial',16,'bold'))

scrollbar=ttk.Scrollbar(rightFrame,orient=VERTICAL)
scrollbar.grid(row=1,column=4,sticky='ns')


buttonFrame=CTkFrame(window,fg_color='#161D27')
buttonFrame.grid(row=2,column=0,columnspan=2)

newButton=CTkButton(buttonFrame,text='New Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
newButton.grid(row=0,column=0,pady=5)

addButton=CTkButton(buttonFrame,text='Add Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
addButton.grid(row=0,column=1,pady=5,padx=5)

updateButton=CTkButton(buttonFrame,text='Update Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
updateButton.grid(row=0,column=2,pady=5,padx=5)

deleteButton=CTkButton(buttonFrame,text='Delete Employee',font=('arial',15,'bold'),width=160,corner_radius=15)
deleteButton.grid(row=0,column=3,pady=5,padx=5)

deleteallButton=CTkButton(buttonFrame,text='Delete All',font=('arial',15,'bold'),width=160,corner_radius=15)
deleteallButton.grid(row=0,column=4,pady=5,padx=5)









window.mainloop()
