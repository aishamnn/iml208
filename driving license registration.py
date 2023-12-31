import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class DrivingLicenseRegistrationApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Driving License Registration")

        self.tree = ttk.Treeview(master, columns=("Name", "Age", "License Number", "Phone", "Gender"), show="headings", height=10)
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("License Number", text="License Number")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Gender", text="Gender")
        self.tree.pack(pady=10)

        add_button = ttk.Button(master, text="Add", command=self.add_driver)
        update_button = ttk.Button(master, text="Update", command=self.update_driver)
        delete_button = ttk.Button(master, text="Delete", command=self.delete_driver)

        add_button.pack(pady=5)
        update_button.pack(pady=5)
        delete_button.pack(pady=5)

        self.populate_data()

    def populate_data(self):
        # Data for demonstration
        data = [
            ("Nur Iman", 25, "DL92938909", "0178229099", "Female"),
            ("Muhammad Iqbal", 33, "DL92389098", "0163227377", "Male"),
            ("Aisha Aamanna", 19, "DL12345656", "01162137436", "Female")
        ]

        for item in data:
            self.tree.insert("", tk.END, values=item)

    def add_driver(self):
        new_driver = simpledialog.askstring("Add Driver", "Enter driver details (Name - Age - License Number - Phone - Gender):")
        if new_driver:
            details = new_driver.split(" - ")
            if len(details) == 5:
                self.tree.insert("", tk.END, values=details)
            else:
                messagebox.showerror("Error", "Invalid input format.")

    def update_driver(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_item = self.tree.item(selected_item, "values")
            updated_driver = simpledialog.askstring("Update Driver", "Enter updated driver details (Name - Age - License Number - Phone - Gender):",
                                                    initialvalue=" - ".join(map(str, selected_item)))
            if updated_driver:
                details = updated_driver.split(" - ")
                if len(details) == 5:
                    self.tree.item(selected_item, values=details)
                else:
                    messagebox.showerror("Error", "Invalid input format.")
        else:
            messagebox.showerror("Error", "Please select a driver to update.")

    def delete_driver(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirmation = messagebox.askyesno("Delete Driver", "Are you sure you want to delete this driver?")
            if confirmation:
                self.tree.delete(selected_item)
        else:
            messagebox.showerror("Error", "Please select a driver to delete.")


if __name__ == "__main__":
    root = tk.Tk()
    app = DrivingLicenseRegistrationApp(root)
    root.mainloop()
