import job_operations
import tkinter as tk
from tkinter import ttk
from database import initialize_database

initialize_database()

applications = job_operations.get_applications()
print(applications)

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

status_label = ttk.Combobox(root, values=["Applied", "Interview","Offer","Rejected", "Withdrawn"])
status_label.pack()

root.mainloop()




