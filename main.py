FONT = ("Courier", 14, "bold")
# UI Setup
from tkinter import *

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

pass_btn = Button(text="Generate Password")
pass_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=31, command=add_password)
add_btn.grid(column=1, row=4, columnspan=2, sticky="ew")



window.mainloop()