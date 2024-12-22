import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title("Meralco Form")
window.state('zoomed')

# Load and resize the image
image = Image.open(r"C:\Users\Worldtech Computer\PycharmProjects\PLDL01E\PLDL01E_THEA\meralco_03.jpg")  # Replace with your image path
image = image.resize((160, 30))  # Adjust size as needed
photo = ImageTk.PhotoImage(image)
window.configure(bg="#ffcfb1")

# Create a frame for the header
header_frame = tk.Frame(window, bg= '#e85d04')
header_frame.pack(fill="x",pady=1)

# Create a label for the image
image_label = tk.Label(header_frame, image=photo, bg='#e85d04')
image_label.place(x=200, y=35)

# Create a label for the title APPLICATION FORM
title_label = tk.Label(header_frame, text="APPLICATION FORM",fg='white', bg= '#e85d04', font=("Helvetica", 20, "bold"))
title_label.pack(padx=25, pady=35, anchor="center")

image2_path = (r"C:\Users\Worldtech Computer\PycharmProjects\PLDL01E\PLDL01E_THEA\meral.jpeg")  # Replace with your image path
image2 = Image.open(image2_path)
image2 = image2.resize((100, 70))  # Adjust size as needed
photo_image2 = ImageTk.PhotoImage(image2)  # Use a unique name

# Create a label for the second image (within the header frame)
second_image_label = tk.Label(header_frame, image=photo_image2, bg='#e85d04')
second_image_label.place(x=95, y=15)  # Adjust coordinates as needed

class Design_GUI_Interface:
    def __init__(self):
        pass  # No need for unused arguments in the constructor

    def frames(self, x, y):
        self.frame1 = Frame(window, width=2000, height=100, borderwidth=0, bg='#E0FFFF')
        self.frame1.place(x=x, y=y)

    def frames2(self, x, y):
        self.frame1 = Frame(window, width=2000, height=195, borderwidth=0, bg='#E0FFFF')
        self.frame1.place(x=x, y=y)

    def frame3(self, x, y):
        self.frame1 = Frame(window, width=2000, height=230, borderwidth=0, bg='#E0FFFF')
        self.frame1.place(x=x, y=y)

    def textbox_design1(self, x, y):
        self.textbox = Text(width=20, height=1, fg='black', bg='white',
        font=('Helvetica', 11, 'bold'), )
        self.textbox.place(x=x, y=y)

    def textbox_design2(self, x, y):
        self.textbox = Text(width=25, height=1, fg='black', bg='white',
        font=('Helvetica', 11, 'bold'), )
        self.textbox.place(x=x, y=y)

    def textbox_design3(self, x, y):
        self.textbox = Text(width=50, height=1, fg='black', bg='white',
        font=('Helvetica', 11, 'bold'), )
        self.textbox.place(x=x, y=y)

    def textbox_design4(self, x, y):
        self.textbox = Text(width=55, height=3, fg='black', bg='white',
        font=('Helvetica', 11, 'bold'), )
        self.textbox.place(x=x, y=y)

    def label_design(self, x, y, text_value):
        self.lbl = Label(text=text_value, bg='#E0FFFF', fg='black', font=('Helvetica', 13, 'bold'))
        self.lbl.place(x=x, y=y)

    def label_design2(self, x, y, text_value):
        self.lbl = Label(text=text_value, bg='#E0FFFF', fg='black', font=('Helvetica', 10))
        self.lbl.place(x=x, y=y)

    def label_design3(self, x, y, text_value):
        self.lbl = Label(text=text_value, bg='black', fg='white', font=('Arial', 13, 'bold'))
        self.lbl.place(x=x, y=y)

    def button_design(self, x, y):
        self.upload_button = Button(width=15, pady=7, text='Save File', bg='#e85d04', fg='black',
                                    cursor='hand2', border=0)  # Corrected 'boarder' to 'border'
        self.upload_button.place(x=x, y=y)

my_gui_design = Design_GUI_Interface()
# Create frames using methods
my_gui_design.frames(1, 157)
my_gui_design.frames2(1,305)
my_gui_design.frame3(1, 548)

# Create a frame for application details
title_frame = tk.Frame(window, bg="white", height=1)  # Adjust height as needed
title_frame.place(x=0, y=133, anchor="w", relwidth=1)  # Use side="bottom" to anchor it at the bottom

# Create a label for service application details
title_label = tk.Label(title_frame, text="SERVICE APPLICATION DETAILS", fg="black",bg="white", font=("Helvetica", 16, "bold"))
title_label.pack(side="left", padx=35, pady=5)  # Add padding to center the text vertically

