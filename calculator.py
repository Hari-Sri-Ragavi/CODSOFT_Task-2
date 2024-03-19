import tkinter as tk

def button_click(symbol):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current + symbol)

def clear_display():
    entry_display.delete(0, tk.END)

def calculate():
    try:
        expression = entry_display.get()
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, result)
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Colorful Calculator")

# Display Entry
entry_display = tk.Entry(root, width=20, font=("Helvetica", 14))
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=10, pady=10, font=("Helvetica", 14), command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Clear Button
clear_button = tk.Button(root, text="C", padx=10, pady=10, font=("Helvetica", 14), command=clear_display)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

# Calculate Button
calculate_button = tk.Button(root, text="=", padx=10, pady=10, font=("Helvetica", 14), command=calculate)
calculate_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# Configure row and column weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

# Run the main event loop
root.mainloop()