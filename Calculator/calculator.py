import tkinter as tk
from tkinter import messagebox

# Functions to perform arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        messagebox.showerror("Error", "Division by zero is not allowed")
        return None

# Function to perform the calculation
def calculate():
    num1 = entry_num1.get()  # Get the first number from the entry widget
    num2 = entry_num2.get()  # Get the second number from the entry widget
    operation = operation_var.get()  # Get the selected operation from the dropdown menu

    try:
        num1 = float(num1)  # Convert first number to float
        num2 = float(num2)  # Convert second number to float
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")  # Show error if inputs are not valid numbers
        return

    # Perform the selected operation
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    else:
        result = None

    # Set the result in the result label if calculation is successful
    if result is not None:
        result_var.set(f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")  # Set the title of the window

# Create and place widgets
tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=10, pady=5)
entry_num1 = tk.Entry(root)  # Entry widget for the first number
entry_num1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=10, pady=5)
entry_num2 = tk.Entry(root)  # Entry widget for the second number
entry_num2.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Select operation:").grid(row=2, column=0, padx=10, pady=5)
operation_var = tk.StringVar()
operation_var.set("Add")  # default value

# Dropdown menu for selecting operation
operations = ["Add", "Subtract", "Multiply", "Divide"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=2, column=1, padx=10, pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2, pady=10)

# Label to display the result
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=4, columnspan=2, pady=10)

# Run the application
root.mainloop()