# Creating a combo box for service type
options = ["PREPAID ELECTRICITY", "SERVICE APPLICATION", "PEAK/OFF-PEAK", "NET METERING", "DISTRIBUTED ENERGY RESOURCES", "PROTECTED LINE COVERS"]
combo_box = ttk.Combobox(window, values=options, font=('Helvetica', 12), width=25)  # Adjusted width
combo_box.place(x=90, y=212)  # Coordinates for the combo box

# Creating a combo box for service bundle
options = ["FULL BUNDLE", "TECHNICAL BUNDLE", "PROCESSING BUNDLE", "DOCUMENTARY BUNDLE"]
combo_box = ttk.Combobox(window, values=options, font=('Helvetica', 12), width=25)  # Adjusted width
combo_box.place(x=460, y=212)  # Coordinates for the combo box

# Tkinter IntVar variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()

# Checkbutton for "SINGLE" and "MULTI METER"
Checkbutton(window, text="SINGLE", variable=var1, font=('helvetica',12),bg='#E0FFFF').place(x=867, y=207)
Checkbutton(window, text="MULTI-METER", variable=var2, font=('helvetica',12),bg='#E0FFFF').place(x=970, y=207)

# Checkbutton for "RESIDENTIAL" and "BUSINESS"
Checkbutton(window, text="RESIDENTIAL", variable=var3, font=('helvetica',12),bg='#E0FFFF').place(x=1230, y=207)
Checkbutton(window, text="BUSINESS", variable=var4, font=('helvetica',12),bg='#E0FFFF').place(x=1380, y=207)

#label for service application details
servicetype_lbl = my_gui_design.label_design(85, 175, 'SERVICE TYPE')
servicebundle_lbl = my_gui_design.label_design(455, 170, 'SERVICE BUNDLE')
applicationtype_lbl = my_gui_design.label_design(870, 170, 'APPLICATION TYPE')
whatistheservicefor_lbl = my_gui_design.label_design(1230, 170, 'WHAT IS THE SERVICE FOR?')
appliedload_lbl = my_gui_design.label_design(1653, 170, 'APPLIED LOAD (kW)')

#Textbox for service application details
appliedloadtxt = my_gui_design.textbox_design1(1655, 212)

# Create a frame for Customer Details
title_frame = tk.Frame(window, bg="white", height=1)  # Adjust height as needed
title_frame.place(x=0, y=281, anchor="w", relwidth=1)  # Use side="bottom" to anchor it at the bottom

# Create a label for Customer Details
title_label = tk.Label(title_frame, text="CUSTOMER DETAILS", fg="black",bg="white", font=("Helvetica", 16, "bold"))
title_label.pack(side="left", padx=35, pady=5)  # Add padding to center the text vertically

#Check button for "CUSTOMER" and "REPRESENTATIVE"
Checkbutton(window, text="CUSTOMER", variable=var5, font=('helvetica',12),bg='#E0FFFF').place(x=85, y=355)
Checkbutton(window, text="REPRESENTATIVE", variable=var6, font=('helvetica',12),bg='#E0FFFF').place(x=230, y=355)

# Creating a combo box for suffix
options = ["II", "III", "IV", "V", "Jr.", "Sr."]
combo_box = ttk.Combobox(window, values=options, font=('Helvetica', 12), width=15)  # Adjusted width
combo_box.place(x=1425, y=358)  # Coordinates for the combo box

# Creating a combo box for gender
options = ["MAN", "WOMAN", "LGBTQ+", "PREFER NOT TO STATE"]
combo_box = ttk.Combobox(window, values=options, font=('Helvetica', 12), width=15)  # Adjusted width
combo_box.place(x=1655, y=360)  # Coordinates for the combo box

# creating a label for customer details
appliyingas_lbl = my_gui_design.label_design(85, 325, 'I AM APPLYING AS*')
firstname_lbl = my_gui_design.label_design(470,325, 'FIRST NAME')
middlename_lbl = my_gui_design.label_design(787,325, 'MIDDLE NAME')
lastname_lbl = my_gui_design.label_design(1100, 325, 'LAST NAME')
suffix_lbl = my_gui_design.label_design(1422, 325, 'SUFFIX')
gender_lbl = my_gui_design.label_design(1652, 325, 'GENDER')
dateofbirth_lbl = my_gui_design.label_design(85, 420, 'DATE OF BIRTH')
landlinenum_lbl = my_gui_design.label_design(420, 420, 'LANDLINE NUMBER')
phonenumber_lbl = my_gui_design.label_design(750, 420, 'PHONE NUMBER')
emailaddress_lbl = my_gui_design.label_design(1100, 420,'EMAIL ADDRESS')
preferrednotificationchannel_lbl = my_gui_design.label_design(1505, 420, 'PREFERRED NOTIFICATION CHANNEL')

