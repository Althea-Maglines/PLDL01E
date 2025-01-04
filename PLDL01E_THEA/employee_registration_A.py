import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk

#creating class for employee registration
class EmployeeRegistration:
    def __init__(self):
        self.window = tk.Tk()
        self.configure_window()
        self.create_header()
        self.create_frames()
        self.add_first_frame_title()
        self.add_label_first_frame()
        self.add_image()
        self.add_button_choose_file()
        self.add_textbox_first_frame()
        self.add_combobox_first_frame()
        self.add_label_second_frame()
        self.add_textbox_second_frame()
        self.add_second_frame_title()
        self.add_second_frame_title()
        self.add_label_third_frame()
        self.add_textbox_third_frame()
        self.add_third_frame_title()
        self.add_label_fourth_frame()
        self.add_textbox_fourth_frame()
        self.add_combobox_fourth_frame()
        self.add_button_save_cancel()

# creating a configure window
    def configure_window(self):
    # setting up the window to portrait and the background color
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

    # Calculate window dimensions (e.g., 80% of screen height for width)
        window_width = int(screen_height * 1)
        window_height = screen_height
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
        self.window.title("Employee Registration Page Design")
        self.window.configure(bg="#eff4f9")

# creating the header
    def create_header(self):
        header_frame = tk.Frame(self.window, background='#eff4f9', height=100, pady=25, padx=0)  # Adjust padding as needed
        header_frame.pack(fill="x")

        header_label = tk.Label(header_frame, background='#eff4f9', text="EMPLOYEE REGISTRATION", font=("Arial", 30, "bold"),
                        foreground="#365878")
        header_label.pack(expand=True)

# creating frames
    def create_frames(self):
        # Frame configurations (bg, x, y, width, height)
        frames = [
            ("#365878", 40, 100, 1000, 40),  # title frame for employee personal information
            ("white", 40, 150, 1000, 185), #  frame for employee personal information
            ("white", 40, 345, 1000, 160), # 2nd frame for employee personal information
            ("#365878", 40, 515, 1000, 40), # title frame for contact information
            ("white", 40, 565, 1000, 160), # 3rd frame for contact information
            ("#365878", 40, 735, 1000, 40),  # title frame for address
            ("white", 40, 785, 1000, 220),  # 3rd frame for contact information
        ]

        for bg, x, y, width, height in frames:
            frame = tk.Frame(self.window, bg=bg, width=width, height=height)  # Create the frame
            frame.place(x=x, y=y)

# creating the first frame title
    def add_first_frame_title(self):
        """Add text with a specific font and position."""
    # adding text for employee personal information
        text1 = "EMPLOYEE PERSONAL INFORMATION"
        font1 = ("Arial", 15, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text1, font=font1, bg="#365878", fg='#dbe5ec')
        label.place(x=350, y=105)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

# adding image
    def add_image(self):
        """Load, resize, and place an image on the window."""
    #image profile
            # Load and resize the image
        image_path = r"C:\Users\Worldtech Computer\PycharmProjects\PLDL01E\PLDL01E_THEA\profile_pic.png"
        image = Image.open(image_path)
        image = image.resize((120, 110))  # Adjust size as needed
        photo = ImageTk.PhotoImage(image)

            # Create and position the image label
        image_label = tk.Label(self.window, image=photo, bg="#dbe5ec")
        image_label.photo = photo  # Prevent garbage collection
        image_label.place(x=80, y=170)  # Adjust the x, y coordinates as needed

# adding button (choose file)
    def add_button_choose_file(self):
        """Create and position the login button."""
    # creating button for choose file
        self.choose_file_button = ctk.CTkButton(master=self.window,text="Choose File", font=("Arial", 15 ),fg_color='#292828',
                            border_color="#365878", height=25, width=100, corner_radius=1)
        self.choose_file_button.place(x=93, y=295)  # Adjust x and y coordinates as needed

