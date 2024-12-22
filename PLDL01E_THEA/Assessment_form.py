import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title("Assessment Form")
window.state('zoomed')

# Load and resize the image
image = Image.open(r"C:\Users\Worldtech Computer\PycharmProjects\PLDL01E\PLDL01E_THEA\lyceum_cav.jpg")  # Replace with your image path
image = image.resize((100, 100))  # Adjust size as needed
photo = ImageTk.PhotoImage(image)

# Create a frame for the header
header_frame = tk.Frame(window, bg= '#9c2824')
header_frame.pack(fill="x")

# Create a label for the image
image_label = tk.Label(header_frame, image=photo, bg='#9c2824')
image_label.place(x=505, y=5)

# Create a label for the title
title_label = tk.Label(header_frame, text="LYCEUM OF THE PHILIPPINES UNIVERSITY - CAVITE\n1st Semester, AY 2024-2025\nUNOFFICIAL ASSESSMENT FORM",fg='white', bg= '#9c2824', font=("Helvetica", 15,), justify=tk.CENTER)
title_label.pack(side="top", padx=15, pady=23, anchor="center")

class Design_GUI_Interface:
    def __init__(self):
        pass  # No need for unused arguments in the constructor

    def frames(self, x, y):
        self.frame1 = Frame(window, width=2000, height=100, borderwidth=0, bg='light grey')
        self.frame1.place(x=x, y=y)

    def frames2(self, x, y):
        self.frame1 = Frame(window, width=2000, height=425, borderwidth=0, bg='light grey')
        self.frame1.place(x=x, y=y)

    def frames3(self, x, y):
        self.frame1 = Frame(window, width=2000, height=50, borderwidth=0, bg='#c9c8c8')
        self.frame1.place(x=x, y=y)

    def frames4(self, x, y):
        self.frame1 = Frame(window, width=2000, height=50, borderwidth=0, bg='#bab7b7')
        self.frame1.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=35, height=1, fg='black', bg='white',
        font=('Helvetica', 11, 'bold'), )
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=15, height=1, fg='black', bg='white',
        font=('Helvetica', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def textbox_design3(self, x, y):
        self.textbox = Text(width=45, height=1, fg='black', bg='white',
        font=('Helvetica', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def textbox_design4(self, x, y):
        self.textbox = Text(width=10, height=1, fg='black', bg='white',
        font=('Helvetica', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def textbox_design5(self, x, y):
        self.textbox = Text(width=20, height=1, fg='black', bg='white',
        font=('Helvetica', 11, 'bold'))
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.lbl = Label(text=text_value, bg='light grey', fg='black', font=('Helvetica', 11, 'bold'))
        self.lbl.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.lbl = Label(text=text_value, bg='light grey', fg='black', font=('Helvetica', 9))
        self.lbl.place(x=x, y=y)

    def label_design3(self, x, y, text_value):
        self.lbl = Label(text=text_value, bg='light grey', fg='black', font=('Helvetica', 9, 'bold'))
        self.lbl.place(x=x, y=y)

    def label_design4(self, x, y, text_value):
        self.lbl = Label(text=text_value, bg='light grey', fg='black', font=('Helvetica', 10, 'bold'))
        self.lbl.place(x=x, y=y)

    def label_design5(self, x, y, text_value):
        self.lbl = Label(text=text_value, bg='light grey', fg='black', font=('Helvetica', 8))
        self.lbl.place(x=x, y=y)

    def combo_field(self, x, y, combo_values):
        self.n = tk.StringVar()
        self.combo_fields = ttk.Combobox(window, width=25, textvariable=self.n)
        self.combo_fields['values'] = combo_values
        self.combo_fields.place(x=x, y=y)
        self.combo_fields.current()

    def button_design(self, x, y):
        self.upload_button = Button(width=15, pady=7, text='Save File',
        bg='white', fg='black', cursor='hand2', border=0)  # Corrected 'boarder' to 'border'
        self.upload_button.place(x=x, y=y)

my_gui_design = Design_GUI_Interface()

# Create frames using methods
my_gui_design.frames(1, 125)
my_gui_design.frames3(1, 310)
my_gui_design.frames4(1, 360)
my_gui_design.frames3(1, 410)
my_gui_design.frames4(1, 460)
my_gui_design.frames3(1, 510)
my_gui_design.frames4(1, 560)
my_gui_design.frames3(1, 610)
my_gui_design.frames4(1, 660)
my_gui_design.frames2(1, 760)

# Create a frame for the Class Schedule
title_frame = tk.Frame(window, bg="white", height=1)  # Adjust height as needed
title_frame.place(x=0, y=250, anchor="w", relwidth=1)

# Create a label for the Class Schedule
title_label = tk.Label(title_frame, text="CLASS SCHEDULE", fg="black",bg="white", font=("Helvetica", 16, "bold"))
title_label.pack(pady=2)  # Add padding to center the text vertically

# Create a frame for the table headers
table_header_frame = tk.Frame(window, bg='#a2a2a2', height=1)
table_header_frame.place(x=0, y=293, anchor="w", relwidth=1)

subject_code_label = tk.Label(table_header_frame, text="SUBJECT CODE", font=("Helvetica", 13, "bold"), bg='#a2a2a2')
subject_code_label.pack(side="left", padx=50, pady=5)

course_description_label = tk.Label(table_header_frame, text="COURSE DESCRIPTION", font=("Helvetica", 13, "bold"), bg='#a2a2a2')
course_description_label.pack(side="left", padx=150, pady=5)

section_label = tk.Label(table_header_frame, text="SECTION", font=("Helvetica", 13, "bold"), bg='#a2a2a2')
section_label.pack(side="left", padx=50, pady=5)

time_label = tk.Label(table_header_frame, text="TIME", font=("Helvetica", 13, "bold"), bg='#a2a2a2')
time_label.pack(side="left", padx=100, pady=5)

days_label = tk.Label(table_header_frame, text="DAYS", font=("Helvetica", 13, "bold"), bg='#a2a2a2')
days_label.pack(side="left", padx=100, pady=5)

room_label = tk.Label(table_header_frame, text="ROOM", font=("Helvetica", 13, "bold"), bg='#a2a2a2')
room_label.pack(side="left", padx=100, pady=5)

units_label = tk.Label(table_header_frame, text="UNITS", font=("Helvetica", 13, "bold"), bg='#a2a2a2')
units_label.pack(side="left", padx=100, pady=5)

# Create text boxes (consider using variables for clarity)
applicantidtxt = my_gui_design.textbox_design1(200, 145)
nametxt = my_gui_design.textbox_design1(200,185)
coursetxt = my_gui_design.textbox_design1(1550,145)
collegetxt = my_gui_design.textbox_design1(1550,185 )

#textbox label for first frame
applicantide_lbl = my_gui_design.label_design(65, 145, 'APPLICANT ID :')
name_lbl = my_gui_design.label_design(65,185, 'NAME :' )
course_lbl = my_gui_design.label_design(1445,145, 'COURSE :')
college_lbl = my_gui_design.label_design(1445, 185, 'COLLEGE :')

# Creating text boxes for Subject Code
subjectcode1txt = my_gui_design.textbox_design2(55, 324)
subjectcode2txt = my_gui_design.textbox_design2(55, 373)
subjectcode3txt = my_gui_design.textbox_design2(55, 424)
subjectcode4txt = my_gui_design.textbox_design2(55, 473)
subjectcode5txt = my_gui_design.textbox_design2(55, 524)
subjectcode6txt = my_gui_design.textbox_design2(55, 573)
subjectcode7txt = my_gui_design.textbox_design2(55, 624)

#Creating text boxes for Course Description
course_description1txt = my_gui_design.textbox_design3(300, 324)
course_description2txt = my_gui_design.textbox_design3(300, 373)
course_description3txt = my_gui_design.textbox_design3(300, 424)
course_description4txt = my_gui_design.textbox_design3(300, 473)
course_description5txt = my_gui_design.textbox_design3(300, 524)
course_description6txt = my_gui_design.textbox_design3(300, 573)
course_description7txt = my_gui_design.textbox_design3(300, 624)

#Creating text boxes for Section
section1txt = my_gui_design.textbox_design4(777, 324)
section2txt = my_gui_design.textbox_design4(777, 373)
section3txt = my_gui_design.textbox_design4(777, 424)
section4txt = my_gui_design.textbox_design4(777, 473)
section5txt = my_gui_design.textbox_design4(777, 524)
section6txt = my_gui_design.textbox_design4(777, 573)
section7txt = my_gui_design.textbox_design4(777, 624)

#Creating text boxes for time
time1txt = my_gui_design.textbox_design5(955, 324)
time2txt = my_gui_design.textbox_design5(955, 373)
time3txt = my_gui_design.textbox_design5(955, 424)
time4txt = my_gui_design.textbox_design5(955, 473)
time5txt = my_gui_design.textbox_design5(955, 524)
time6txt = my_gui_design.textbox_design5(955, 573)
time7txt = my_gui_design.textbox_design5(955, 624)

# Creating text boxes for Days
day1txt = my_gui_design.textbox_design4(1237, 324)
day2txt = my_gui_design.textbox_design4(1237, 373)
day3txt = my_gui_design.textbox_design4(1237, 424)
day4txt = my_gui_design.textbox_design4(1237, 473)
day5txt = my_gui_design.textbox_design4(1237, 524)
day6txt = my_gui_design.textbox_design4(1237, 573)
day7txt = my_gui_design.textbox_design4(1237, 624)

#Creating text boxes for Room
room1txt = my_gui_design.textbox_design2(1470, 324)
room2txt = my_gui_design.textbox_design2(1470, 373)
room3txt = my_gui_design.textbox_design2(1470, 424)
room4txt = my_gui_design.textbox_design2(1470, 473)
room5txt = my_gui_design.textbox_design2(1470, 524)
room6txt = my_gui_design.textbox_design2(1470, 573)
room7txt = my_gui_design.textbox_design2(1470, 624)

#Creating text boxes for Units
units1txt = my_gui_design.textbox_design2(1725, 324)
units2txt = my_gui_design.textbox_design2(1725, 373)
units3txt = my_gui_design.textbox_design2(1725, 424)
units4txt = my_gui_design.textbox_design2(1725, 473)
units5txt = my_gui_design.textbox_design2(1725, 524)
units6txt = my_gui_design.textbox_design2(1725, 573)
units7txt = my_gui_design.textbox_design2(1725, 624)
totalunitstxt = my_gui_design.textbox_design2(1725, 673)

#Creating frame and text boxes for total units
table_header_frame = tk.Frame(window, height=1, bg='#bab7b7')
table_header_frame.place(x=5, y=670)

# Create a label for the total units
total_units_label = tk.Label(table_header_frame, text="TOTAL UNITS", font=("Helvetica", 13, "bold"), bg='#bab7b7')
total_units_label.pack(side="left", padx=50, pady=5)

# Create a label for the Payment Information
title_frame = tk.Frame(window, bg="white", height=1)  # Adjust height as needed
title_frame.place(x=0, y=735, anchor="w", relwidth=1)  # Use side="bottom" to anchor it at the bottom

# Create a label for the student information
title_label = tk.Label(title_frame, text="ASSESSMENT FEES", fg="black",bg="white", font=("Helvetica", 16, "bold"))
title_label.pack(pady=2)  # Add padding to center the text vertically

# Creating a label for assessment fee
tuitionfee_lbl = my_gui_design.label_design(55, 770, 'TUITION FEE')
miscellaneousfees_lbl = my_gui_design.label_design(55, 805, 'TOTAL MISCELLANEOUS FEES')
laboratory_otherfees_lbl = my_gui_design.label_design(55,840, 'TOTAL LABORATORY AND OTHER FEES')

#Creating a label for the amount of assessment fee
tuitionfee2_lbl = my_gui_design.textbox_design2( 1725, 770)
miscellaneousfees2_lbl = my_gui_design.textbox_design2( 1725, 805)
laboratoryandotherfeeslbl = my_gui_design.textbox_design2(1725, 840)

# creating a frame/divider
title_frame = tk.Frame(window, bg="black", height=2)  # Adjust height as needed
title_frame.place(x=0, y=837, anchor="w", relwidth=1)
title_frame = tk.Frame(window, bg="black", height=2)  # Adjust height as needed
title_frame.place(x=0, y=867, anchor="w", relwidth=1)

# creating a label for laboratory and other fees
exambooklet_lbl = my_gui_design.label_design2(65, 875, 'EXAM BOOKLET')
lmsfee_lbl = my_gui_design.label_design2(65, 900, 'LMS FEE')
professionalengineeringlaboratoryfee_lbl = my_gui_design.label_design2(875, 875, 'PROFESSIONAL ENGINEERING LABORATORY FEE')
computerlaboratoryfee_lbl = my_gui_design.label_design2(450, 875, 'COMPUTER LABORATORY FEE')
computerlaboratoryfee2_lbl = my_gui_design.label_design2(450, 900, "COMPUTER LABORATORY FEE 2")

totalassessment_lbl = my_gui_design.label_design3(1500, 880, 'TOTAL ASSESSMENT FEE')
addinstallmentcharge_lbl = my_gui_design.label_design2(1500, 910, 'ADD: INSTALLMENT CHARGE')
totalamountdue_lbl = my_gui_design.label_design3(1500, 950, 'TOTAL AMOUNT DUE')
lesspaymentmade_lbl = my_gui_design.label_design2(1500, 980, 'LESS: PAYMENT MADE')
balance_lbl = my_gui_design.label_design3(1500, 1020, 'BALACE (PAYABLE INSTALLMENTS)')

# creating a textbox for laboratory and other fees
exambooklettxt = my_gui_design.textbox_design4(300, 875)
lmsfeetxt = my_gui_design.textbox_design4(300, 900)
professionalengineeringlaboratoryfee_lbl = my_gui_design.textbox_design4(1250, 875)
computerlaboratoryfee_lbl = my_gui_design.textbox_design4(725, 875)
computerlaboratoryfee2_lbl = my_gui_design.textbox_design4(725, 900)

totalassessmenttxt = my_gui_design.textbox_design2(1725, 880)
addinstallmentchargetxt = my_gui_design.textbox_design2(1725, 910)
totalamountduetxt = my_gui_design.textbox_design2(1725, 950)
lesspaymentmadetxt = my_gui_design.textbox_design2(1725, 980)
balancetxt = my_gui_design.textbox_design2(1725, 1020)

#divider for total amount due
title_frame = tk.Frame(window, bg="black", height=2)  # Adjust height as needed
title_frame.place(x=1503, y=940, width=345)
title_frame = tk.Frame(window, bg="black", height=2)  # Adjust height as needed
title_frame.place(x=1503, y=1010, width=345)

#creating a label for installment payment schedule
installmentpaymentschedule_lbl = my_gui_design.label_design4(655, 935, 'INSTALLMENT PAYMENT SCHEDULE')
payment_lbl = my_gui_design.label_design3(250, 955, 'PAYMENT')
duedate_lbl = my_gui_design.label_design3(733, 955, 'DUE DATE')
minimumumamountdue_lbl = my_gui_design.label_design3(1150, 955, 'MINIMUM AMOUNT DUE')
firstinstallment_lbl = my_gui_design.label_design5(250, 980, '1ST INSTALLMENT')
secondinstallment_lbl = my_gui_design.label_design5(250, 1005, '2ND INSTALLMENT')
thirdinstallment_lbl = my_gui_design.label_design5(250, 1030, '3RD INSTALLMENT')

#creating a textbox for installment payment schedule
duefirstinstallmenttxt = my_gui_design.textbox_design4(725, 980)
duesecondinstallmenttxt = my_gui_design.textbox_design4(725, 1005 )
duesecondinstallmenttxt = my_gui_design.textbox_design4(725, 1030 )

minimumamountduefirstinstallmenttxt = my_gui_design.textbox_design4(1175, 980)
minimumamountduesecondinstallmenttxt = my_gui_design.textbox_design4(1175, 1005)
minimumamountduethirdinstallmenttxt = my_gui_design.textbox_design4(1175, 1030)

#call for the button and place under the image
uploadbutton = my_gui_design.button_design(1725, 65)

window.mainloop()