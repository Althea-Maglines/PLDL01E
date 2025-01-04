import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# creating class for payroll page design
class PayrollPageDesign:
    def __init__(self):
        self.window = tk.Tk()
        self.configure_window()
        self.create_header()
        self.create_frame_employee_basic_info()
        self.create_button_search_employee()
        self.add_employee_info_section()
        self.create_labels()
        self.create_textboxes()
        self.basic_income_frame_title()
        self.create_frames()
        self.honorarium_income_frame_title()
        self.other_income_frame_title()
        self.regular_deductions_frame_title()
        self.other_deductions_frame_title()
        self.deduction_summary_frame_title()
        self.add_footer()
        self.add_button()

# creating a configure window
    def configure_window(self):
        self.window.state('zoomed')  # Adjust size as needed
        self.window.title("Payroll Page Design")
        self.window.configure(bg="#dbd2c1")

# creating the header
    def create_header(self):
        # creating a frame for header
        header_frame = tk.Frame(self.window, bg='#102f54')
        header_frame.pack(fill="x", pady=1)

        # creating the label for header
        title_label = tk.Label(header_frame, text="MINA'S CHOICE PAYROLL", fg='white', bg='#102f54', font=("Helvetica", 20, "bold"))
        title_label.pack(padx=25, pady=35, anchor="center")

# Adding the employee basic information section
    def add_employee_info_section(self):
    # Create a frame and label for Employee Basic Info
        title_frame = tk.Frame(self.window, bg="black", height=1)
        title_frame.place(x=0, y=137.5, anchor="w", width=600)
        title_label = tk.Label(title_frame, text="EMPLOYEE BASIC INFORMATION", fg="white", bg="black",
                                   font=("Helvetica", 16, "bold"))
        title_label.pack(anchor="w", padx=55, pady=10)
        tk.Frame(self.window, bg="#102f54", height=50).place(x=0, y=137.5, anchor="w", width=40)

    # Profile photo
        image_path = r"C:\Users\Worldtech Computer\PycharmProjects\PLDL01E\PLDL01E_THEA\black_profile.jpg"  # Replace with your actual path
        image = Image.open(image_path)
        image = image.resize((160, 150))  # Adjust size as needed
        photo_image = ImageTk.PhotoImage(image)
        first_image_label = Label(self.window, image=photo_image, bg='#343434')
        first_image_label.image = photo_image  # Keep a reference to prevent garbage collection
        first_image_label.place(x=200, y=185)

# creating a frames
    def create_frames(self):
        frames = [
            ("white", 0, 104, 2000, 5)
        ]
        for bg, x, y, width, height in frames:
            frame = tk.Frame(self.window, bg=bg, width=width, height=height)
            frame.place(x=x, y=y)