#creating a text box for customer details
firstnametxt = my_gui_design.textbox_design2(473, 360)
middlenametxt = my_gui_design.textbox_design2(790,360)
lastnametxt = my_gui_design.textbox_design2(1103, 360)

# creating a divider
title_frame = tk.Frame(window, bg="#ffcfb1", height=2)  # Adjust height as needed
title_frame.place(x=0, y=400, anchor="w", relwidth=1)

# creating a clearable text box1 for date of birth
text_box1 = Entry(window, width=20, font=("Helvetica", 12), fg="gray")
text_box1.place(x=85, y=455)
text_box1.insert(0, "MM/DD/YYYY")
text_box1.config(fg="black")

# Bind clear_text functionality directly to the button click event
text_box1.bind("<Button-1>", lambda event: text_box1.delete(0, END))

# creating a clearable text box2 for primary mobile
text_box1 = Entry(window, width=20, font=("Helvetica", 12), fg="black")
text_box1.place(x=420, y=455)
text_box1.insert(0, "XXXX - XXXX")

# Bind clear_text functionality directly to the button click event
text_box1.bind("<Button-1>", lambda event: text_box1.delete(0, END))

# creating a clearable text box3 for phone number
text_box1 = Entry(window, width=20, font=("Helvetica", 12), fg="black")
text_box1.place(x=753, y=455)
text_box1.insert(0, "+63 XXXXXXXXXX")

# Bind clear_text functionality directly to the button click event
text_box1.bind("<Button-1>", lambda event: text_box1.delete(0, END))

# creating a clearable text box4 for email
text_box1 = Entry(window, width=30, font=("Helvetica", 12), fg="black")
text_box1.place(x=1103, y=455)
text_box1.insert(0, "email.@mail.com")

# Bind clear_text functionality directly to the button click event
text_box1.bind("<Button-1>", lambda event: text_box1.delete(0, END))

# Create a StringVar to hold the selected radiobutton value
selected_option = StringVar(value="Option 1")

# Create radiobuttons with customization
radiobutton1 = Radiobutton(window, text="BOTH", variable=selected_option, value="Option 1",
            fg="black", bg="#E0FFFF", font=("Helvetica", 12))
radiobutton1.place(x=1500, y=455)

radiobutton2 = Radiobutton(window, text="SMS", variable=selected_option, value="Option 2",
                         fg="black", bg="#E0FFFF", font=("Helvetica", 12))
radiobutton2.place(x=1630, y=455)  # Position radiobutton2

radiobutton3 = Radiobutton(window, text="EMAIL", variable=selected_option, value="Option 3",
                         fg="black", bg="#E0FFFF", font=("Helvetica", 12))
radiobutton3.place(x=1745, y=455)  # Position radiobutton2


# Create a frame for Customer Details
title_frame = tk.Frame(window, bg="white", height=1)  # Adjust height as needed
title_frame.place(x=0, y=524, anchor="w", relwidth=1)  # Use side="bottom" to anchor it at the bottom

# Create a label for Customer Details
title_label = tk.Label(title_frame, text="SERVICE ADDRESS", fg="black",bg="white", font=("Helvetica", 16, "bold"))
title_label.pack(side="left", padx=35, pady=5)  # Add padding to center the text vertically

# creating a label for service address
province_lbl = my_gui_design.label_design(85, 565, 'PROVINCE')
city_municipality_lbl = my_gui_design.label_design(565, 565, 'CITY/MUNICIPALITY')
barangay_lbl = my_gui_design.label_design(1103, 565, 'BARANGAY')
street_lbl = my_gui_design.label_design(1607, 565, 'STREET')
fulladdress = my_gui_design.label_design(85, 665, 'HOUSE/BLDG. NO., STREET, SUBDIVISION')
landmark = my_gui_design.label_design(1147, 665, 'LANDMARK')

# creating a text box for service address
pronvicetxt = my_gui_design.textbox_design2(88, 600)
city_municipalitytxt = my_gui_design.textbox_design2(568, 600)
barangaytxt = my_gui_design.textbox_design2(1100, 600)
streettxt = my_gui_design.textbox_design2(1610, 600)
fulladdresstxt = my_gui_design.textbox_design3(87, 700)
landmarktxt = my_gui_design.textbox_design4(1150, 700)

# creating a divider
title_frame = tk.Frame(window, bg="#ffcfb1", height=2)  # Adjust height as needed
title_frame.place(x=0, y=645, anchor="w", relwidth=1)

# creating a frame footer
title_frame = tk.Frame(window, bg="black", height=300)  # Adjust height as needed
title_frame.place(x=0, y=930, anchor="w", relwidth=1)

