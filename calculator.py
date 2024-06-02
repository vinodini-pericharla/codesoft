import tkinter as tk

# Initialize main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600+500+100")
root.resizable(False, False)
root.configure(bg="gray")

equation = ""

def clear():
    global equation
    equation = ""
    label_input.config(text=equation)
    label_result.config(text="")

def show(value):
    global equation
    equation += value
    label_input.config(text=equation)

def backspace():
    global equation
    equation = equation[:-1]
    label_input.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation:
        try:
            result = str(eval(equation))
            equation = result
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)

# Input display label
label_input = tk.Label(root, text="", font=("Arial", 18), anchor='e', bg="white", fg="black", padx=10, pady=5)
label_input.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Result display label
label_result = tk.Label(root, text="", font=("Arial", 24), anchor='e', bg="white", fg="black", padx=10, pady=10)
label_result.grid(row=1, column=0, columnspan=4, sticky="nsew")

# Button specifications
buttons = [
    ('C', 2, 0, clear), ('/', 2, 1, lambda: show("/")), ('%', 2, 2, lambda: show("%")), ('⬅', 2, 3, backspace),
    ('7', 3, 0, lambda: show("7")), ('8', 3, 1, lambda: show("8")), ('9', 3, 2, lambda: show("9")), ('*', 3, 3, lambda: show("*")),
    ('4', 4, 0, lambda: show("4")), ('5', 4, 1, lambda: show("5")), ('6', 4, 2, lambda: show("6")), ('-', 4, 3, lambda: show("-")),
    ('1', 5, 0, lambda: show("1")), ('2', 5, 1, lambda: show("2")), ('3', 5, 2, lambda: show("3")), ('+', 5, 3, lambda: show("+")),
    ('0', 6, 0, lambda: show("0"), 1, 2), ('.', 6, 2, lambda: show(".")), ('=', 6, 3, calculate)
]

# Add buttons to the grid
for button in buttons:
    if len(button) == 4:
        text, row, col, cmd = button
        rowspan, colspan = 1, 1
    elif len(button) == 5:
        text, row, col, cmd, colspan = button
        rowspan = 1
    elif len(button) == 6:
        text, row, col, cmd, rowspan, colspan = button
    
    btn = tk.Button(root, text=text, command=cmd, font=("Arial", 18), bg="lightgray", fg="black")
    btn.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky="nsew", padx=5, pady=5)

# Grid configuration for responsiveness
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
