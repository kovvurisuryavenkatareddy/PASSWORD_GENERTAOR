import random
import string
import tkinter as tk
from tkinter import messagebox
def generate_password():
    # Get the desired length of the password from the Entry widget
    length = int(length_entry.get())
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password by selecting characters randomly
    password = ''.join(random.choice(characters) for _ in range(length))
    # Show the generated password in the password_entry widget
    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, password)
# Create the main Tkinter window
window = tk.Tk()
window.title("Password Generator")
# Increase the window size
window.geometry("400x200")
# Create a label and an entry widget for the password length
length_label = tk.Label(window, text="Enter the length of the password:", font=("Arial", 12))
length_label.pack()
length_entry = tk.Entry(window, font=("Arial", 12))
length_entry.pack()
# Create a button to generate the password
generate_button = tk.Button(window, text="Generate Password", command=generate_password, font=("Arial", 12))
generate_button.pack()
# Create a label and an entry widget to display the generated password
password_label = tk.Label(window, text="Generated Password:", font=("Arial", 12))
password_label.pack()
password_entry = tk.Entry(window, font=("Arial", 12))
password_entry.pack()
# Run the Tkinter event loop
window.mainloop()