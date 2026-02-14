import tkinter as tk
from tkinter import messagebox

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# Create main window
root = tk.Tk()
root.title("Simple Add Calculator")

# Window size
window_width = 300
window_height = 200

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate center position
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

# Set geometry
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Disable resizing
root.resizable(False, False)

# Labels and Entry fields
tk.Label(root, text="Enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()

# Add Button
tk.Button(root, text="Add", command=add_numbers).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="Result: ")
result_label.pack()

# Run the app
root.mainloop()
