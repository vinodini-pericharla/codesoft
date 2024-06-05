import tkinter as tk
from tkinter import ttk

contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()
    category = selected_category.get()
    if name and phone:
        if not phone.isdigit():
            error_message.config(text="Error: Phone number should contain only digits.")
            return
        contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address, 'category': category})
        update_contact_list()
        clear_entries()
        error_message.config(text="")
    else:
        error_message.config(text="Error: Name and phone are required fields.")

def update_contact():
    index = selected_contact_index.get()
    if index >= 0:
        if not entry_phone.get().isdigit():
            error_message.config(text="Error: Phone number should contain only digits.")
            return
        contacts[index] = {
            'name': entry_name.get(),
            'phone': entry_phone.get(),
            'email': entry_email.get(),
            'address': entry_address.get(),
            'category': selected_category.get()
        }
        update_contact_list()
        clear_entries()
        error_message.config(text="")
    else:
        error_message.config(text="Error: No contact selected for update.")

def delete_contact():
    index = selected_contact_index.get()
    if index >= 0:
        del contacts[index]
        update_contact_list()
        clear_entries()
        error_message.config(text="")
    else:
        error_message.config(text="Error: No contact selected for deletion.")

def search_contact():
    query = entry_search.get().lower()
    contact_list.delete(*contact_list.get_children())
    found = False
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contact_list.insert('', tk.END, values=(contact['name'], contact['phone'], contact['category']))
            found = True
    if not found:
        error_message.config(text="Error: Contact not found.")

def update_contact_list():
    contact_list.delete(*contact_list.get_children())
    for contact in contacts:
        contact_list.insert('', tk.END, values=(contact['name'], contact['phone'], contact['category']))

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)
    selected_category.set(categories[0])
    error_message.config(text="")

def on_contact_select(event):
    selected_item = contact_list.selection()
    if selected_item:
        contact = contact_list.item(selected_item)['values']
        if contact:
            contact_name = contact[0]
            for c in contacts:
                if c['name'] == contact_name:
                    entry_name.delete(0, tk.END)
                    entry_name.insert(0, c['name'])
                    entry_phone.delete(0, tk.END)
                    entry_phone.insert(0, c['phone'])
                    entry_email.delete(0, tk.END)
                    entry_email.insert(0, c['email'])
                    entry_address.delete(0, tk.END)
                    entry_address.insert(0, c['address'])
                    selected_category.set(c['category'])
                    selected_contact_index.set(contacts.index(c))
                    error_message.config(text="")
                    break

window = tk.Tk()
window.title("Contact Book")
window.geometry("700x400")
window.configure(bg="#f0f0f0") 

style = ttk.Style()
style.theme_use("clam")
style.configure('TLabel', font=('Helvetica', 12), background='#f0f0f0')
style.configure('TButton', font=('Helvetica', 12), background='#1565c0', foreground='#ffffff') 
style.configure('Treeview', font=('Helvetica', 10), rowheight=25)
style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'))
style.map('TButton', background=[('active', '#004ba0')]) 

details_frame = tk.Frame(window, bg="#f0f0f0") 
details_frame.pack(side="top", fill="x", padx=20, pady=20)

lbl_name = ttk.Label(details_frame, text="Name:", background='#f0f0f0') 
lbl_name.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
entry_name = ttk.Entry(details_frame, width=30)
entry_name.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

lbl_phone = ttk.Label(details_frame, text="Phone:", background='#f0f0f0')  
lbl_phone.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_phone = ttk.Entry(details_frame, width=30)
entry_phone.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

lbl_email = ttk.Label(details_frame, text="Email:", background='#f0f0f0') 
lbl_email.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
entry_email = ttk.Entry(details_frame, width=30)
entry_email.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

lbl_address = ttk.Label(details_frame, text="Address:", background='#f0f0f0')  
lbl_address.grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
entry_address = ttk.Entry(details_frame, width=30)
entry_address.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

lbl_category = ttk.Label(details_frame, text="Category:", background='#f0f0f0')  
lbl_category.grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
selected_category = tk.StringVar()
categories = ["Friends", "Family", "Work"]
selected_category.set(categories[0])
category_dropdown = ttk.OptionMenu(details_frame, selected_category, *categories)
category_dropdown.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
details_frame.columnconfigure(1, weight=1)

search_frame = tk.Frame(window, bg="#f0f0f0")  
search_frame.pack(side="top", fill="x", padx=20, pady=10)

lbl_search = ttk.Label(search_frame, text="Search:", background='#f0f0f0') 
lbl_search.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry_search = ttk.Entry(search_frame, width=30)
entry_search.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

btn_search = ttk.Button(search_frame, text="Search", command=search_contact)
btn_search.grid(row=0, column=2, padx=5, pady=5)

contact_list_frame = tk.Frame(window, bg="#f0f0f0")  
contact_list_frame.pack(side="top", fill="both", expand=True, padx=20, pady=10)

contact_list = ttk.Treeview(contact_list_frame, columns=('name', 'phone', 'category'), show='headings', selectmode='browse')
contact_list.heading('name', text='Name')
contact_list.heading('phone', text='Phone')
contact_list.heading('category', text='Category')
contact_list.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(contact_list_frame, orient="vertical", command=contact_list.yview)
scrollbar.pack(side="right", fill="y")
contact_list.configure(yscrollcommand=scrollbar.set)

contact_list.bind("<<TreeviewSelect>>", on_contact_select)

btn_frame = tk.Frame(window, bg="#f0f0f0")  
btn_frame.pack(side="top", padx=20, pady=10)

btn_add = ttk.Button(btn_frame, text="Add Contact", command=add_contact)
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_update = ttk.Button(btn_frame, text="Update Contact", command=update_contact)
btn_update.grid(row=0, column=1, padx=5, pady=5)

btn_delete = ttk.Button(btn_frame, text="Delete Contact", command=delete_contact)
btn_delete.grid(row=0, column=2, padx=5, pady=5)

error_message = tk.Label(window, text="", fg="red", bg="#f0f0f0")  
error_message.pack(side="top", padx=20, pady=10)

selected_contact_index = tk.IntVar(value=-1)

window.mainloop()