#FOOTER
# Meralco logo footer
image3_path = r"C:\Users\Worldtech Computer\PycharmProjects\PLDL01E\PLDL01E_THEA\bnw_meralco.jpg"  # Replace with your actual path
image3 = Image.open(image3_path).convert("RGB")  # Convert to a supported format (if needed)
image3 = image3.resize((150, 100))  # Adjust size as needed
photo_image3 = ImageTk.PhotoImage(image3)

# Create a label for the second image (using coordinates)
second_image_label = Label(image=photo_image3, bg='black')
second_image_label.place(x=1585, y=850)  # Adjust coordinates as needed

# Creating a label
aboutmeralco = my_gui_design.label_design3(400, 800, 'ABOUT MERALCO')
explore = my_gui_design.label_design3(650, 800, 'EXPLORE ABOUT MERALCO')
news_advisories = my_gui_design.label_design3(975, 800, 'NEWS & ADVISORIES')

# initializing Label text for ABOUT MERALCO
profile_text = "Profile"
governance_text = "Governance"
disclosure_text = "Disclosure"
investor_relations_text = "Investor Relations"
careers_text = "Careers"
advocacies_text = "Advocacies"
competitive_selection_text = "Competitive Selection"  # Combine last two lines
process_text = "Process"

# Profile label
profile_label = Label(window, text=profile_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
profile_label.place(x=400, y=845)
profile_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
profile_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# governance label
governance_label = Label(window, text=governance_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
governance_label.place(x=400, y=870)
governance_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
governance_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# disclosure label
disclosure_label = Label(window, text=disclosure_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
disclosure_label.place(x=400, y=895)
disclosure_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
disclosure_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# investor label
investor_relations_label = Label(window, text=investor_relations_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
investor_relations_label.place(x=400, y=920)
investor_relations_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
investor_relations_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# careers label
careers_label = Label(window, text=careers_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
careers_label.place(x=400, y=945)
careers_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
careers_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# advocacies label
advocacies_label = Label(window, text=advocacies_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
advocacies_label.place(x=400, y=970)
advocacies_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
advocacies_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# competitive selection label
competitive_selection_label = Label(window, text=competitive_selection_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
competitive_selection_label.place(x=400, y=995)
competitive_selection_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
competitive_selection_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# process label
process_label = Label(window, text=process_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
process_label.place(x=400, y=1020)
process_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
process_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# initializing label text for EXPLORE ABOUT MERALCO
forhomes_text = "For Homes"
forbriz_text = "For Biz"
forenterprise_text = "For Enterprise"

# forhomes label
forhomes_label = Label(window, text=forhomes_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
forhomes_label.place(x=650, y=845)
forhomes_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
forhomes_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# forbiz label
forbriz_label = Label(window, text=forbriz_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
forbriz_label.place(x=650, y=870)
forbriz_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
forbriz_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# forenterprise label
forenterprise_label = Label(window, text=forenterprise_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
forenterprise_label.place(x=650, y=895)
forenterprise_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
forenterprise_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# initializing label text for NEWS & ADVISORIES
maintenance_schedule_text = "Maintenance Schedule"
meter_deposit_refund_text = "Meter Deposit Refund"
rates_archive_text = "Rates Archives"
latest_news_press_release_text = "Latest News & Press Releases"
safety_tips_text = "Safety Tips"

# maintenance schedule label
maintenance_schedule_label = Label(window, text=maintenance_schedule_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
maintenance_schedule_label.place(x=975, y=845)
maintenance_schedule_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
maintenance_schedule_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# meter deposit refund label
meter_deposit_refund_label = Label(window, text=meter_deposit_refund_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
meter_deposit_refund_label.place(x=975, y=870)
meter_deposit_refund_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
meter_deposit_refund_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# rates archive label
rates_archive_label = Label(window, text=rates_archive_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
rates_archive_label.place(x=975, y=895)
rates_archive_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
rates_archive_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# latest news release label
latest_news_press_release_label = Label(window, text=latest_news_press_release_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
latest_news_press_release_label.place(x=975, y=920)
latest_news_press_release_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
latest_news_press_release_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# safety tips label
safety_tips_label = Label(window, text=safety_tips_text, fg="white", bg="black", font=('Arial', 13))  # Keep white text
safety_tips_label.place(x=975, y=945)
safety_tips_label.bind("<Enter>", lambda event: event.widget.config(fg="#00A3A3"))  # Change to blue
safety_tips_label.bind("<Leave>", lambda event: event.widget.config(fg="white"))  # Change back to white

# creating a label for copyright meralco
copyright_lbl = my_gui_design.label_design3(1495, 990, '© Meralco 2024   Privacy   Help & Support')

#call for the button and place under the image
uploadbutton = my_gui_design.button_design(1700, 723)

window.mainloop()
