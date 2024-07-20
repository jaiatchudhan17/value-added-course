import tkinter as tk
from tkinter import messagebox

class StudentMarkListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Mark List")
        
        self.create_widgets()

    def create_widgets(self):
        
        tk.Label(self.root, text="Name").grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(self.root, text="Roll Number").grid(row=1, column=0, padx=10, pady=5)
        self.roll_entry = tk.Entry(self.root)
        self.roll_entry.grid(row=1, column=1, padx=10, pady=5)
        
       
        self.subjects = ["business analytics", "machine learning analysis", "social network analysis", "python programming", "text analysis"]
        self.mark_entries = []
        
        for i, subject in enumerate(self.subjects, start=2):
            tk.Label(self.root, text=subject).grid(row=i, column=0, padx=10, pady=5)
            entry = tk.Entry(self.root)
            entry.grid(row=i, column=1, padx=10, pady=5)
            self.mark_entries.append(entry)
        
        
        self.add_button = tk.Button(self.root, text="Add Student", command=self.add_student)
        self.add_button.grid(row=len(self.subjects) + 2, column=0, columnspan=2, pady=10)
        
       
        self.student_listbox = tk.Listbox(self.root, width=50, height=10)
        self.student_listbox.grid(row=len(self.subjects) + 3, column=0, columnspan=2, padx=10, pady=10)
        
    def add_student(self):
        name = self.name_entry.get()
        roll_number = self.roll_entry.get()
        marks = [entry.get() for entry in self.mark_entries]
        
        if not name or not roll_number or any(not mark for mark in marks):
            messagebox.showwarning("Input Error", "All fields are required")
            return
        
        student_data = f"Name: {name}, Roll Number: {roll_number}, Marks: {', '.join(marks)}"
        self.student_listbox.insert(tk.END, student_data)
        
        
        self.name_entry.delete(0, tk.END)
        self.roll_entry.delete(0, tk.END)
        for entry in self.mark_entries:
            entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentMarkListApp(root)
    root.mainloop()
