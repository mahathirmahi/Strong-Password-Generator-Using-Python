import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = int(length_entry.get())

    if length < 8:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Password length should be at least 8 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    root.clipboard_clear()  # Clear the clipboard to ensure it's clean
    root.clipboard_append(password)  # Append the password to the clipboard
    root.update()  # Update the clipboard to reflect the changes

# Create the main window
root = tk.Tk()
root.title("Strong Password Generator")

# Create widgets
length_label = ttk.Label(root, text="Password Length:")
length_entry = ttk.Entry(root)
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
password_label = ttk.Label(root, text="Generated Password:")
password_entry = ttk.Entry(root)
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)

# Arrange widgets using grid layout manager
length_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
length_entry.grid(row=0, column=1, padx=5, pady=5)
generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="we")
password_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
password_entry.grid(row=2, column=1, padx=5, pady=5, sticky="we")
copy_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="we")

# Set resize behavior
root.columnconfigure(1, weight=1)

# Run the application
root.mainloop()