# creating a frames
    def frame(self, x, y):
        self.frames = Frame(self.window, width=600, height=1000, borderwidth=0, bg='#ebeae7')
        self.frames.place(x=x, y=y)

    def frame2(self, x, y):
        self.frames2 = Frame(self.window, width=433, height=165, borderwidth=0, bg='#ebeae7')
        self.frames2.place(x=x, y=y)

    def frame3(self, x, y):
        self.frames3 = Frame(self.window, width=433, height=165, borderwidth=0, bg='#ebeae7')
        self.frames3.place(x=x, y=y)

    def frame4(self, x, y):
        self.frames4 = Frame(self.window, width=433, height=165, borderwidth=0, bg='#ebeae7')
        self.frames4.place(x=x, y=y)

    def frame5(self, x, y):
        self.frames5 = Frame(self.window, width=600, height=280, borderwidth=0, bg='#aaaaaa')
        self.frames5.place(x=x, y=y)

    def frame6(self, x, y):
        self.frames6 = Frame(self.window, width=600, height=50, borderwidth=0, bg='white')
        self.frames6.place(x=x, y=y)

    def frame7(self, x, y):
        self.frames7 = Frame(self.window, width=600, height=50, borderwidth=0, bg='#e8e8e8')
        self.frames7.place(x=x, y=y)

    def frame8(self, x, y):
        self.frames8 = Frame(self.window, width=433, height=50, borderwidth=0, bg='white')
        self.frames8.place(x=x, y=y)

    def frame9(self, x, y):
        self.frames9 = Frame(self.window, width=433, height=50, borderwidth=0, bg='#e8e8e8')
        self.frames9.place(x=x, y=y)

    def frame10(self, x, y):
        self.frames10 = Frame(self.window, width=1309, height=100, borderwidth=0, bg='#ebeae7')
        self.frames10.place(x=x, y=y)

    def frame11(self, x, y):
        self.frames11 = Frame(self.window, width=1309, height=50, borderwidth=0, bg='white')
        self.frames11.place(x=x, y=y)

    def frame12(self, x, y):
        self.frames12 = Frame(self.window, width=1309, height=50, borderwidth=0, bg='#e8e8e8')
        self.frames12.place(x=x, y=y)

    def frame13(self, x, y):
        self.frames13 = Frame(self.window, width=1309, height=200, borderwidth=0, bg='#ebeae7')
        self.frames13.place(x=x, y=y)

    def frame14(self, x, y):
        self.frames14 = Frame(self.window, width=1309, height=50, borderwidth=0, bg='#ebeae7')
        self.frames14.place(x=x, y=y)

# creating the frames of employee basic info
    def create_frame_employee_basic_info(self):
        self.frame(0, 157)
        self.frame6(0, 425)
        self.frame7(0, 480)
        self.frame6(0, 535)
        self.frame7(0, 590)
        self.frame6(0, 645)
        self.frame7(0, 700)
        self.frame6(0, 755)
        self.frame7(0, 810)
        self.frame6(0, 865)
        self.frame7(0, 920)

# creating a Label design
    def label_design(self, x, y, text_value):
        self.lbl = Label(self.window, text=text_value, bg='#7c7c7c', fg='white', font=('Helvetica', 25, 'bold'))
        self.lbl.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.lbl = Label(self.window, text=text_value, bg='white', fg='#3d3d3d', font=('Helvetica', 16, 'bold'))
        self.lbl.place(x=x, y=y)

    def label_design3(self, x, y, text_value):
        self.lbl = Label(self.window, text=text_value, bg='#e8e8e8', fg='#3d3d3d', font=('Helvetica', 16, 'bold'))
        self.lbl.place(x=x, y=y)

    # creating a textboxes design
    def textbox_design1(self, x, y):
        self.textbox = Text(width=20, height=1, fg='black', bg='light gray',
        font=('Helvetica', 11))
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=12, height=1, fg='black', bg='light gray',
        font=('Helvetica', 11))
        self.textbox.place(x=x, y=y)

    def textbox_design3(self, x, y):
        self.textbox = Text(width=20, height=1, fg='black', bg='light gray',
        font=('Helvetica', 11))
        self.textbox.place(x=x, y=y)

# Employee Basic Information Labels
    def create_labels(self):
        self.label_design2(25, 435.5, 'First Name : ')
        self.label_design3(25, 490.5, 'Middle Name : ')
        self.label_design2(25, 545.5, 'Last Name : ')
        self.label_design3(25, 600.5, 'Civil Status : ')
        self.label_design2(25, 654.5, 'Qualified Dependents Status : ')
        self.label_design3(25, 710.5, 'Paydate : ')
        self.label_design2(25, 765.5, 'Employee Status : ')
        self.label_design3(25, 820.5, 'Designation : ')
        self.label_design2(25, 875.5, 'Employee Number : ')
        self.label_design3(25, 930.5, 'Department : ')