# adding label for first frame
    def add_label_first_frame(self):
        # adding text for first name
        text2 = "First Name"
        font2 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text2, font=font2, bg="white", fg='#292828')
        label.place(x=250, y=170)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

        # adding text for middle name
        text3 = "Middle Name"
        font3 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text3, font=font3, bg="white", fg='#292828')
        label.place(x=450, y=170)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

        # adding text for last name
        text4 = "Last Name"
        font4 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text4, font=font4, bg="white", fg='#292828')
        label.place(x=650, y=170)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

        # adding text for last name
        text4 = "Suffix"
        font4 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text4, font=font4, bg="white", fg='black')
        label.place(x=850, y=170)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

        # adding text for last name
        text5 = "Date of Birth"
        font5 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text5, font=font5, bg="white", fg='black')
        label.place(x=250, y=240)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

        # adding text for last name
        text6 = "Gender"
        font6 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text6, font=font6, bg="white", fg='black')
        label.place(x=450, y=240)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

        # adding text for last name
        text7 = "Nationality"
        font7 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text7, font=font7, bg="white", fg='black')
        label.place(x=650, y=240)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

        # adding text for last name
        text8 = "Civil Status"
        font8 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text8, font=font8, bg="white", fg='black')
        label.place(x=850, y=240)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

# adding text for first frame
    def add_textbox_first_frame(self):
        """Create and position a text box (Entry widget)."""
    # adding text box for first name
        text_box = ctk.CTkTextbox(self.window, width=150, height=3, corner_radius=1, border_width=1,border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box.place(x=250, y=200)  # Adjust the x, y coordinates as needed

    # adding text box for middle name
        text_box2 = ctk.CTkTextbox(self.window, width=150, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box2.place(x=450, y=200)  # Adjust the x, y coordinates as needed

    # adding text box for last name
        text_box2 = ctk.CTkTextbox(self.window, width=150, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                   fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box2.place(x=650, y=200)  # Adjust the x, y coordinates as needed

    # adding text box for suffix
        text_box3 = ctk.CTkTextbox(self.window, width=150, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                   fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box3.place(x=850, y=200)  # Adjust the x, y coordinates as needed

    # adding a textbox for date of birth
        text_box4 = ctk.CTkTextbox(self.window, width=150, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='gray', font=("Arial", 15))  # This is a text box from customtkinter
        text_box4.place(x=250, y=270)  # Adjust the x, y coordinates as needed
        text_box4.insert("0.0", "dd/mm/yyyy")  # Placeholder text

# adding combobox for first frame
    def add_combobox_first_frame(self):
    # setting an option for gender combo box
        genders = ["", "Male", "Female", "LGBTQ+", "Prefer not to state"]
    # adding a combo box
        self.gender_combo = ctk.CTkComboBox(self.window, values=genders, width=150, height=25, corner_radius=1, border_width=1, border_color="light gray",
                            fg_color="#f8fbfc", text_color="#292828", font=("Arial", 15))
        self.gender_combo.place(x=450, y=270)  # Adjust placement as needed

    # setting an option for nationality combo box
        nationalities = ["", "American", "Australian", "British", "Canadian", "Chinese", "Filipino", "German", "Ghanaian", "Indian",
                         "Indonesian", "Italian", "Japanese", "Korean", "Lebanese", "Nigerian", "Philippines", "Papua New Guinian",
                         "Saudia", "Solomon Island", "Sudanese", "Taiwanese", "Turkish", "Vietnamese", "Yemeni", "Others"]
    # adding a combo box
        self.nationality_combo = ctk.CTkComboBox(self.window, values=nationalities, width=150, height=25, corner_radius=1, border_width=1, border_color="light gray",
                                        fg_color="#f8fbfc", text_color="#292828", font=("Arial", 15))
        self.nationality_combo.place(x=650, y=270)  # Adjust placement as needed

    # setting an option for nationality combo box
        civil_status = ["", "Single", "Married", "Divorced", "Separated", "Widowed"]
    # adding a combo box
        self.civil_status_combo = ctk.CTkComboBox(self.window, values=civil_status, width=150, height=25, corner_radius=1, border_width=1, border_color="light gray",
                                    fg_color="#f8fbfc", text_color="#292828", font=("Arial", 15))
        self.civil_status_combo.place(x=850, y=270)  # Adjust placement as needed

# adding label for second frame
    def add_label_second_frame(self):
        # adding text for department
        text1 = "Department"
        font1 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text1, font=font1, bg="white", fg='#292828')
        label.place(x=80, y=360)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

        # adding text for department
        text2 = "Designation"
        font2 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text2, font=font2, bg="white", fg='#292828')
        label.place(x=540, y=360)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

        # adding text for department
        text3 = "Qualified Dep. Status"
        font3 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text3, font=font3, bg="white", fg='#292828')
        label.place(x=780, y=360)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

        text4 = "Employee Status"
        font4 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text4, font=font4, bg="white", fg='#292828')
        label.place(x=80, y=430)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

        text5 = "Pay Date"
        font5 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text5, font=font5, bg="white", fg='#292828')
        label.place(x=540, y=430)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

        text6 = "Employee Number"
        font6 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text6, font=font6, bg="white", fg='#292828')
        label.place(x=780, y=430)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

