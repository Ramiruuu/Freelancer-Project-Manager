import tkinter as tk
from tkinter import messagebox
import datetime

# List to store projects
projects = []

# Function to add a project
def add_project():
    project_name = entry_project_name.get()
    client_name = entry_client_name.get()
    due_date = entry_due_date.get()
    payment = entry_payment.get()

    try:
        due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
        project = {
            'Project Name': project_name,
            'Client Name': client_name,
            'Due Date': due_date,
            'Payment': float(payment),
            'Status': 'In Progress'
        }
        projects.append(project)
        messagebox.showinfo("Success", "Project added successfully!")
        clear_entries()
    except ValueError:
        messagebox.showerror("Error", "Invalid date format or payment amount.")

# Function to view all projects
def view_projects():
    if projects:
        project_list = "\n".join([
            f"{i+1}. {p['Project Name']} (Client: {p['Client Name']}, Due: {p['Due Date'].strftime('%Y-%m-%d')}, Payment: ${p['Payment']:.2f}, Status: {p['Status']})"
            for i, p in enumerate(projects)
        ])
        messagebox.showinfo("Projects", project_list)
    else:
        messagebox.showinfo("Projects", "No projects found.")

# Function to clear entry fields
def clear_entries():
    entry_project_name.delete(0, tk.END)
    entry_client_name.delete(0, tk.END)
    entry_due_date.delete(0, tk.END)
    entry_payment.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Freelancer Project Manager")

tk.Label(root, text="Project Name:").grid(row=0, column=0)
entry_project_name = tk.Entry(root)
entry_project_name.grid(row=0, column=1)

tk.Label(root, text="Client Name:").grid(row=1, column=0)
entry_client_name = tk.Entry(root)
entry_client_name.grid(row=1, column=1)

tk.Label(root, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0)
entry_due_date = tk.Entry(root)
entry_due_date.grid(row=2, column=1)

tk.Label(root, text="Payment Amount:").grid(row=3, column=0)
entry_payment = tk.Entry(root)
entry_payment.grid(row=3, column=1)

tk.Button(root, text="Add Project", command=add_project).grid(row=4, column=0, columnspan=2)
tk.Button(root, text="View Projects", command=view_projects).grid(row=5, column=0, columnspan=2)

root.mainloop()