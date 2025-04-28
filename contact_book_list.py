import tkinter as tk
from tkinter import messagebox, simpledialog

contacts = []

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required fields!")
        return

    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    refresh_contact_list()
    clear_entries()
    messagebox.showinfo("Success", "Contact added successfully!")

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

def refresh_contact_list():
    listbox_contacts.delete(0, tk.END)
    for idx, contact in enumerate(contacts):
        listbox_contacts.insert(tk.END, f"{idx+1}. {contact['name']} - {contact['phone']}")

def search_contact():
    query = entry_search.get().lower()
    listbox_contacts.delete(0, tk.END)
    for idx, contact in enumerate(contacts):
        if query in contact['name'].lower() or query in contact['phone']:
            listbox_contacts.insert(tk.END, f"{idx+1}. {contact['name']} - {contact['phone']}")

def update_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a contact to update.")
        return

    index = selected[0]
    contact = contacts[index]
  
    name = simpledialog.askstring("Update Name", "Enter new name:", initialvalue=contact['name'])
    phone = simpledialog.askstring("Update Phone", "Enter new phone number:", initialvalue=contact['phone'])
    email = simpledialog.askstring("Update Email", "Enter new email:", initialvalue=contact['email'])
    address = simpledialog.askstring("Update Address", "Enter new address:", initialvalue=contact['address'])

    if name and phone:
        contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
        refresh_contact_list()
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showwarning("Input Error", "Name and Phone cannot be empty.")

def delete_contact():
    selected = listbox_contacts.curselection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a contact to delete.")
        return

    index = selected[0]
    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{contacts[index]['name']}'?")
    if confirm:
        del contacts[index]
        refresh_contact_list()
        messagebox.showinfo("Success", "Contact deleted successfully!")

root = tk.Tk()
root.title("Contact Book")
root.geometry("500x600")
root.resizable(False, False)

frame_top = tk.Frame(root)
frame_top.pack(pady=10)

tk.Label(frame_top, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_name = tk.Entry(frame_top, width=40)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(frame_top, text="Phone:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_phone = tk.Entry(frame_top, width=40)
entry_phone.grid(row=1, column=1, pady=5)

tk.Label(frame_top, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_email = tk.Entry(frame_top, width=40)
entry_email.grid(row=2, column=1, pady=5)

tk.Label(frame_top, text="Address:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_address = tk.Entry(frame_top, width=40)
entry_address.grid(row=3, column=1, pady=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="Add Contact", command=add_contact, width=15)
btn_add.grid(row=0, column=0, padx=5)

btn_update = tk.Button(frame_buttons, text="Update Contact", command=update_contact, width=15)
btn_update.grid(row=0, column=1, padx=5)

btn_delete = tk.Button(frame_buttons, text="Delete Contact", command=delete_contact, width=15)
btn_delete.grid(row=0, column=2, padx=5)

frame_search = tk.Frame(root)
frame_search.pack(pady=10)

entry_search = tk.Entry(frame_search, width=30)
entry_search.grid(row=0, column=0, padx=5)

btn_search = tk.Button(frame_search, text="Search", command=search_contact, width=10)
btn_search.grid(row=0, column=1, padx=5)

btn_show_all = tk.Button(frame_search, text="Show All", command=refresh_contact_list, width=10)
btn_show_all.grid(row=0, column=2, padx=5)

frame_listbox = tk.Frame(root)
frame_listbox.pack(pady=10)

listbox_contacts = tk.Listbox(frame_listbox, width=70, height=20)
listbox_contacts.pack()
root.mainloop()