# adding textbox for second frame
    def add_textbox_second_frame(self):
        """Create and position a text box (Entry widget)."""
    # adding text box for department
        text_box = ctk.CTkTextbox(self.window, width=420, height=3, corner_radius=1, border_width=1,border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box.place(x=80, y=390)  # Adjust the x, y coordinates as needed

    # adding text box for designation
        text_box2 = ctk.CTkTextbox(self.window, width=200, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box2.place(x=540, y=390)  # Adjust the x, y coordinates as needed

    # adding text box for qualified dep. status
        text_box3 = ctk.CTkTextbox(self.window, width=220, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                   fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box3.place(x=780, y=390)  # Adjust the x, y coordinates as needed

    # adding text box for employee status
        text_box4 = ctk.CTkTextbox(self.window, width=420, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box4.place(x=80, y=460)  # Adjust the x, y coordinates as needed

    # adding text box for pay date
        text_box5 = ctk.CTkTextbox(self.window, width=200, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                   fg_color='#f8fbfc', text_color='gray', font=("Arial", 15))  # This is a text box from customtkinter
        text_box5.place(x=540, y=460)  # Adjust the x, y coordinates as needed
        text_box5.insert("0.0", "dd/mm/yyyy")

    # adding text box for employee number
        text_box6 = ctk.CTkTextbox(self.window, width=220, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                   fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box6.place(x=780, y=460)  # Adjust the x, y coordinates as needed

# adding title for second frame
    def add_second_frame_title(self):
        """Add text with a specific font and position."""
    # adding text for contact information
        text1 = "CONTACT INFORMATION"
        font1 = ("Arial", 15, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text1, font=font1, bg="#365878", fg='#dbe5ec')
        label.place(x=415, y=520)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

# adding label for third frame
    def add_label_third_frame(self):
    # adding text for contact number
        text1 = "Contact Number"
        font1 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text1, font=font1, bg="white", fg='#292828')
        label.place(x=80, y=580)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

    # adding text for email
        text2 = "Email"
        font2 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text2, font=font2, bg="white", fg='#292828')
        label.place(x=560, y=580)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

    # adding text for other (social media)
        text3 = "Other (Social Media)"
        font3 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text3, font=font3, bg="white", fg='#292828')
        label.place(x=80, y=650)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

    # adding social media account id/no.
        text4 = "Social Media Account ID/No."
        font4 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text4, font=font4, bg="white", fg='#292828')
        label.place(x=560, y=650)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

# adding textbox for third frame
    def add_textbox_third_frame(self):
        """Create and position a text box (Entry widget)."""
    # adding text box for contact no.
        text_box = ctk.CTkTextbox(self.window, width=430, height=3, corner_radius=1, border_width=1,border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box.place(x=80, y=610)  # Adjust the x, y coordinates as needed

    # adding text box for email
        text_box2 = ctk.CTkTextbox(self.window, width=435, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box2.place(x=565, y=610)  # Adjust the x, y coordinates as needed

    # adding text box for other (social media)
        text_box3 = ctk.CTkTextbox(self.window, width=430, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                   fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box3.place(x=80, y=680)  # Adjust the x, y coordinates as needed

    # adding text box for social media account id/no.
        text_box4 = ctk.CTkTextbox(self.window, width=435, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box4.place(x=565, y=680)  # Adjust the x, y coordinates as needed

# adding title for third frame
    def add_third_frame_title(self):
        """Add text with a specific font and position."""
    # adding title text for address
        text1 = "ADDRESS"
        font1 = ("Arial", 15, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text1, font=font1, bg="#365878", fg='#dbe5ec')
        label.place(x=487, y=740)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

# adding a label for fourth frame
    def add_label_fourth_frame(self):
    # adding text for address line 1
        text1 = "Address Line 1"
        font1 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text1, font=font1, bg="white", fg='#292828')
        label.place(x=80, y=800)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

    # adding text for address line 2
        text2 = "Address Line 2"
        font2 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text2, font=font2, bg="white", fg='#292828')
        label.place(x=560, y=800)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

    # adding text for city/municipality
        text3 = "City/Municipality"
        font3 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text3, font=font3, bg="white", fg='#292828')
        label.place(x=80, y=870)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

    # adding text for state/province
        text4 = "State/Province"
        font4 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text4, font=font4, bg="white", fg='#292828')
        label.place(x=320, y=870)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

    # adding text for country
        text5 = "Country"
        font5 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text5, font=font5, bg="white", fg='#292828')
        label.place(x=560, y=870)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

    # adding text for zip code
        text6 = "Zip Code"
        font6 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text6, font=font6, bg="white", fg='black')
        label.place(x=800, y=870)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

    # adding text for zip code
        text7 = "Picture Path"
        font7 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text7, font=font7, bg="white", fg='black')
        label.place(x=80, y=935)  # Use place() with anchor for centering
        # Set the x and y coordinates for the position

