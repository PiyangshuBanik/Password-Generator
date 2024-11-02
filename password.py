import tkinter as tk
import random
import string
import pyperclip  # Requires installation of pyperclip for clipboard functionality

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Secure Password Generator")
        self.master.geometry("700x700")
        self.master.configure(bg="#f0f0f0")  # Light background color

        # Title label
        self.title_label = tk.Label(master, text="Piyangshu's Secure Password Generator", bg="#4CAF50", fg="white", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)

        # Password length input
        self.length_label = tk.Label(master, text="Password Length:", bg="#f0f0f0", font=("Arial", 14))
        self.length_label.pack(pady=5)
        self.length_entry = tk.Entry(master, font=("Arial", 14), width=10)
        self.length_entry.pack(pady=5)

        # Character type checkboxes
        self.uppercase_var = tk.BooleanVar()
        self.uppercase_checkbox = tk.Checkbutton(master, text="Include Uppercase Letters", variable=self.uppercase_var, bg="#f0f0f0", font=("Arial", 12))
        self.uppercase_checkbox.pack(pady=5)

        self.numbers_var = tk.BooleanVar()
        self.numbers_checkbox = tk.Checkbutton(master, text="Include Numbers", variable=self.numbers_var, bg="#f0f0f0", font=("Arial", 12))
        self.numbers_checkbox.pack(pady=5)

        self.symbols_var = tk.BooleanVar()
        self.symbols_checkbox = tk.Checkbutton(master, text="Include Symbols", variable=self.symbols_var, bg="#f0f0f0", font=("Arial", 12))
        self.symbols_checkbox.pack(pady=5)

        # Generate password button
        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password, bg="#4CAF50", fg="white", font=("Arial", 14), relief="raised")
        self.generate_button.pack(pady=15)

        # Password display area
        self.password_label = tk.Label(master, text="Generated Password:", bg="#f0f0f0", font=("Arial", 14))
        self.password_label.pack(pady=5)
        self.password_text = tk.Text(master, height=5, width=40, font=("Arial", 14), bg="#e0e0e0", relief="sunken")
        self.password_text.pack(pady=5)

        # Copy to clipboard button
        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard, bg="#4CAF50", fg="white", font=("Arial", 14))
        self.copy_button.pack(pady=10)

        # Clear button
        self.clear_button = tk.Button(master, text="Clear", command=self.clear_fields, bg="#FF5733", fg="white", font=("Arial", 14))
        self.clear_button.pack(pady=10)

    def generate_password(self):
        length = int(self.length_entry.get())
        use_uppercase = self.uppercase_var.get()
        use_numbers = self.numbers_var.get()
        use_symbols = self.symbols_var.get()

        character_pool = string.ascii_lowercase  # Start with lowercase letters

        if use_uppercase:
            character_pool += string.ascii_uppercase
        if use_numbers:
            character_pool += string.digits
        if use_symbols:
            character_pool += string.punctuation

        if length < 1 or length > 128:
            self.password_text.delete(1.0, tk.END)
            self.password_text.insert(tk.END, "Password length must be between 1 and 128.")
            return

        password = ''.join(random.choice(character_pool) for _ in range(length))
        self.password_text.delete(1.0, tk.END)
        self.password_text.insert(tk.END, password)

    def copy_to_clipboard(self):
        password = self.password_text.get(1.0, tk.END)
        pyperclip.copy(password)

    def clear_fields(self):
        self.length_entry.delete(0, tk.END)
        self.uppercase_var.set(False)
        self.numbers_var.set(False)
        self.symbols_var.set(False)
        self.password_text.delete(1.0, tk.END)

root = tk.Tk()
app = PasswordGeneratorApp(root)
root.mainloop()