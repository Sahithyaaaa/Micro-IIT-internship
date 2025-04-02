import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

def get_key():
    key_path = "secret.key"
    if not os.path.exists(key_path):
        with open(key_path, "wb") as key_file:
            key_file.write(Fernet.generate_key())
            messagebox.showinfo("Key Generated", "Encryption key saved as secret.key")
    else:
        messagebox.showinfo("Key Exists", "Encryption key saved as secret.key already exists")        
    with open(key_path, "rb") as key_file:
        return key_file.read()

def process_file(encrypt):
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    try:
        with open(file_path, "rb") as file:
            data = file.read()
        fernet = Fernet(get_key())
        processes_data = fernet.encrypt(data) if encrypt else fernet.decrypt(data)

        new_file_path = f"{file_path}{'.enc' if encrypt else '_decrypted'}"
        with open(new_file_path, "wb") as new_file:
            new_file.write(processes_data)    

        messagebox.showinfo("Success", f"File {'encrypted' if encrypt else 'decrypted'} successfullyy! saved as {new_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Operation failed: {e}")

def setup_gui():
    root = tk.Tk()
    root.title("File Encryption/Decryptuion Tool")
    root.geometry("400x250")
    root.config(bg="#f0f0f0")

    for text, cmd, color in [
        ("Generate Key", get_key, "#4CAF50"),
        ("Encrypt File", lambda: process_file(True), "#2196F3"),
        ("Decrypt File", lambda: process_file(False), "#FF5722")
    ]:
        tk.Button(root, text=text, command=cmd, width=20, height=2, bg=color, fg="white").pack(pady=5)
    root.mainloop()
setup_gui()
