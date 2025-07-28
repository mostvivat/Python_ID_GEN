import tkinter as tk
from tkinter import messagebox
import random

def generate_thai_id():
    digits = [random.randint(1, 8)]  # First digit cannot be 0 or 9
    for _ in range(11):
        digits.append(random.randint(0, 9))
    
    # Calculate checksum
    total = sum([digits[i] * (13 - i) for i in range(12)])
    checksum = (11 - (total % 11)) % 10
    digits.append(checksum)

    return ''.join(str(d) for d in digits)

def on_generate():
    id_var.set(generate_thai_id())

# Create GUI
root = tk.Tk()
root.title("Thai ID Card Number Generator")
root.geometry("350x150")

id_var = tk.StringVar()

label = tk.Label(root, text="Generated Thai ID Number:", font=('Arial', 12))
label.pack(pady=10)

entry = tk.Entry(root, textvariable=id_var, font=('Arial', 14), width=25, justify='center')
entry.pack()

generate_btn = tk.Button(root, text="Generate ID Card Number", command=on_generate, font=('Arial', 12))
generate_btn.pack(pady=10)

root.mainloop()
