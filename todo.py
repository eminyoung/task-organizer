import tkinter as tk
import tkinter.messagebox

root = tk.Tk()
root.title("To-Do List")
task_var = tk.StringVar()

def add_task():
    task = entry_task.get()
    listbox_tasks.insert(tk.END, task)

# Create GUI
listbox_tasks = tk.Listbox(root, height=3, width=50)
listbox_tasks.pack()

entry_task = tk.Entry(root, width=50, font="arial 20", bd=0)
entry_task.pack()

button_add_task = tk.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

root.mainloop()