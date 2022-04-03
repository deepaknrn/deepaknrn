import tkinter
from tkinter import messagebox
import PasswordGenerator 
import json

website=""
email_user=""
password=""
choice=""
notification=""
generate_password=""
data={}
website_search=""
search=[]

#--------------------------------SEARCH

def search():
  global website_search
  global search
  website_search=website_textbox.get()
  search=[]
  try:
    with open("./password.json") as data_file:
      data=json.load(data_file)
  except FileNotFoundError:
    tkinter.messagebox.showinfo(title=None, message="Search File is empty")
  else:
    try:
      search.append(data[website_search])
    except KeyError:
      tkinter.messagebox.showinfo(title=None, message="Website not Found")
    else: 
      tkinter.messagebox.showinfo(title=None, message=data[website_search])



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  global generate_password
  password_textbox.delete(0,'end')
  generate_password=PasswordGenerator.password
  password_textbox.insert(0,generate_password)
  

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
  global website
  global email_user
  global password
  global choice 
  global notification
  website=website_textbox.get()
  email_user=email_textbox.get()
  password=password_textbox.get()

  new_data={
    website:{
      "email":email_user,
      "password":password
    }
  }


  if(len(str(website))==0 or len(str(email_user))==0 or len(str(password))==0):
    notification=tkinter.messagebox.showerror(title="Details are emtpy", message="Details are empty")
  else:
      choice=tkinter.messagebox.askokcancel(title="Website",message=f"These are the details entered Website : {website} , email/user : {email_user} , password : {password}. Press OK to Continue CANCEL to CANCEL")

      if choice:
        global data
        #Reading old data from the file if the file exists
        try:
          with open("./password.json","r") as data_file:
            data=json.load(data_file)
        #Updating the old data from the file with the new data
        except FileNotFoundError:
           data.update(new_data)
           with open("./password.json","w") as data_file: 
            json.dump(data,data_file,indent=4)
        else:
            data.update(new_data)
        #Writing the data to the file and saving it
            f=open("./password.json","w")
            json.dump(data,f,indent=4)
            f.close()
        finally:
            website_textbox.delete(0,'end')
            email_textbox.delete(0,'end')
            password_textbox.delete(0,'end')
      
      else:
        website_textbox.delete(0,'end')
        email_textbox.delete(0,'end')
        password_textbox.delete(0,'end')

# ---------------------------- UI SETUP ------------------------------- #

window=tkinter.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)
window.config(bg="white")

canvas=tkinter.Canvas(width=200, height=200,bg="white",highlightthickness=0)
filename = tkinter.PhotoImage(file = "logo.png")
image = canvas.create_image(100, 100,image=filename)
canvas.grid(column=1,row=0)

website_label=tkinter.Label(text="Website",font=("Arial",8,"bold"),bg="white",highlightthickness=0)
website_label.grid(column=0,row=1)

email_label=tkinter.Label(text="Email/Username",font=("Arial",8,"bold"),bg="white",highlightthickness=0)
email_label.grid(column=0,row=2)

password_label=tkinter.Label(text="Password",font=("Arial",8,"bold"),bg="white",highlightthickness=0)
password_label.grid(column=0,row=3)

website_textbox=tkinter.Entry()
website_textbox.config(width="35")
website_textbox.focus()
website_textbox.grid(column=1,row=1,columnspan=2)

email_textbox=tkinter.Entry()
email_textbox.config(width="35")
email_textbox.insert(0, string="angela@email.com")
email_textbox.grid(column=1,row=2,columnspan=2)

password_textbox=tkinter.Entry()
password_textbox.config(width="21")
password_textbox.grid(column=1,row=3)

generate_password=tkinter.Button(command=generate_password,text="Generate Password")
generate_password.grid(column=3,row=4)

search=tkinter.Button(command=search,text="Search")
search.grid(column=3,row=1)

add=tkinter.Button(command=add,text="Add")
add.config(width="36")
add.grid(column=1,row=5,columnspan=2)





















window.mainloop()
