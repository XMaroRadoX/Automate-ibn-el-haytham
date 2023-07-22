import tkinter as tk
from tkinter import  Label,  ttk  , font
from PIL import Image, ImageTk
from logic import mainloop


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Course Registration Tool")
       # Set the background image
       
               # Creating a Font object of "TkDefaultFont"
        self.defaultFont = font.nametofont("TkDefaultFont")
  
        # Overriding default-font with custom settings
        # i.e changing font-family, size and weight
        self.defaultFont.configure(family="Times",
                                   size=12)
             # Set the background image
        background_img = Image.open("app/bg.png")
        background_img = background_img.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
        self.background_img_tk = ImageTk.PhotoImage(background_img)

        # Create a Label widget and set the background image
        self.background_label = Label(root, image=self.background_img_tk)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Title
        self.title_label = tk.Label(
            root, text="Ibn Alhaitham Bot", font=("Times", 24) ,fg='#ffffff' , bg='#000000')
        self.title_label.grid(row=0, column=0, columnspan=12, pady=10)

        # Your Info Section
        self.info_section = tk.LabelFrame(
            
            root, text="Your Info", padx=10, pady=5  ,fg='#ffffff' , bg='#000000')
        self.info_section.grid(row=1, column=0, columnspan=12, padx=10, pady=5)

        # Username and Password Entry fields
        self.username_label = tk.Label(self.info_section, text="ID:" ,fg='#ffffff' , bg='#000000')
        self.username_label.grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self.info_section)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        self.password_label = tk.Label(self.info_section, text="Password:" ,fg='#ffffff' , bg='#000000')
        self.password_label.grid(row=0, column=2, padx=10, pady=5)
        self.password_entry = tk.Entry(self.info_section, show="*")
        self.password_entry.grid(row=0, column=3, padx=10, pady=5)

        # Dropdowns Section
        self.dropdown_section = tk.LabelFrame(
            root, text="Dropdowns", padx=10, pady=5 ,fg='#ffffff' , bg='#000000')
        self.dropdown_section.grid(
            row=2, column=0, columnspan=12, padx=10, pady=5)

        # Independent arrays for dropmenu options
        self.terms = [f"{i}" for i in range(0, 11)]
        self.courses = ["Communication Systems", "Data Structures",
                        "Algorithms", "Database Systems", "Artificial Intelligence"]
        self.lecture_numbers = [str(i) for i in range(1, 11)]
        self.section_numbers = [str(i) for i in range(1, 11)]
        self.lab_numbers = [str(i) for i in range(1, 11)]

        # Dropmenus
        self.term_label = tk.Label(self.dropdown_section, text="Term:" ,fg='#ffffff' , bg='#000000')
        self.term_label.grid(row=0, column=0, padx=10, pady=5)
        self.term_var = tk.StringVar(root)
        self.term_var.set(self.terms[0])
        self.term_menu = ttk.OptionMenu(
            self.dropdown_section, self.term_var, *self.terms)
        self.term_menu.grid(row=0, column=1, padx=10, pady=5)

        self.course_label = tk.Label(
            self.dropdown_section, text="Course Name:" ,fg='#ffffff' , bg='#000000')
        self.course_label.grid(row=1, column=0, padx=10, pady=5)
        self.course_var = tk.StringVar(root)
        self.course_var.set(self.courses[0])
        self.course_menu = ttk.OptionMenu(
            self.dropdown_section, self.course_var, *self.courses)
        self.course_menu.grid(row=1, column=1, padx=10, pady=5)


        self.lecture_label = tk.Label(
            self.dropdown_section, text="Group Number:" ,fg='#ffffff' , bg='#000000')
        self.lecture_label.grid(row=2, column=0, padx=10, pady=5)
        self.lecture_var = tk.StringVar(root)
        self.lecture_var.set(self.lecture_numbers[0])
        self.lecture_menu = ttk.OptionMenu(
            self.dropdown_section, self.lecture_var, *self.lecture_numbers)
        self.lecture_menu.grid(row=2, column=1, padx=10, pady=5)

        self.section_label = tk.Label(
            self.dropdown_section, text="Section Number:" ,fg='#ffffff' , bg='#000000')
        self.section_label.grid(row=0, column=3, padx=10, pady=5)
        self.section_var = tk.StringVar(root)
        self.section_var.set(self.section_numbers[0])
        self.section_menu = ttk.OptionMenu(
            self.dropdown_section, self.section_var, *self.section_numbers)
        self.section_menu.grid(row=0, column=4, padx=10, pady=5)

        self.lab_label = tk.Label(self.dropdown_section, text="Lab Number:" ,fg='#ffffff' , bg='#000000')
        self.lab_label.grid(row=1, column=3, padx=10, pady=5)
        self.lab_var = tk.StringVar(root)
        self.lab_var.set(self.lab_numbers[0])
        self.lab_menu = ttk.OptionMenu(
            self.dropdown_section, self.lab_var, *self.lab_numbers)
        self.lab_menu.grid(row=1, column=4, padx=10, pady=5)


        self.add_drop_section = tk.LabelFrame(
            root, text="Add/Drop", padx=50, pady=5 ,fg='#ffffff' , bg='#000000')
        self.add_drop_section.grid(
            row=4, column=4, columnspan=12, padx=100, pady=5)

        # Add Button
        self.add_button = tk.Button(self.add_drop_section, text="Add Course", highlightthickness=10, bg='#00c6f7', command=self.add_to_json)
        self.add_button.grid(row=0, column=0, columnspan=12, padx=10, pady=5)

        
        self.remove_button = tk.Button(self.add_drop_section, text="Drop Course", highlightthickness=10, bg='#00c6f7', command=self.remove_from_json)
        self.remove_button.grid(row=0, column=100, columnspan=12 ,padx=10, pady=5)


        # Panel to show the appended info
        self.info_panel = tk.Text(root, width=60, height=8 ,fg='#ffffff' , bg='#000000')
        self.info_panel.grid(row=5, column=0, columnspan=12, padx=10, pady=5)
        scrollbar = tk.Scrollbar(root, command=self.info_panel.yview)
        self.info_panel.config(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=5, column=11, sticky="ns")

        # Go Button
        self.go_button = tk.Button(root, text="Go", command=self.go_function , bg='#00c6f7' ,highlightthickness=10, padx=40)
        self.go_button.grid(row=6, column=0, columnspan=12, padx=10, pady=5)
        
        self.label=tk.Label(root, width=50,height=2, text="Developed by: Marwan Radwan" ,fg='#ffffff' , bg='#000000')
        self.label.grid(row=7, column=0, columnspan=12, padx=10, pady=5)


        # Initialize an empty list to store JSON objects
        self.json_objects = []

    def format_json_object(self, json_object):
        # Format the JSON object as a clear table-like structure
        formatted_info = (
            f"Course: {json_object['course']},"
            f"Term: {json_object['Term']}\n"
            f"Group Number: {json_object['Group Number']},"
            f"Section Number: {json_object['Section Number']},"
            f"Lab Number: {json_object['Lab Number']}\n\n"
        )
        return formatted_info

    def add_to_json(self):
        # Create a JSON object from the selected dropmenu values
        json_object = {
            'course': self.course_var.get(),
            'Term': self.term_var.get(),
            'Group Number': self.lecture_var.get(),
            'Section Number': self.section_var.get(),
            'Lab Number': self.lab_var.get()
        }
        # Append the JSON object to the list
        self.json_objects.append(json_object)
        # Clear the info panel and display the updated list
        self.info_panel.delete("1.0", tk.END)
        formatted_info = [self.format_json_object(obj) for obj in self.json_objects]
        self.info_panel.insert(tk.END, "\n".join(formatted_info))

    def remove_from_json(self):
        json_object = {
            'course': self.course_var.get(),
            'Term': self.term_var.get(),
            'Group Number': self.lecture_var.get(),
            'Section Number': self.section_var.get(),
            'Lab Number': self.lab_var.get()
        }

        # Remove the JSON object from the list
        self.json_objects.remove(json_object)

        # Clear the info panel and display the updated list
        self.info_panel.delete("1.0", tk.END)
        formatted_info = [self.format_json_object(obj) for obj in self.json_objects]
        self.info_panel.insert(tk.END, "\n".join(formatted_info))

    def go_function(self):
            mainloop(self.username_entry.get(),  self.password_entry.get(),self.json_objects)

    
    def force_exit(self):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
