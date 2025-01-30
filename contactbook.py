import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, root):
        self.contact_data = []
        self.window = root
        self.window.title("Contact Manager")
        self.window.geometry("550x450")

        self.create_widgets()

    def create_widgets(self):
        # Labels and Entry Fields
        self.name_label = tk.Label(self.window, text="Full Name:")
        self.name_label.grid(row=0, column=0, padx=15, pady=10)
        self.name_input = tk.Entry(self.window)
        self.name_input.grid(row=0, column=1, padx=15, pady=10)

        self.phone_label = tk.Label(self.window, text="Phone Number:")
        self.phone_label.grid(row=1, column=0, padx=15, pady=10)
        self.phone_input = tk.Entry(self.window)
        self.phone_input.grid(row=1, column=1, padx=15, pady=10)

        self.email_label = tk.Label(self.window, text="Email:")
        self.email_label.grid(row=2, column=0, padx=15, pady=10)
        self.email_input = tk.Entry(self.window)
        self.email_input.grid(row=2, column=1, padx=15, pady=10)

        self.address_label = tk.Label(self.window, text="Address:")
        self.address_label.grid(row=3, column=0, padx=15, pady=10)
        self.address_input = tk.Entry(self.window)
        self.address_input.grid(row=3, column=1, padx=15, pady=10)

        # Buttons
        self.add_button = tk.Button(self.window, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=15)

        self.view_button = tk.Button(self.window, text="Show Contacts", command=self.display_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.search_label = tk.Label(self.window, text="Search (Name/Phone):")
        self.search_label.grid(row=6, column=0, padx=15, pady=10)
        self.search_input = tk.Entry(self.window)
        self.search_input.grid(row=6, column=1, padx=15, pady=10)

        self.search_button = tk.Button(self.window, text="Search", command=self.search_contacts)
        self.search_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(self.window, text="Delete Contact", command=self.remove_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2, pady=10)

        # Contact Listbox to display contacts
        self.contact_listbox = tk.Listbox(self.window, height=10, width=50)
        self.contact_listbox.grid(row=9, column=0, columnspan=2, padx=15, pady=10)

    def add_contact(self):
        name = self.name_input.get()
        phone = self.phone_input.get()
        email = self.email_input.get()
        address = self.address_input.get()

        if name and phone:
            new_contact = {"name": name, "phone": phone, "email": email, "address": address}
            self.contact_data.append(new_contact)
            messagebox.showinfo("Success", "Contact successfully added!")
            self.clear_inputs()
        else:
            messagebox.showwarning("Input Error", "Name and Phone Number are required fields.")

    def display_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        for contact in self.contact_data:
            contact_info = f"{contact['name']} - {contact['phone']}"
            self.contact_listbox.insert(tk.END, contact_info)

    def search_contacts(self):
        search_term = self.search_input.get().lower()
        self.contact_listbox.delete(0, tk.END)

        results = [contact for contact in self.contact_data if 
                   search_term in contact['name'].lower() or search_term in contact['phone']]

        if results:
            for contact in results:
                contact_info = f"{contact['name']} - {contact['phone']}"
                self.contact_listbox.insert(tk.END, contact_info)
        else:
            messagebox.showinfo("No Results", "No contacts match your search criteria.")

    def remove_contact(self):
        selected_contact_index = self.contact_listbox.curselection()

        if selected_contact_index:
            contact_index = selected_contact_index[0]
            del self.contact_data[contact_index]
            self.contact_listbox.delete(contact_index)
            messagebox.showinfo("Deleted", "Contact successfully removed!")
        else:
            messagebox.showwarning("No Selection", "Please select a contact to delete.")

    def clear_inputs(self):
        self.name_input.delete(0, tk.END)
        self.phone_input.delete(0, tk.END)
        self.email_input.delete(0, tk.END)
        self.address_input.delete(0, tk.END)
        self.search_input.delete(0, tk.END)


if __name__ == "__main__":
    root_window = tk.Tk()
    app = ContactManager(root_window)
    root_window.mainloop()