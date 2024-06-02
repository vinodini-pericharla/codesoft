from tkinter import *
import string
import random

def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    all_characters = small_alphabets + capital_alphabets + numbers + special_characters
    password_length = int(length_Box.get())

    passwordField.config(state=NORMAL)  # Temporarily make the field editable
    passwordField.delete(0, END)

    if choice.get() == 1:
        password = ''.join(random.sample(small_alphabets, password_length))
    elif choice.get() == 2:
        password = ''.join(random.sample(small_alphabets + capital_alphabets, password_length))
    elif choice.get() == 3:
        password = ''.join(random.sample(all_characters, password_length))
    
    passwordField.insert(0, password)
    passwordField.config(state='readonly')  # Make the field readonly again

root = Tk()
root.title("Password Generator")
root.geometry("570x490+500+100")
root.resizable(False, False)
root.config(bg="#f0f0f0")  # Very light grey background

choice = IntVar()

# Centering all widgets within the window
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(3):
    root.grid_columnconfigure(i, weight=1)

passwordLabel = Label(root, text="Password Generator", font=("times new roman", 20, "bold"), bg="#f0f0f0", fg="black")
passwordLabel.grid(row=0, column=0, columnspan=3, pady=10, sticky="n")

weakradioButton = Radiobutton(root, text="Weak", value=1, variable=choice, font=("arial", 13, "bold"), bg="#f0f0f0", fg="black", selectcolor="#f0f0f0", indicatoron=1, relief="flat", highlightbackground="black", highlightcolor="black")
weakradioButton.grid(row=1, column=0, padx=10, pady=10, sticky="n")

mediumradioButton = Radiobutton(root, text="Medium", value=2, variable=choice, font=("arial", 13, "bold"), bg="#f0f0f0", fg="black", selectcolor="#f0f0f0", indicatoron=1, relief="flat", highlightbackground="black", highlightcolor="black")
mediumradioButton.grid(row=1, column=1, padx=10, pady=10, sticky="n")

strongradioButton = Radiobutton(root, text="Strong", value=3, variable=choice, font=("arial", 13, "bold"), bg="#f0f0f0", fg="black", selectcolor="#f0f0f0", indicatoron=1, relief="flat", highlightbackground="black", highlightcolor="black")
strongradioButton.grid(row=1, column=2, padx=10, pady=10, sticky="n")

lengthLabel = Label(root, text="Password Length", font=("arial", 13, "bold"), bg="#f0f0f0", fg="black")
lengthLabel.grid(row=2, column=0, columnspan=3, pady=10, sticky="n")

length_Box = Spinbox(root, from_=5, to_=18, width=5, font=("arial", 13, "bold"))
length_Box.grid(row=3, column=0, columnspan=3, pady=10, sticky="n")

generateButton = Button(root, text="Generate", font=("arial", 13, "bold"), bg="#f0f0f0", fg="black", command=generator)
generateButton.grid(row=4, column=0, columnspan=3, pady=10, sticky="n")

passwordField = Entry(root, width=20, bd=2, font=("arial", 13))
passwordField.grid(row=5, column=0, columnspan=3, pady=10, sticky="n")
passwordField.config(state='readonly')  # Make the field readonly initially

root.mainloop()
