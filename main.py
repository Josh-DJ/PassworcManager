from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ------------- Generate Password ------
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    pass_ltr = [random.choice(letters) for _ in range(nr_letters)]
    num_ltr = [random.choice(numbers) for _ in range(nr_numbers)]
    sym_ltr = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = pass_ltr + num_ltr + sym_ltr
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    pass_entry.insert(0, password)


# -------------- Add Password ----------
def add_password():
    # Save values
    web = web_entry.get()
    email = user_entry.get()
    pw = pass_entry.get()

    if len(web) == 0 or len(pw) == 0:
        messagebox.showwarning(title="Warning", message="Please fill out all fields.")

    else:
        approve = messagebox.askokcancel(title="Information", message=f"These are the details entered: \n Email: {email} \n"
                                                                  f" Password:{pw} \n Is this okay?")

    if approve:
        # Save items to file
        with open("data.txt", "a+") as file:
            file.write(web + " | " + email + " | " + pw + "\n")
            # Delete values from GUI
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------UI Setup----------------
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width= 200, height= 200, highlightthickness=0)
lock_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_png)
canvas.grid(column=1, row=0)

#Labels
web_lbl = Label(text="Website:")
web_lbl.grid(column=0, row=1)

user_lbl = Label(text="Email/Username:")
user_lbl.grid(column=0, row=2)

pass_lbl = Label(text="Password:")
pass_lbl.config(padx=10)
pass_lbl.grid(column=0, row=3)

#Widgets
web_entry = Entry(textvariable="Website", width=35)
web_entry.grid(column=1, row= 1, columnspan=2, sticky="ew")
web_entry.focus()

user_entry = Entry(textvariable="User", width=35)
user_entry.grid(column=1, row= 2, columnspan=2, sticky="ew")
user_entry.insert(0,"test@example.com") # Pre-populates email name

pass_entry = Entry(textvariable="Password", width=24)
pass_entry.grid(column=1, row=3, sticky="ew")

pass_btn = Button(text="Generate Password", command=gen_password)
pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=31, command=add_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky="ew")



window.mainloop()