# adding textbox for fourth frame
    def add_textbox_fourth_frame(self):
        """Create and position a text box (Entry widget)."""
    # adding text box for address line 1
        text_box = ctk.CTkTextbox(self.window, width=430, height=3, corner_radius=1, border_width=1,border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box.place(x=80, y=830)  # Adjust the x, y coordinates as needed

    # adding text box for address line 2
        text_box2 = ctk.CTkTextbox(self.window, width=435, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box2.place(x=565, y=830)  # Adjust the x, y coordinates as needed

    # adding text box for city/municipality
        text_box2 = ctk.CTkTextbox(self.window, width=200, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box2.place(x=80, y=900)  # Adjust the x, y coordinates as needed

    # adding text box for state/province
        text_box3 = ctk.CTkTextbox(self.window, width=200, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                   fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box3.place(x=320, y=900)  # Adjust the x, y coordinates as needed

    # adding text box for zip code
        text_box4 = ctk.CTkTextbox(self.window, width=200, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box4.place(x=800, y=900)  # Adjust the x, y coordinates as needed

    # adding text box for picture path
        text_box5 = ctk.CTkTextbox(self.window, width=920, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box5.place(x=80, y=965)  # Adjust the x, y coordinates as needed

# adding combo box for fourth frame
    def add_combobox_fourth_frame(self):
    # setting an option for country combo box
        country = ["", "Philippines", "Country 2", "Country 3"]
    # adding a combo box
        self.country_combo = ctk.CTkComboBox(self.window, values=country, width=200, height=25, corner_radius=1, border_width=1, border_color="light gray",
                            fg_color="#f8fbfc", text_color="#292828", font=("Arial", 15))
        self.country_combo.place(x=560, y=900)  # Adjust placement as needed

# adding button (save) (cancel)
    def add_button_save_cancel(self):
        """Create and position the login button."""
    # creating button for save
        self.save_button = ctk.CTkButton(master=self.window,text="Save", font=("Arial", 15 ),fg_color='#365878',
                            border_color="#365878", height=30, width=100, corner_radius=1)
        self.save_button.place(x=40, y=1015)  # Adjust x and y coordinates as needed

    # creating button for cancel
        self.cancel_button = ctk.CTkButton(master=self.window, text="Cancel", font=("Arial", 15), fg_color='#91a9bb',
                                         border_color="#365878", height=30, width=100, corner_radius=1)
        self.cancel_button.place(x=150, y=1015)  # Adjust x and y coordinates as needed
