from tkinter import Tk, Button, Label, Entry, messagebox
from password_generator import Password_Generator
import json
import pyclip
FONT_NAME = "Arial"
BLACK = "#000000"
LIGHT_GRAY = "#363636"
WHITE = "#FFFFFF"

pass_gen = Password_Generator()


def generate_password():
    user_password_entry.delete(0, len(user_password_entry.get()))
    user_password_entry.insert(0, pass_gen.password_generator())
    pyclip.copy(user_password_entry.get())
    messagebox.showinfo(title="Password Copied", message="Password copied to clipboard.\nPress CTRL V to paste.")


def generate_password_no_symbols():
    user_password_entry.delete(0, len(user_password_entry.get()))
    user_password_entry.insert(0, pass_gen.password_generator_no_symbols())
    pyclip.copy(user_password_entry.get())
    messagebox.showinfo(title="Password Copied", message="Password copied to clipboard.\nPress CTRL V to paste.")



def add_password():
    '''
        checks for blank fields and asks user to input the information

        asks user if they wish to add their credentials or if they want to
        make changes.

        adds the website, user name/email, and password to a text file,
        then clears the entry fields

        saved in passwords.json
        ----------
    '''
    new_password = {
        website_entry.get():{
            "email": user_name_entry.get(),
            "password": user_password_entry.get(),
        }
    }
    if len(website_entry.get()) == 0:
        messagebox.showinfo(title="Missing Information", message="Please enter the website for these credentials.")
    elif len(user_name_entry.get()) == 0:
        messagebox.showinfo(title="Missing Information", message="Please enter the User Name or Email for these credentials.")
    elif len(user_password_entry.get()) == 0:
        messagebox.showinfo(title="Missing Information", message="Please enter the password for these credentials.")
    elif len(user_password_entry.get()) <=7 : 
        messagebox.showinfo(title="Missing Information", message="Password is too short.\nA minimum of 8 alphaumeric characters is recommended.\n\nPress the 'Generate Password' button to generate a password.")
    else:
        try:
            with open("passwords.json", "r") as add_pass:
                data = json.load(add_pass)  # Read file
        except FileNotFoundError:
            with open("passwords.json", "w") as add_pass:
                json.dump(new_password, add_pass, indent=2)
        else:
            data.update(new_password)   # Update data
            with open("passwords.json", "w") as add_pass:
                json.dump(data, add_pass, indent=2) # Add updated data
        finally:
                website_entry.delete(0, len(website_entry.get()))
                #user_name_entry.delete(0, len(user_name_entry.get()))
                user_password_entry.delete(0, len(user_password_entry.get()))


def delete_password():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as loaded_password_file:
            result = json.load(loaded_password_file)
            if website in result:
                del result[website]
                with open("passwords.json", "w") as loaded_password_file:
                    json.dump(result, loaded_password_file, indent=2)
                messagebox.showinfo(title="Information Deleted", message=f"Website: {website}\n\nEntry deleted.")
            else:
                messagebox.showinfo(title="No Entry", message=f"No entry exists for {website}.")
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="No file exists. Add an entry.")
    except KeyError:
        messagebox.showinfo(title="No Entry", message=f"No entry exists for {website}.")


# Search
def search():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as loaded_password_file:
            result = json.load(loaded_password_file)
            if website in result:
                email = result[website]["email"]
                password = result[website]["password"]
            else:
                messagebox.showinfo(title="No Entry", message=f"No entry exists for {website}.")
    except FileNotFoundError:
        messagebox.showinfo(title="File Not Found", message="No file exists. Add an entry.")
    except KeyError:
        messagebox.showinfo(title="No Entry", message=f"No entry exists for {website}.")
    else:
        messagebox.showinfo(title="Information Found", message=f"Website: {website}\n\nEmail/User Name: {email}\n\nPassword: {password}")

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30, bg=BLACK)

# Labels
website_label = Label(text="Website", fg=WHITE, bg=BLACK, font=(FONT_NAME, 16))
website_label.grid(column=0, row=1)

user_name_label = Label(text="User Name/Email", fg=WHITE, bg=BLACK, font=(FONT_NAME, 16))
user_name_label.grid(column=0, row=2)

user_password_label = Label(text="Password", fg=WHITE, bg=BLACK, font=(FONT_NAME, 16))
user_password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=20, bg=LIGHT_GRAY, fg=WHITE, font=(FONT_NAME, 16))
website_entry.focus()
website_entry.grid(column=1, row=1)

user_name_entry = Entry(width=40, bg=LIGHT_GRAY, fg=WHITE, font=(FONT_NAME, 16))
#user_name_entry.insert(0,string="User Name or Email")
user_name_entry.grid(column=1, row=2, columnspan=2)

user_password_entry = Entry(width=20, bg=LIGHT_GRAY, fg=WHITE, font=(FONT_NAME, 16))
user_password_entry.grid(column=1, row=3)

# Buttons
search_btn = Button(text="Search", highlightthickness=0, command=search, width=15, font=(FONT_NAME, 14))
search_btn.grid(column=0, row=4)

password_gen_noS_btn = Button(text="Generate Password no Symbols", highlightthickness=0, command=generate_password_no_symbols, font=(FONT_NAME, 14))
password_gen_noS_btn.grid(column=1, row=4)

password_generator_btn = Button(text="Generate Password with Symbols", highlightthickness=0, command=generate_password, font=(FONT_NAME, 14))
password_generator_btn.grid(column=1, row=5)

add_password_btn = Button(text="Add Password", highlightthickness=0, command=add_password, width=35, font=(FONT_NAME, 14))
add_password_btn.grid(column=3, row=4)

delete_password_btn = Button(text="Delete Password", highlightthickness=0, command=delete_password, width=35, font=(FONT_NAME, 14))
delete_password_btn.grid(column=3, row=5)

window.mainloop()