import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class EmployeeForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Personal Information")
        self.root.geometry("800x600")

        # Title
        title = tk.Label(self.root, text="SE-RI`S EMPLOYEE PERSONAL INFORMATION", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Form frame
        self.form_frame = tk.Frame(self.root, padx=20, pady=20)
        self.form_frame.pack(fill="both", expand=True)

        # Personal Information Section
        self.create_personal_info()

        # Contact Info Section
        self.create_contact_info()

        # Address Section
        self.create_address_info()

        # Buttons
        self.create_buttons()

    def create_personal_info(self):
        section_title = tk.Label(self.form_frame, text="Personal Information", font=("Arial", 12, "bold"))
        section_title.grid(row=0, column=0, columnspan=4, pady=5)

        # Form fields
        fields = ["First Name", "Middle Name", "Last Name", "Suffix", "Date of Birth", "Gender",
                  "Nationality", "Civil Status", "Department", "Designation", "Qualified Dep. Status",
                  "Employee Status", "Paydate", "Employee Number"]

        self.personal_info = {}  # To store user inputs

        for idx, field in enumerate(fields):
            label = tk.Label(self.form_frame, text=field + ":")
            label.grid(row=idx + 1, column=0, sticky="w", pady=2)

            if field in ["Gender", "Nationality", "Civil Status", "Qualified Dep. Status"]:
                combobox = ttk.Combobox(self.form_frame, values=["Option 1", "Option 2", "Option 3"])
                combobox.grid(row=idx + 1, column=1, padx=5, pady=2)
                self.personal_info[field] = combobox
            elif field == "Date of Birth" or field == "Paydate":
                date_entry = tk.Entry(self.form_frame)
                date_entry.grid(row=idx + 1, column=1, padx=5, pady=2)
                self.personal_info[field] = date_entry
            else:
                entry = tk.Entry(self.form_frame)
                entry.grid(row=idx + 1, column=1, padx=5, pady=2)
                self.personal_info[field] = entry

    def create_contact_info(self):
        section_title = tk.Label(self.form_frame, text="Contact Info", font=("Arial", 12, "bold"))
        section_title.grid(row=15, column=0, columnspan=4, pady=5)

        # Form fields
        fields = ["Contact No.", "Email", "Other (Social Media)", "Social Media Account ID/No."]

        self.contact_info = {}  # To store user inputs

        for idx, field in enumerate(fields):
            label = tk.Label(self.form_frame, text=field + ":")
            label.grid(row=16 + idx, column=0, sticky="w", pady=2)

            entry = tk.Entry(self.form_frame)
            entry.grid(row=16 + idx, column=1, padx=5, pady=2)
            self.contact_info[field] = entry

    def create_address_info(self):
        section_title = tk.Label(self.form_frame, text="Address", font=("Arial", 12, "bold"))
        section_title.grid(row=20, column=0, columnspan=4, pady=5)

        # Form fields
        fields = ["Address Line 1", "Address Line 2", "City/Municipality", "State/Province",
                  "Country", "Zip Code", "Picture Path"]

        self.address_info = {}  # To store user inputs

        for idx, field in enumerate(fields):
            label = tk.Label(self.form_frame, text=field + ":")
            label.grid(row=21 + idx, column=0, sticky="w", pady=2)

            if field == "Country":
                combobox = ttk.Combobox(self.form_frame, values=["Philippines", "Other"])
                combobox.grid(row=21 + idx, column=1, padx=5, pady=2)
                self.address_info[field] = combobox
            elif field == "Picture Path":
                path_button = tk.Button(self.form_frame, text="Browse", command=self.browse_file)
                path_button.grid(row=21 + idx, column=1, padx=5, pady=2, sticky="w")
                self.address_info[field] = tk.StringVar()
            else:
                entry = tk.Entry(self.form_frame)
                entry.grid(row=21 + idx, column=1, padx=5, pady=2)
                self.address_info[field] = entry

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.address_info["Picture Path"].set(file_path)

    def create_buttons(self):
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x", pady=10)

        save_btn = tk.Button(btn_frame, text="Save", command=self.save_data)
        save_btn.pack(side="left", padx=10)

        cancel_btn = tk.Button(btn_frame, text="Cancel", command=self.root.quit)
        cancel_btn.pack(side="right", padx=10)

    def save_data(self):
        print("Save button clicked.")
        # Logic to save data can go here