# Employee Basic Information Textboxes
    def create_textboxes(self):
        self.textbox_design1(370, 440)
        self.textbox_design1(370, 495)
        self.textbox_design1(370, 550)
        self.textbox_design1(370, 605)
        self.textbox_design1(370, 660)
        self.textbox_design1(370, 715)
        self.textbox_design1(370, 770)
        self.textbox_design1(370, 825)
        self.textbox_design1(370, 880)
        self.textbox_design1(370, 935)

# creating a button design
    def button_design(self, x, y):
        self.upload_button = Button(self.window, width=20, pady=7, text='SEARCH EMPLOYEE', bg='#102f54', fg='white',
        font=('Helvetica', 13, 'bold'), cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def button_design1(self, x, y):
        self.upload_button = Button(self.window, width=20, pady=7, text='GROSS INCOME', bg='#102f54', fg='white',
                                    font=('Helvetica', 13, 'bold'), cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def button_design2(self, x, y):
        self.upload_button = Button(self.window, width=20, pady=7, text='NET INCOME', bg='#102f54', fg='white',
                                    font=('Helvetica', 13, 'bold'), cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def button_design3(self, x, y):
        self.upload_button = Button(self.window, width=20, pady=7, text='SAVE', bg='#102f54', fg='white',
                                    font=('Helvetica', 13, 'bold'), cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def button_design4(self, x, y):
        self.upload_button = Button(self.window, width=20, pady=7, text='UPDATE', bg='#102f54', fg='white',
                                    font=('Helvetica', 13, 'bold'), cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def button_design5(self, x, y):
        self.upload_button = Button(self.window, width=20, pady=7, text='NEW', bg='#102f54', fg='white',
                                    font=('Helvetica', 13, 'bold'), cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def create_button_search_employee(self):
        self.button_design(180, 360)

# creating basic info
    def basic_income_frame_title(self):
        # Frame for Basic Income
        self.frame2(606, 157)
        self.frame8(606, 167)
        self.frame9(606, 222)
        self.frame8(606, 277)

        # Creating a title frame for basic income
        title_frame_basic_income = tk.Frame(self.window, bg="black", height=1)
        title_frame_basic_income.place(x=606, y=137.5, anchor="w", width=433)  # Position for Basic Income

        # Label for Basic Income
        title_label_basic_income = tk.Label(title_frame_basic_income, text="BASIC INCOME", fg="white", bg="black",
                                    font=("Helvetica", 16, "bold"))
        title_label_basic_income.pack(anchor="w", padx=60, pady=10)  # Add padding to center the text vertically

        # creating the blue design in left side
        frame = tk.Frame(self.window, bg="#102f54", height=50)
        frame.place(x=606, y=137.5, anchor="w", width=45)

        # Add new label and textbox for Rate / Hour
        self.label_design2(625, 177, "Rate / Hour : ")
        self.textbox_design2(915, 182)

        # Add new label and textbox for No. of Hours / Cut Off
        self.label_design3(625, 233, "No. of Hours / Cut Off : ")
        self.textbox_design2(915, 237)

        # Add new label and textbox for Income / Cut Off
        self.label_design2(625, 287.5, "Income / Cut Off : ")
        self.textbox_design2(915, 291.5)

# creating honorarium income
    def honorarium_income_frame_title(self):
        # frame for honorarium income
        self.frame3(1044, 157)
        self.frame8(1044, 167)
        self.frame9(1044, 222)
        self.frame8(1044, 277)

        # Create a frame for honorarium income
        title_frame_honorarium_income = tk.Frame(self.window, bg="black", height=1)  # Adjust height as needed
        title_frame_honorarium_income.place(x=1044, y=137.5, anchor="w", width=433)  # Use side="bottom" to anchor it at the bottom

        # Create a label for honorarium income
        title_label = tk.Label(title_frame_honorarium_income, text="HONORARIUM INCOME", fg="white", bg="black",
                        font=("Helvetica", 16, "bold"))
        title_label.pack(anchor="w", padx=60, pady=10)  # Add padding to center the text vertically

        # creating the blue design in left side
        title_frame = tk.Frame(self.window, bg="#102f54", height=50)  # Adjust height as needed
        title_frame.place(x=1044, y=137.5, anchor="w", width=45)

        # Add new label and textbox for Rate / Hour
        self.label_design2(1063, 177, 'Rate / Hour : ')
        self.textbox_design2(1353, 182)

        # Add new label and textbox for No. of Hours / Cut Off
        self.label_design3(1063, 233, 'No. of Hours / Cut Off : ')
        self.textbox_design2(1353, 237)

        # Add new label and textbox for Income / Cut Off
        self.label_design2(1063, 287.5, 'Income / Cut Off : ')
        self.textbox_design2(1353, 291.5)

# creating other income
    def other_income_frame_title(self):
        self.frame4(1482, 157)
        self.frame8(1482, 167)
        self.frame9(1482, 222)
        self.frame8(1482, 277)

        # Create a frame for other income
        title_frame_other_income = tk.Frame(self.window, bg="black", height=1)  # Adjust height as needed
        title_frame_other_income.place(x=1482, y=137.5, anchor="w", width=433)  # Use side="bottom" to anchor it at the bottom

        # Create a label for other income
        title_label = tk.Label(title_frame_other_income, text="OTHER INCOME", fg="white", bg="black", font=("Helvetica", 16, "bold"))
        title_label.pack(anchor="w", padx=60, pady=10)  # Add padding to center the text vertically
        title_frame = tk.Frame(self.window, bg="#102f54", height=50)  # Adjust height as needed
        title_frame.place(x=1482, y=137.5, anchor="w", width=45)

        # Add new label and textbox for Rate / Hour
        self.label_design2(1501, 177, 'Rate / Hour : ')
        self.textbox_design2(1791, 182)

        # Add new label and textbox for No. of Hours / Cut Off
        self.label_design3(1501, 233, 'No. of Hours / Cut Off : ')
        self.textbox_design2(1791, 237)

        # Add new label and textbox for Income / Cut Off
        self.label_design2(1501, 287.5, 'Income / Cut Off : ')
        self.textbox_design2(1791, 291.5)

# creating other income
    def regular_deductions_frame_title(self):
        self.frame10(606, 380)
        self.frame11(606, 387)
        self.frame12(606, 442)

    # Create a frame for regular deductions
        title_frame_regular_deduction = tk.Frame(self.window, bg="black", height=1)  # Adjust height as needed
        title_frame_regular_deduction.place(x=606, y=357.5, anchor="w", width=1309)  # Use side="bottom" to anchor it at the bottom

    # Create a label for regular deductions
        title_label = tk.Label(title_frame_regular_deduction, text="REGULAR DEDUCTION", fg="white", bg="black",
                           font=("Helvetica", 16, "bold"))
        title_label.pack(anchor="w", padx=60, pady=10)  # Add padding to center the text vertically
        title_frame = tk.Frame(self.window, bg="#102f54", height=50)  # Adjust height as needed
        title_frame.place(x=606, y=357.5, anchor="w", width=40)

    # add new label and textbox for sss contribution
        self.label_design2(625, 397, 'SSS Contribution : ')
        self.textbox_design3(1000, 402)

    # add new label and textbox for phil health contribution
        self.label_design3(625, 452, 'PhilHealth Contribution : ')
        self.textbox_design3(1000, 457)

    # add new label and textbox for pag-ibig contribution
        self.label_design2(1350, 397, 'Pag-ibig Contribution : ')
        self.textbox_design3(1730, 402)

    # add new label and textbox for income tax
        self.label_design3(1350, 452, 'Income Tax : ')
        self.textbox_design3(1730, 457)

# creating other deductions
    def other_deductions_frame_title(self):
        self.frame13(606, 500)
        self.frame11(606, 553)
        self.frame12(606, 608)
        self.frame11(606, 663)

    # Create a frame other deduction
        title_frame_other_deduction = tk.Frame(self.window, bg="black", height=1)  # Adjust height as needed
        title_frame_other_deduction.place(x=606, y=523.5, anchor="w", width=1309)  # Use side="bottom" to anchor it at the bottom

    # Create a label for other deductions
        title_label = tk.Label(title_frame_other_deduction, text="OTHER DEDUCTION", fg="white", bg="black", font=("Helvetica", 16, "bold"))
        title_label.pack(anchor="w", padx=60, pady=10)  # Add padding to center the text vertically
        title_frame = tk.Frame(self.window, bg="#102f54", height=50)  # Adjust height as needed
        title_frame.place(x=606, y=523.5, anchor="w", width=40)

    # add new label and text box for sss loan
        self.label_design2(625, 563, 'SSS Loan : ')
        self.textbox_design3(1000, 568)

    # add new label and text box for pag-ibig load
        self.label_design3(625,618, 'Pag-ibig Load : ')
        self.textbox_design3(1000, 622)

    # add new label and text box for faculty savings deposit
        self.label_design2(625, 673, 'Faculty Savings Deposit : ')
        self.textbox_design3(1730, 568)

    # add new label and text box for salary loan
        self.label_design2(1350, 563, 'Faculty Savings Loan : ')
        self.textbox_design3(1000, 677)

    # add new label and text box for salary loan
        self.label_design3(1350, 618, 'Salary Loan : ')
        self.textbox_design3(1730, 622)

    # add new label and text box for deduction summary
        self.label_design2(1350, 673, 'Other Loan : ')
        self.textbox_design3(1730, 677)

# creating deduction summary
    def deduction_summary_frame_title(self):
        self.frame14(606, 750)
        self.frame11(606, 773)

    # Create a frame for deduction summary
        title_frame_deduction_summary = tk.Frame(self.window, bg="black", height=1)  # Adjust height as needed
        title_frame_deduction_summary.place(x=606, y=743.5, anchor="w", width=1309)  # Use side="bottom" to anchor it at the bottom

    # Create a label for deduction summary
        title_label = tk.Label(title_frame_deduction_summary, text="DEDUCTION SUMMARY", fg="white", bg="black",
                           font=("Helvetica", 16, "bold"))
        title_label.pack(anchor="w", padx=60, pady=10)  # Add padding to center the text vertically
        title_frame = tk.Frame(self.window, bg="#102f54", height=50)  # Adjust height as needed
        title_frame.place(x=606, y=743.5, anchor="w", width=40)

    # add new label for text box for total deduction
        self.label_design2(625, 783, 'Total Deductions : ')
        self.textbox_design3(1730, 783)

# adding a button for gross income, net income, save, update, and new
    def add_button(self):
        # Create footer section with buttons and a frame
        title_frame = tk.Frame(self.window, bg="black", height=1)
        title_frame.place(x=606, y=890, anchor="w", width=1309)
        title_label = tk.Label(title_frame, text="", fg="white", bg="black", font=("Helvetica", 16, "bold"))
        title_label.pack(anchor="w", padx=60, pady=20)

        title_frame = tk.Frame(self.window, bg="#102f54", height=80)
        title_frame.place(x=606, y=890, anchor="w", width=40)

        # uploading button for gross income, net income, save, update, new
        uploadbutton1 = self.button_design1(660, 865)
        uploadbutton2 = self.button_design2(915, 865)
        uploadbutton3 = self.button_design3(1170, 865)
        uploadbutton4 = self.button_design4(1430, 865)
        uploadbutton5 = self.button_design5(1695, 865)

#adding a footer
    def add_footer(self):

        # creating a footer frame
        title_frame = tk.Frame(self.window, bg="#102f54", height=90)
        title_frame.place(x=0, y=1025, anchor="w", width=2000)

        title_frame = tk.Frame(self.window, bg="white", height=10)
        title_frame.place(x=0, y=980, anchor="w", width=2000)
