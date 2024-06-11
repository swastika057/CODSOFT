import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, master):
        # Initialize the TodoApp class with the provided master window
        self.master = master
        self.master.title("To-Do List")  # Set the title of the window

        # Initialize an empty list to store tasks
        self.tasks = []

        # Create an entry widget for entering tasks
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=5)  # Place the entry widget in the window

        # Create a button for adding tasks
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)  # Place the button in the window

        # Create a listbox for displaying tasks
        self.task_listbox = tk.Listbox(master, width=50, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=5)  # Place the listbox in the window

        # Create a button for updating tasks
        self.update_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_button.grid(row=2, column=0, padx=5, pady=5)  # Place the button in the window

        # Create a button for marking tasks as complete or incomplete
        self.complete_button = tk.Button(master, text="Mark Complete/Incomplete", command=self.toggle_complete)
        self.complete_button.grid(row=2, column=1, padx=5, pady=5)  # Place the button in the window

        # Create a button for deleting tasks
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=2, column=2, padx=5, pady=5)  # Place the button in the window

        # Create a button for clearing all tasks
        self.clear_button = tk.Button(master, text="Clear All", command=self.clear_tasks)
        self.clear_button.grid(row=2, column=3, padx=5, pady=5)  # Place the button in the window

    def add_task(self):
        # Function to add a new task
        task = self.task_entry.get()  # Get the task text from the entry widget
        if task:
            # If the task is not empty, append it to the tasks list
            self.tasks.append(task)
            # Insert the task into the listbox with numbering
            self.update_task_display()
            self.task_entry.delete(0, tk.END)  # Clear the entry widget after adding the task
        else:
            # If the task is empty, show a warning message
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def update_task(self):
        # Function to update a task
        try:
            selected_task_index = self.task_listbox.curselection()[0]  # Get the index of the selected task
            updated_task = self.task_entry.get()  # Get the updated task text from the entry widget
            if updated_task:
                # If the updated task is not empty, update it in the tasks list and listbox
                self.tasks[selected_task_index] = updated_task
                self.update_task_display()
                self.task_entry.delete(0, tk.END)  # Clear the entry widget after updating the task
            else:
                # If the updated task is empty, show a warning message
                messagebox.showwarning("Warning", "Task cannot be empty!")
        except IndexError:
            # If no task is selected, show a warning message
            messagebox.showwarning("Warning", "No task selected!")

    def toggle_complete(self):
        # Function to toggle the completion status of a task
        try:
            selected_task_index = self.task_listbox.curselection()[0]  # Get the index of the selected task
            task_text = self.tasks[selected_task_index]
            # If the task is marked as complete, unmark it; otherwise, mark it as complete
            if task_text.startswith("[X] "):
                self.tasks[selected_task_index] = task_text[4:]
            else:
                self.tasks[selected_task_index] = "[X] " + task_text
            self.update_task_display()  # Update the task display in the listbox
        except IndexError:
            # If no task is selected, show a warning message
            messagebox.showwarning("Warning", "No task selected!")

    def delete_task(self):
        # Function to delete a task
        try:
            selected_task_index = self.task_listbox.curselection()[0]  # Get the index of the selected task
            del self.tasks[selected_task_index]  # Remove the task from the tasks list
            self.update_task_display()  # Update the task display in the listbox
        except IndexError:
            # If no task is selected, show a warning message
            messagebox.showwarning("Warning", "No task selected!")

    def clear_tasks(self):
        # Function to clear all tasks
        self.tasks = []  # Clear the tasks list
        self.update_task_display()  # Update the task display in the listbox

    def update_task_display(self):
        # Function to update the task display in the listbox
        self.task_listbox.delete(0, tk.END)  # Clear the current task display
        for index, task in enumerate(self.tasks, start=1):
            # Iterate through the tasks list and add tasks with numbering to the listbox
            task_text = f"{index}. {task}"
            self.task_listbox.insert(tk.END, task_text)  # Insert the task text into the listbox

def main():
    root = tk.Tk()  # Create the main window
    app = TodoApp(root)  # Instantiate the TodoApp class
    root.mainloop()  # Start the Tkinter event loop

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly
