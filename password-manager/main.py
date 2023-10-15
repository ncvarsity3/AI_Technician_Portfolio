from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = ["".join(choice(letters)) for char in range(randint(8, 10))]
    symbol_list = ["".join(choice(symbols)) for char in range(randint(2, 4))]
    number_list = ["".join(choice(numbers)) for char in range(randint(2, 4))]

    password_list = letter_list+symbol_list+number_list

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    pword = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": pword,
        }

    }

    if len(website) == 0 or len(pword) == 0:
        messagebox.showinfo(title="Account Error", message="Please don't leave any fields empty!")

    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()
# ---------------------------- PASSWORD SEARCH ------------------------------- #
def find_password():
    website = website_entry.get()

    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")

    else:
        if website in data:
            messagebox.showinfo(title="Found Password", message=f"Your password for {website} is {data[website]['password']}")

        else:
            messagebox.showinfo(title="Error", message=f"There is no password for {website} yet.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title(string="Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
bg_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_img)
canvas.grid(column=1, row=0)

######## Labels ########
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

######## Entries ########
website_entry = Entry(width=24)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=24)
email_entry.insert(0, "ncvarsity3@gmail.com")
email_entry.grid(row=2, column=1)

password_entry = Entry(width=24)
password_entry.grid(row=3, column=1)

######## Buttons ########
password_generate_button = Button(text="Generate Password", width=14, command=generate_password)
password_generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=20, command=save)
add_button.grid(row=4, column=1)

search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(row=1, column=2)




window.mainloop()
