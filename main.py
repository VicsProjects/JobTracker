from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

import job_operations
from database import initialize_database

initialize_database()

root = tk.Tk()
root.title("Job Tracker")
root.geometry("800x500")

heading = tk.Label(root, text="Job Application Tracker")
heading.pack()

company_label = tk.Label(root, text="Company:")
company_label.pack()

company_entry = tk.Entry(root)
company_entry.pack()

job_title_label = tk.Label(root, text="Job Title:")
job_title_label.pack()

job_title_entry = tk.Entry(root)
job_title_entry.pack()

status_combobox = ttk.Combobox(root, values=["Applied", "Interview","Offer","Rejected", "Withdrawn"], state="readonly")
status_combobox.pack()

application_date_label = tk.Label(root, text="Application Date:")
application_date_label.pack()

application_date_entry = tk.Entry(root)
application_date_entry.pack()

notes_label = tk.Label(root, text="Notes:")
notes_label.pack()

notes_entry = tk.Text(root, height=4, width=40)
notes_entry.pack()

def add_application():
    company = company_entry.get()
    job_title = job_title_entry.get()
    status = status_combobox.get()
    application_date = application_date_entry.get()
    notes = notes_entry.get("1.0", "end-1c")
    if not company.strip() or not job_title.strip():
        return messagebox.showerror("Error", "Company and job title can not be left blank")
    job_operations.add_application(company, job_title, status, application_date, notes)
    company_entry.delete(0, "end")
    job_title_entry.delete(0, "end")
    status_combobox.set("Applied")
    application_date_entry.delete(0, "end")
    notes_entry.delete("1.0", "end")
    refresh_applications()

add_button = tk.Button(root, text="Add Application", command=add_application)
add_button.pack()

tree = ttk.Treeview(root, columns=("company", "job_title", "status", "application_date", "notes"), show="headings")
tree.heading("company", text="Company")
tree.heading("job_title", text="Job Title")
tree.heading("status", text="Status")
tree.heading("application_date", text="Application Date")
tree.heading("notes", text="Notes")
tree.pack()

def refresh_applications():
    for item in tree.get_children():
        tree.delete(item)
    applications = job_operations.get_applications()
    for application in applications:
        tree.insert("", "end", iid=application[0], values=application[1:])

refresh_applications()


root.mainloop()




