from tkinter import Tk, Label, Button, Entry, StringVar, OptionMenu
import tkinter.messagebox as messagebox

def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            if mode == "encrypt":
                shifted_char = chr((ord(char) - base + shift) % 26 + base)
            else:  # For decryption
                shifted_char = chr((ord(char) - base - shift) % 26 + base)
            result += shifted_char
        else:
            result += char
    return result

def encrypt_decrypt():
    message = entry_message.get()
    shift = int(entry_shift.get())
    mode = mode_var.get()

    if mode not in ["encrypt", "decrypt"]:
        messagebox.showerror("Error", "Invalid mode. Please use either 'encrypt' or 'decrypt'.")
        return

    try:
        output = caesar_cipher(message, shift, mode)
        output_var.set(output)
    except ValueError:
        messagebox.showerror("Error", "Invalid shift value. Please enter an integer.")

# Create GUI window
window = Tk()
window.title("Caesar Cipher")

# Labels
Label(window, text="Message:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
Label(window, text="Shift value:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
Label(window, text="Mode:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
Label(window, text="Output:").grid(row=3, column=0, padx=5, pady=5, sticky="e")

# Entry fields
entry_message = Entry(window, width=40)
entry_message.grid(row=0, column=1, padx=5, pady=5)
entry_shift = Entry(window, width=10)
entry_shift.grid(row=1, column=1, padx=5, pady=5)

# Mode dropdown
mode_var = StringVar(window)
mode_var.set("encrypt")
mode_dropdown = OptionMenu(window, mode_var, "encrypt", "decrypt")
mode_dropdown.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# Output field
output_var = StringVar(window)
output_label = Label(window, textvariable=output_var, wraplength=300, justify="left")
output_label.grid(row=3, column=1, padx=5, pady=5, sticky="w")

# Encrypt/Decrypt button
encrypt_button = Button(window, text="Encrypt/Decrypt", command=encrypt_decrypt)
encrypt_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Start GUI event loop
window.mainloop()
