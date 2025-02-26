import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import encrypt
import decrypt

def encrypt_image():
    image_path = filedialog.askopenfilename(title="Select Image")
    if not image_path:
        return
    message = message_entry.get()
    password = password_entry.get()
    output_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if not output_path:
        return
    try:
        encrypt.embed_message(image_path, message, password, output_path)
        messagebox.showinfo("Success", "Message encrypted successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def decrypt_image():
    image_path = filedialog.askopenfilename(title="Select Image")
    if not image_path:
        return
    password = decrypt_password_entry.get()
    decrypted_message = decrypt.extract_message(image_path, password)
    decrypted_message_label.config(text=decrypted_message)

def update_button_state(*args):
    encrypt_button.config(state="normal" if message_entry.get() and password_entry.get() else "disabled")
    decrypt_button.config(state="normal" if decrypt_password_entry.get() else "disabled")

root = tk.Tk()
root.title("Advanced Image Steganography")
root.geometry("700x400")
root.configure(bg="#f0f0f0")

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)

# Encryption Section
tk.Label(frame, text="Encrypt", font=("Arial", 14)).grid(row=0, column=0, pady=10)
tk.Label(frame, text="Secret Message:").grid(row=1, column=0)
message_entry = tk.Entry(frame, width=30)
message_entry.grid(row=2, column=0, padx=10, pady=5)
tk.Label(frame, text="Password:").grid(row=3, column=0)
password_entry = tk.Entry(frame, width=30, show="*")
password_entry.grid(row=4, column=0, padx=10, pady=5)
encrypt_button = ttk.Button(frame, text="Select Image & Encrypt", command=encrypt_image, state="disabled")
encrypt_button.grid(row=5, column=0, pady=10)

# Decryption Section
tk.Label(frame, text="Decrypt", font=("Arial", 14)).grid(row=0, column=1, pady=10)
tk.Label(frame, text="Password:").grid(row=1, column=1)
decrypt_password_entry = tk.Entry(frame, width=30, show="*")
decrypt_password_entry.grid(row=2, column=1, padx=10, pady=5)
decrypt_button = ttk.Button(frame, text="Select Image & Decrypt", command=decrypt_image, state="disabled")
decrypt_button.grid(row=3, column=1, pady=10)
decrypted_message_label = tk.Label(frame, text="", font=("Arial", 12), wraplength=300, fg="blue")
decrypted_message_label.grid(row=4, column=1, pady=10)

# Trace changes in input fields
message_entry.bind("<KeyRelease>", update_button_state)
password_entry.bind("<KeyRelease>", update_button_state)
decrypt_password_entry.bind("<KeyRelease>", update_button_state)

root.mainloop()
