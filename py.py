import tkinter as tk
from tkinter import messagebox

def check_scholarship_eligibility():
    try:
        gpa = float(gpa_entry.get())
        income = int(income_entry.get())
        community_service_hours = int(community_entry.get())
        field_of_study = field_entry.get().strip().lower()
        is_from_rural_area = rural_var.get()
        
        scholarships = []

        if gpa >= 3.5:
            scholarships.append("Academic Scholarship")

        if income <= 100000:
            scholarships.append("Need-Based Scholarship")

        if community_service_hours >= 50:
            scholarships.append("Community Service Scholarship")

        if field_of_study in ["science", "technology", "engineering", "mathematics"]:
            scholarships.append("STEM Scholarship")

        if is_from_rural_area:
            scholarships.append("Rural Area Scholarship")

        result = "\n".join(scholarships) if scholarships else "No scholarships available based on the provided information."
        messagebox.showinfo("Eligible Scholarships", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for GPA, Income, and Community Service Hours.")

# Create GUI window
root = tk.Tk()
root.title("Scholarship Eligibility Checker")
root.geometry("400x400")

# Labels and Entry Fields
tk.Label(root, text="GPA:").pack()
gpa_entry = tk.Entry(root)
gpa_entry.pack()

tk.Label(root, text="Family Income (RWF):").pack()
income_entry = tk.Entry(root)
income_entry.pack()

tk.Label(root, text="Community Service Hours:").pack()
community_entry = tk.Entry(root)
community_entry.pack()

tk.Label(root, text="Field of Study:").pack()
field_entry = tk.Entry(root)
field_entry.pack()

rural_var = tk.BooleanVar()
tk.Checkbutton(root, text="From a Rural Area", variable=rural_var).pack()

# Submit Button
tk.Button(root, text="Check Eligibility", command=check_scholarship_eligibility).pack()

# Run GUI
root.mainloop()
