import  tkinter as tk

import random
import string

window = tk.Tk()

window.title(" Password Generator ")
window.geometry("500x400")

title_label = tk.Label(
    window,
    text="Password Generator",
    font=("Arial", 30)
    )
title_label.pack(padx=20)
Password_Length_label = tk.Label(
    window,
    text="Password_Length (m):"
)
Password_Length_label.pack()

Password_Length_entry=tk.Entry(window)
Password_Length_entry.pack(pady=10)

generated_password = ""

def generate_password():
    global generated_password
    try:
        Password_Length=int(Password_Length_entry.get())
        if Password_Length< 8:
            result_label.config (
            text="invalid password length .\n Minimum 8"
        )
            return
        character = string.ascii_letters + string.digits+"!@#$%^&*"
        generated_password = ''.join(
            random.choice(character) 
            for i in range(Password_Length))
    
        result_label.config(
            text=f"Generated Password:\n{generated_password}"
        )
    
    except ValueError:
        result_label.config(
            text="Please enter a valid number.")
        
   

def copy_password():
    if generated_password == "":
        result_label.config(
            text="Please generate a password first."
        )
        return

    window.clipboard_clear()
    window.clipboard_append(generated_password)
    window.update()

    result_label.config(
        text="Password copied to clipboard!"
    )

calculate_button = tk.Button(
    window,
    text="Generate Password",
    command=generate_password
)
calculate_button.pack(pady=20)

copy_button= tk.Button(
    window,
    text="Copy Password",
    command=copy_password
)
copy_button.pack(pady=10)



result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12)
)
result_label.pack(pady=10)

window.mainloop()
