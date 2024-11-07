# ui.py
import tkinter as tk
from tkinter import messagebox
from db import insert_contact, fetch_contacts, update_contact, delete_contact


class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")

        # Input fields
        tk.Label(root, text="Name").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Phone").grid(row=1, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1)

        tk.Label(root, text="Email").grid(row=2, column=0)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1)

        # Buttons
        tk.Button(root, text="Add Contact", command=self.add_contact).grid(row=3, column=0)
        tk.Button(root, text="Edit Contact", command=self.edit_contact).grid(row=3, column=1)
        tk.Button(root, text="Delete Contact", command=self.remove_contact).grid(row=3, column=2)

        # Contact List
        self.contact_listbox = tk.Listbox(root, width=50)
        self.contact_listbox.grid(row=4, column=0, columnspan=3)

        self.fetch_contacts()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name and phone and email:
            insert_contact(name, phone, email)
            self.clear_entries()
            self.fetch_contacts()
        else:
            messagebox.showwarning("Input Error", "All fields are required")

    def edit_contact(self):
        selected = self.contact_listbox.curselection()
        if selected:
            contact = self.contact_listbox.get(selected[0])
            contact_id = contact.split(" - ")[0]
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            update_contact(contact_id, name, phone, email)
            self.clear_entries()
            self.fetch_contacts()
        else:
            messagebox.showwarning("Selection Error", "No contact selected")

    def remove_contact(self):
        selected = self.contact_listbox.curselection()
        if selected:
            contact = self.contact_listbox.get(selected[0])
            contact_id = contact.split(" - ")[0]
            delete_contact(contact_id)
            self.clear_entries()
            self.fetch_contacts()
        else:
            messagebox.showwarning("Selection Error", "No contact selected")

    def fetch_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        contacts = fetch_contacts()
        for contact in contacts:
            self.contact_listbox.insert(tk.END, f"{contact[0]} - {contact[1]} - {contact[2]} - {contact[3]}")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
