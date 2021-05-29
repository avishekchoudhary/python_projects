from tkinter import *
from tkinter import messagebox
import random
import json
from typing import final
# import pyperclip





# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_passwd():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letter = ([random.choice(letters) for num in range(nr_letters)])
    password_symbol = ([random.choice(symbols) for num in range(nr_symbols)])
    password_numbers = ([random.choice(numbers) for num in range(nr_numbers)])

    password_list = password_letter+password_symbol+password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    passwd_entry.insert(0, password)
    # pyperclip.copy(password) #copies newly generated password to your clipborad

def search():
    web_name = web_entry.get()
    try:
        with open('./manager.json', 'r') as file:
            data_file = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No data file found')
    else:
        if web_name in data_file:
            messagebox.showinfo(title='Info', message=f'email:{data_file[web_name]["email"]}\nPassword:{data_file[web_name]["password"]}')
        else:
            messagebox.showerror(title='Error', message="Requested credentials doesn't exist in Database")                 

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = web_entry.get()
    email = mail_entry.get()
    password = passwd_entry.get()

    data = {
        website:
                {
                    'email':email,
                    'password': password
                }
}


    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Error', message="Website or Password feilds can't be empty")
    else:
        is_true = messagebox.askokcancel(title=f'{website}', message=f'Following are the details you have entered:\n Email: {email}\n Password: {password}\n Is it ok to you🐱‍👤👍')
        if is_true == True:
            try:
                with open('./manager.json', 'r') as file:
                    file_data = json.load(file)
            except FileNotFoundError:
                with open('./manager.json', 'w') as file:
                    json.dump(data, file, indent=4)    
            else:    
                file_data.update(data)
                with open('./manager.json', 'w') as file:
                    json.dump(file_data,file,indent=4)

            finally:
                web_entry.delete(0,END)
                passwd_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Psswd Manager')
window.config(padx=60,pady=60)

canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text='Website')
website_label.grid(column=0, row=1)

web_entry = Entry(width=35)
web_entry.grid(column=1,row=1)
web_entry.focus()

search_button = Button(text='Search',width=10,command=search)
search_button.grid(column=2,row=1)

email_label = Label(text='Email/Username')
email_label.grid(column=0, row=2)

mail_entry = Entry(width=35)
mail_entry.grid(column=1, row=2)
mail_entry.insert(0, 'chindichor@gmail.com')

passwd_label = Label(text="Password")
passwd_label.grid(column=0,row=3)

passwd_entry = Entry(width=35)
passwd_entry.grid(column=1,row=3)

gen_button = Button(text='Generate Password', command=gen_passwd,width=20)
gen_button.grid(column=2,row=3)


add_button = Button(text='Add', width=30, command= add)
add_button.grid(column=1,row=4)




window.mainloop()