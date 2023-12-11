from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = []
    password_symbols = []
    password_numbers = []

    password_letters = [choice(letters) for _ in range(randint(5, 7))]
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #     password += char

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)


def find_password():
    search_item = website_entry.get()

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            messagebox.showinfo(title="Website Details", message=f"Website name: {search_item}\n"
                                                                 f"Username: {data[search_item]['email']}\n"
                                                                 f"Password: {data[search_item]['password']}")
            print(data[search_item]["email"])
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found!")
    except KeyError:
        messagebox.showerror(title="Error", message="No details for the website")
    else:
        pass
    finally:
        pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(website) == 0:
        messagebox.showerror(title="ERROR", message="Website name or Password is empty!")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)  # Reading old data
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)  # Saving updated data
        else:
            data.update(new_data)  # Updating the old data with new data
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)  # Saving updated data
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


pass_man = Tk()
pass_man.title("Password Manager")
pass_man.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

search_btn = Button(text="Search", width=10, command=find_password)
search_btn.grid(row=1, column=2)

website_entry = Entry(width=23)
website_entry.grid(row=1, column=1)
website_entry.focus()

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

username_entry = Entry(width=42)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0, "mkaudi@gmail.com")

passwrd_label = Label(text="Password:")
passwrd_label.grid(row=3, column=0)

password_entry = Entry(width=23)
password_entry.grid(row=3, column=1)

generate_btn = Button(text="Generate Password", width=14, command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=35, command=add_password)
add_btn.grid(row=4, column=1, columnspan=2)

pass_man.mainloop()
