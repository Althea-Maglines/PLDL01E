import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("Payroll Page Design")
window.state('zoomed')
window.configure(bg="#dbd2c1")

class Payroll_Page_Design:
    def __init__(self):
        pass  # No need for unused arguments in the constructor

    def frame(self, x, y):
        self.frames = Frame(window, width=600, height=1000, borderwidth=0, bg='#ebeae7')
        self.frames.place(x=x, y=y)

    def frame2(self, x, y):
        self.frames2 = Frame(window, width=433, height=165, borderwidth=0, bg='#ebeae7')
        self.frames2.place(x=x, y=y)

    def frame3(self, x, y):
        self.frames3 = Frame(window, width=433, height=165, borderwidth=0, bg='#ebeae7')
        self.frames3.place(x=x, y=y)

    def frame4(self, x, y):
        self.frames4 = Frame(window, width=433, height=165, borderwidth=0, bg='#ebeae7')
        self.frames4.place(x=x, y=y)

    def frame5(self, x, y):
        self.frames5 = Frame(window, width=600, height=280, borderwidth=0, bg='#aaaaaa')
        self.frames5.place(x=x, y=y)

    def frame6(self, x, y):
        self.frames6 = Frame(window, width=600, height=50, borderwidth=0, bg='white')
        self.frames6.place(x=x, y=y)

    def frame7(self, x, y):
        self.frames7 = Frame(window, width=600, height=50, borderwidth=0, bg='#e8e8e8')
        self.frames7.place(x=x, y=y)

    def frame8(self, x, y):
        self.frames8 = Frame(window, width=433, height=50, borderwidth=0, bg='white')
        self.frames8.place(x=x, y=y)

    def frame9(self, x, y):
        self.frames9 = Frame(window, width=433, height=50, borderwidth=0, bg='#e8e8e8')
        self.frames9.place(x=x, y=y)

    def frame10(self, x, y):
        self.frames10 = Frame(window, width=1309, height=100, borderwidth=0, bg='#ebeae7')
        self.frames10.place(x=x, y=y)

    def frame11(self, x, y):
        self.frames11 = Frame(window, width=1309, height=50, borderwidth=0, bg='white')
        self.frames11.place(x=x, y=y)

    def frame12(self, x, y):
        self.frames12 = Frame(window, width=1309, height=50, borderwidth=0, bg='#e8e8e8')
        self.frames12.place(x=x, y=y)

    def frame13(self, x, y):
        self.frames13 = Frame(window, width=1309, height=200, borderwidth=0, bg='#ebeae7')
        self.frames13.place(x=x, y=y)

    def frame14(self, x, y):
        self.frames14 = Frame(window, width=1309, height=50, borderwidth=0, bg='#ebeae7')
        self.frames14.place(x=x, y=y)

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

    def label_design(self, x, y, text_value):
        self.lbl = Label(text=text_value, bg='#7c7c7c', fg='white', font=('Helvetica', 25, 'bold'))
        self.lbl.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.lbl = Label(text=text_value, bg='white', fg='#3d3d3d', font=('Helvetica', 16, 'bold'))
        self.lbl.place(x=x, y=y)

    def label_design3(self, x, y, text_value):
        self.lbl = Label(text=text_value, bg='#e8e8e8', fg='#3d3d3d', font=('Helvetica', 16   , 'bold'))
        self.lbl.place(x=x, y=y)

    def button_design(self, x, y):
        self.upload_button = Button(width=20, pady=7, text='SEARCH EMPLOYEE', bg='#102f54', fg='white',
        font=('Helvetica', 13, 'bold'), cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def button_design1(self, x, y):
        self.upload_button = Button(width=20, pady=7, text='GROSS INCOME', bg='#102f54', fg='white',
                                    font=('Helvetica', 13, 'bold'), cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def button_design2(self, x, y):
        self.upload_button = Button(width=20, pady=7, text='NET INCOME', bg='#102f54', fg='white',
                                    font=('Helvetica', 13, 'bold'), cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def button_design3(self, x, y):
        self.upload_button = Button(width=20, pady=7, text='SAVE', bg='#102f54', fg='white',
                                    font=('Helvetica', 13, 'bold'), cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def button_design4(self, x, y):
        self.upload_button = Button(width=20, pady=7, text='UPDATE', bg='#102f54', fg='white',
                                    font=('Helvetica', 13, 'bold'), cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

    def button_design5(self, x, y):
        self.upload_button = Button(width=20, pady=7, text='NEW', bg='#102f54', fg='white',
                                    font=('Helvetica', 13, 'bold'), cursor='hand2', border=0)
        self.upload_button.place(x=x, y=y)

my_gui_design = Payroll_Page_Design()

# Create frames
my_gui_design.frame(0, 157)
my_gui_design.frame2(606, 157)
my_gui_design.frame3(1044, 157)
my_gui_design.frame4(1482, 157)
my_gui_design.frame6(0, 425)
my_gui_design.frame7(0, 480)
my_gui_design.frame6(0, 535)
my_gui_design.frame7(0, 590)
my_gui_design.frame6(0, 645)
my_gui_design.frame7(0, 700)
my_gui_design.frame6(0, 755)
my_gui_design.frame7(0, 810)
my_gui_design.frame6(0, 865)
my_gui_design.frame7(0, 920)
my_gui_design.frame10(606, 380)
my_gui_design.frame13(606, 500)
my_gui_design.frame14(606, 750)

#creating a header title
# Create a frame for the header
header_frame = tk.Frame(window, bg= '#102f54')
header_frame.pack(fill="x",pady=1)

# Create a label for the title header
title_label = tk.Label(header_frame, text="MINA'S CHOICE PAYROLL",fg='white', bg= '#102f54', font=("Helvetica", 20, "bold"))
title_label.pack(padx=25, pady=35, anchor="center")

# Create a frame for employee basic info
title_frame = tk.Frame(window, bg="black", height=1)  # Adjust height as needed
title_frame.place(x=0, y=137.5, anchor="w", width=600)  # Use side="bottom" to anchor it at the bottom

# Create a label for employee basic info
title_label = tk.Label(title_frame, text="EMPLOYEE BASIC INFORMATION", fg="white",bg="black", font=("Helvetica", 16, "bold"))
title_label.pack(anchor="w", padx=55, pady=10)  # Add padding to center the text vertically
title_frame = tk.Frame(window, bg="#102f54", height=50)  # Adjust height as needed
title_frame.place(x=0, y=137.5, anchor="w", width=40)

# profile photo
image_path = r"C:\Users\Worldtech Computer\PycharmProjects\PLDL01E\PLDL01E_THEA\black_profile.jpg"  # Replace with your actual path
image = Image.open(image_path)
image = image.resize((160, 150))  # Adjust size as needed
photo_image = ImageTk.PhotoImage(image)

# Create a label for the first image
first_image_label = Label(image=photo_image, bg='#343434')
first_image_label.place(x=200, y=185)  # Adjust coordinates as needed

# Create a frame for basic income
title_frame = tk.Frame(window, bg="black", height=1)  # Adjust height as needed
title_frame.place(x=606, y=137.5, anchor="w", width=433)  # Use side="bottom" to anchor it at the bottom

# Create a label for basic income
title_label = tk.Label(title_frame, text="BASIC INCOME", fg="white",bg="black", font=("Helvetica", 16, "bold"))
title_label.pack(anchor="w", padx=60, pady=10)  # Add padding to center the text vertically
title_frame = tk.Frame(window, bg="#102f54", height=50)  # Adjust height as needed
title_frame.place(x=606, y=137.5, anchor="w", width=45)

# Create a frame for honorarium income
title_frame = tk.Frame(window, bg="black", height=1)  # Adjust height as needed
title_frame.place(x=1044, y=137.5, anchor="w", width=433)  # Use side="bottom" to anchor it at the bottom

# Create a label for honorarium income
title_label = tk.Label(title_frame, text="HONORARIUM INCOME", fg="white",bg="black", font=("Helvetica", 16, "bold"))
title_label.pack(anchor="w", padx=60, pady=10)  # Add padding to center the text vertically
title_frame = tk.Frame(window, bg="#102f54", height=50)  # Adjust height as needed
title_frame.place(x=1044, y=137.5, anchor="w", width=45)

# Create a frame for other income
title_frame = tk.Frame(window, bg="black", height=1)  # Adjust height as needed
title_frame.place(x=1482, y=137.5, anchor="w", width=433)  # Use side="bottom" to anchor it at the bottom

# Create a label for other income
title_label = tk.Label(title_frame, text="OTHER INCOME", fg="white",bg="black", font=("Helvetica", 16, "bold"))
title_label.pack(anchor="w", padx=60, pady=10)  # Add padding to center the text vertically
title_frame = tk.Frame(window, bg="#102f54", height=50)  # Adjust height as needed
title_frame.place(x=1482, y=137.5, anchor="w", width=45)

# creating a label for employee basic info
firstname_lbl = my_gui_design.label_design2(25, 435.5, 'First Name : ')
middlename_lbl = my_gui_design.label_design3(25, 490.5, 'Middle Name : ')
surname_lbl = my_gui_design.label_design2(25, 545.5, 'Last Name : ')
civil_status_lbl = my_gui_design.label_design3(25, 600.5, 'Civil Status : ')
qualified_dependent_status_lbl = my_gui_design.label_design2(25, 654.5, 'Qualified Dependents Status : ')
paydate_lbl = my_gui_design.label_design3(25, 710.5, 'Paydate : ')
employeestatues_lbl = my_gui_design.label_design2(25, 765.5, 'Employee Status : ')
designation_lbl = my_gui_design.label_design3(25, 820.5, 'Designation : ')
employeenumber_lbl = my_gui_design.label_design2(25, 875.5, 'Employee Number : ')
department_lbl = my_gui_design.label_design3(25, 930.5, 'Department : ')

# creating a text box for employee basic info
firstnametxt = my_gui_design.textbox_design1(370,440)
middlenametxt = my_gui_design.textbox_design1(370, 495)
surnametxt = my_gui_design.textbox_design1(370, 550)
civilstatustxt = my_gui_design.textbox_design1(370, 605)
qualifieddependentstatustxt = my_gui_design.textbox_design1(370, 660)
paydatetxt = my_gui_design.textbox_design1(370, 715)
employeestatuestxt = my_gui_design.textbox_design1(370, 770)
designationtxt = my_gui_design.textbox_design1(370, 825)
employeenumbertxt = my_gui_design.textbox_design1(370, 880)
departmenttxt = my_gui_design.textbox_design1(370, 935)

#design for frame
title_frame = tk.Frame(window, bg="white", height=5)  # Adjust height as needed
title_frame.place(x=0, y=106, anchor="w", relwidth=1)

#call for the button search employee
uploadbutton = my_gui_design.button_design(180, 360)

# creating frames for basic income
my_gui_design.frame8(606, 167)
my_gui_design.frame9(606, 222)
my_gui_design.frame8(606, 277)

# creating a label for basic income
rateperhr_lbl = my_gui_design.label_design2(625, 177, 'Rate / Hour : ')
numhrs_cutoff_lbl = my_gui_design.label_design3(625, 233, 'No. of Hours / Cut Off : ')
income_cutoff_lbl = my_gui_design.label_design2(625, 287.5, 'Income / Cut Off : ')

# Creating a text box for basic income
rateperhrtxt = my_gui_design.textbox_design2(915, 182)
numhrs_cutofftxt = my_gui_design.textbox_design2(915, 237)
income_cutofftxt = my_gui_design.textbox_design2(915, 291.5)


# creating frames for honorarium income
my_gui_design.frame8(1044, 167)
my_gui_design.frame9(1044, 222)
my_gui_design.frame8(1044, 277)

# creating a label for honorarium income
rateperhr1_lbl = my_gui_design.label_design2(1063, 177, 'Rate / Hour : ')
numhrs_cutoff1_lbl = my_gui_design.label_design3(1063, 233, 'No. of Hours / Cut Off : ')
income_cutoff1_lbl = my_gui_design.label_design2(1063, 287.5, 'Income / Cut Off : ')

# Creating a text box for honorarium income
rateperhr1txt = my_gui_design.textbox_design2(1353, 182)
numhrs_cutoff1txt = my_gui_design.textbox_design2(1353, 237)
income_cutoff1txt = my_gui_design.textbox_design2(1353, 291.5)

# creating frames for other income
my_gui_design.frame8(1482, 167)
my_gui_design.frame9(1482, 222)
my_gui_design.frame8(1482, 277)

# creating a label for other income
rateperhr2_lbl = my_gui_design.label_design2(1501, 177, 'Rate / Hour : ')
numhrs_cutoff2_lbl = my_gui_design.label_design3(1501, 233, 'No. of Hours / Cut Off : ')
income_cutoff2_lbl = my_gui_design.label_design2(1501, 287.5, 'Income / Cut Off : ')

# Creating a text box for other income
rateperhr2txt = my_gui_design.textbox_design2(1791, 182)
numhrs_cutoff2txt = my_gui_design.textbox_design2(1791, 237)
income_cutoff2txt = my_gui_design.textbox_design2(1791, 291.5)

# Create a frame for regular deductions
title_frame = tk.Frame(window, bg="black", height=1)  # Adjust height as needed
title_frame.place(x=606, y=357.5, anchor="w", width=1309)  # Use side="bottom" to anchor it at the bottom

# Create a label for regular deductions
title_label = tk.Label(title_frame, text="REGULAR DEDUCTION", fg="white",bg="black", font=("Helvetica", 16, "bold"))
title_label.pack(anchor="w", padx=60, pady=10)  # Add padding to center the text vertically
title_frame = tk.Frame(window, bg="#102f54", height=50)  # Adjust height as needed
title_frame.place(x=606, y=357.5, anchor="w", width=40)

# creating frames for regular deductions
my_gui_design.frame11(606, 387)
my_gui_design.frame12(606, 442)

# creating a label for regular deductions
ssscontrib_lbl = my_gui_design.label_design2(625, 397, 'SSS Contribution : ')
philhlthcontrib_lbl = my_gui_design.label_design3(625, 452, 'PhilHealth Contribution : ')
pagibigcontrib_lbl = my_gui_design.label_design2(1350, 397, 'Pag-ibig Contribution : ')
incometax_lbl = my_gui_design.label_design3(1350, 452, 'Income Tax : ')

# creating a text box for regular deductions
ssscontribtxt = my_gui_design.textbox_design3(1000, 402)
philhlthcontribtxt = my_gui_design.textbox_design3(1000, 457)
pagibigcontribtxt = my_gui_design.textbox_design3(1730, 402)
incometaxtxt = my_gui_design.textbox_design3(1730, 457)

# Create a frame other deduction
title_frame = tk.Frame(window, bg="black", height=1)  # Adjust height as needed
title_frame.place(x=606, y=523.5, anchor="w", width=1309)  # Use side="bottom" to anchor it at the bottom

# Create a label for other deductions
title_label = tk.Label(title_frame, text="OTHER DEDUCTION", fg="white",bg="black", font=("Helvetica", 16, "bold"))
title_label.pack(anchor="w", padx=60, pady=10)  # Add padding to center the text vertically
title_frame = tk.Frame(window, bg="#102f54", height=50)  # Adjust height as needed
title_frame.place(x=606, y=523.5, anchor="w", width=40)

# creating frames for other deduction
my_gui_design.frame11(606, 553)
my_gui_design.frame12(606, 608)
my_gui_design.frame11(606, 663)

#creating a label for other deduction
sssloan_lbl = my_gui_design.label_design2(625, 563, 'SSS Loan : ')
pagibigload_lbl = my_gui_design.label_design3(625,618, 'Pag-ibig Load : ')
facultysavingsdeposit_lbl = my_gui_design.label_design2(625, 673, 'Faculty Savings Deposit : ')
facultysavingsloan_lbl = my_gui_design.label_design2(1350, 563, 'Faculty Savings Loan : ')
salaryloan_lbl = my_gui_design.label_design3(1350, 618, 'Salary Loan : ')
otherloan_lbl = my_gui_design.label_design2(1350, 673, 'Other Loan : ')

#creating a text box for other deduction
sssloantxt = my_gui_design.textbox_design3(1000, 568)
pagibigloadtxt= my_gui_design.textbox_design3(1000, 622)
facultysavingsdeposit = my_gui_design.textbox_design3(1000, 677)
facultysavingsloantxt = my_gui_design.textbox_design3(1730, 568)
salaryloantxt = my_gui_design.textbox_design3(1730, 622)
otherloantxt = my_gui_design.textbox_design3(1730, 677)

# Create a frame for deduction summary
title_frame = tk.Frame(window, bg="black", height=1)  # Adjust height as needed
title_frame.place(x=606, y=743.5, anchor="w", width=1309)  # Use side="bottom" to anchor it at the bottom

# Create a label for deduction summary
title_label = tk.Label(title_frame, text="DEDUCTION SUMMARY", fg="white",bg="black", font=("Helvetica", 16, "bold"))
title_label.pack(anchor="w", padx=60, pady=10)  # Add padding to center the text vertically
title_frame = tk.Frame(window, bg="#102f54", height=50)  # Adjust height as needed
title_frame.place(x=606, y=743.5, anchor="w", width=40)

# creating frames for deduction summary
my_gui_design.frame11(606, 773)

#creating a label for deduction summary
totaldeduct_label = my_gui_design.label_design2(625, 783, 'Total Deductions : ')

#creating a text box for deduction summary
totaldeducttxt = my_gui_design.textbox_design3(1730, 783)

# Create a frame for button
title_frame = tk.Frame(window, bg="black", height=1)  # Adjust height as needed
title_frame.place(x=606, y=890, anchor="w", width=1309)  # Use side="bottom" to anchor it at the bottom
title_label = tk.Label(title_frame, text="", fg="white",bg="black", font=("Helvetica", 16, "bold"))
title_label.pack(anchor="w", padx=60, pady=20)  # Add padding to center the text vertically
title_frame = tk.Frame(window, bg="#102f54", height=80)  # Adjust height as needed
title_frame.place(x=606, y=890, anchor="w", width=40)

# uploading button for gross income, net income, save, update, new
uploadbutton1 = my_gui_design.button_design1(660, 865)
uploadbutton2 = my_gui_design.button_design2(915, 865)
uploadbutton3 = my_gui_design.button_design3(1170, 865)
uploadbutton4 = my_gui_design.button_design4(1430, 865)
uploadbutton5 = my_gui_design.button_design5(1695, 865)

#creating a footer
title_frame = tk.Frame(window, bg="#102f54", height=90)  # Adjust height as needed
title_frame.place(x=0, y=1025, anchor="w", width=2000)
title_frame = tk.Frame(window, bg="white", height=10)  # Adjust height as needed
title_frame.place(x=0, y=980, anchor="w", width=2000)


window.mainloop()