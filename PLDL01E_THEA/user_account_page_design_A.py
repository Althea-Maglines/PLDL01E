import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk

#creating class for user account page design
class UserAccountPageDesign:
    def __init__(self):
        self.window = tk.Tk()
        self.configure_window()
        self.create_frames()
        self.add_image_profile()
        self.create_header()
        self.add_text_first_line()
        self.add_textbox_first_line()
        self.add_text_second_line()
        self.add_textbox_second_line()
        self.add_text_third_line()
        self.add_textbox_third_line()
        self.create_button()

# creating configure windows
    def configure_window(self):
        # setting up the window to portrait and the background color
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Set the window height and width
        window_width = int(screen_height * 1.2)  # Set width to 80% of screen height
        window_height = 600

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2  # Center the window vertically
        self.window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
        self.window.title("Employee Registration Page Design")
        self.window.configure(bg="#1e1b1b")

# creating a frames
    def create_frames(self):
        frames = [
                ("#333333", 100, 170, 1100, 350)
            ]
        for bg, x, y, width, height in frames:
            frame = tk.Frame(self.window, bg=bg, width=width, height=height)
            frame.place(x=x, y=y)

# creating a image profile
    def add_image_profile(self):
        image_path = r"C:\Users\Worldtech Computer\PycharmProjects\PLDL01E\PLDL01E_THEA\black_profile.png"  # Replace with your actual path
        image = Image.open(image_path)
        image = image.resize((160, 150))  # Adjust size as needed
        photo_image = ImageTk.PhotoImage(image)
        first_image_label = tk.Label(self.window, image=photo_image, bg='#343434')
        first_image_label.image = photo_image  # Keep a reference to prevent garbage collection
        first_image_label.place(x=125, y=105)

# creating a header
    def create_header(self):
        # creating a frame for header
        header_frame = tk.Frame(self.window, bg='#1e1b1b')
        header_frame.pack(fill="x", pady=1)

        # creating a label for header
        title_label = tk.Label(header_frame, text="USER ACCOUNT INFORMATION", fg='#e7eaec', bg='#1e1b1b', font=("Helvetica", 25, "bold"))
        title_label.pack(padx=5, pady=30, anchor="center")

# adding a text for first line
    def add_text_first_line(self):
        """Add text with a specific font and position."""
    # adding text for first name
        text1 = "First Name"
        font1 = ("Arial", 13, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text1, font=font1, bg="#333333", fg='#e7eaec')
        label.place(x=315, y=190)  # Set the x and y coordinates for the position

    # adding text for Middle Name
        text2 = "Middle Name"
        font2 = ("Arial", 13, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text2, font=font2, bg="#333333", fg='#e7eaec')
        label.place(x=495, y=190)  # Set the x and y coordinates for the position

    # adding text for Last Name
        text3 = "Last Name"
        font3 = ("Arial", 13, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text3, font=font3, bg="#333333", fg='#e7eaec')
        label.place(x=675, y=190)  # Set the x and y coordinates for the position

    # adding text for Suffix
        text4 = "Suffix"
        font4 = ("Arial", 13, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text4, font=font4, bg="#333333", fg='#e7eaec')
        label.place(x=855, y=190)  # Set the x and y coordinates for the position

    # adding text for Department
        text5 = "Department"
        font5 = ("Arial", 13, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text5, font=font5, bg="#333333", fg='#e7eaec')
        label.place(x=1035, y=190)  # Set the x and y coordinates for the position

# adding a textbox for first line
    def add_textbox_first_line(self):
        """Create and position a text box (Entry widget)."""
    # adding text box for first name
        text_box = ctk.CTkTextbox(self.window, width=135, height=3, corner_radius=1, border_width=1,border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15), state="disabled")  # This is a text box from customtkinter
        text_box.place(x=318, y=225)  # Adjust the x, y coordinates as needed

    # adding text box for middle name
        text_box2 = ctk.CTkTextbox(self.window, width=135, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15), state="disabled")  # This is a text box from customtkinter
        text_box2.place(x=498, y=225)  # Adjust the x, y coordinates as needed

    # adding text box for last name
        text_box3 = ctk.CTkTextbox(self.window, width=135, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                   fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15), state="disabled")  # This is a text box from customtkinter
        text_box3.place(x=678, y=225)  # Adjust the x, y coordinates as needed

    # adding text box for suffix
        text_box4 = ctk.CTkTextbox(self.window, width=135, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                   fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15), state="disabled")  # This is a text box from customtkinter
        text_box4.place(x=858, y=225)  # Adjust the x, y coordinates as needed

    # adding a textbox for date of birth
        text_box5 = ctk.CTkTextbox(self.window, width=135, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='gray', font=("Arial", 15), state="disabled")  # This is a text box from customtkinter
        text_box5.place(x=1038, y=225)  # Adjust the x, y coordinates as needed

# adding a text in second line
    def add_text_second_line(self):
        """Add text with a specific font and position."""
    # adding text for Designation
        text1 = "Designation"
        font1 = ("Arial", 13, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text1, font=font1, bg="#333333", fg='#e7eaec')
        label.place(x=125, y=275)  # Set the x and y coordinates for the position

    # adding text for Username
        text2 = "Username"
        font2 = ("Arial", 13, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text2, font=font2, bg="#333333", fg='#e7eaec')
        label.place(x=500, y=275)  # Set the x and y coordinates for the position

    # adding text for Password
        text3 = "Password"
        font3 = ("Arial", 13, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text3, font=font3, bg="#333333", fg='#e7eaec')
        label.place(x=872, y=275)  # Set the x and y coordinates for the position

# adding a textbox for second line
    def add_textbox_second_line(self):
        """Create and position a text box (Entry widget)."""
    # adding text box for designation
        text_box = ctk.CTkTextbox(self.window, width=300, height=3, corner_radius=1, border_width=1,border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15), state="disabled")  # This is a text box from customtkinter
        text_box.place(x=128, y=310)  # Adjust the x, y coordinates as needed

    # adding text box for username
        text_box2 = ctk.CTkTextbox(self.window, width=300, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box2.place(x=503, y=310)  # Adjust the x, y coordinates as needed


    # adding text box for password
        text_box3 = ctk.CTkTextbox(self.window, width=300, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                   fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box3.place(x=875, y=310)  # Adjust the x, y coordinates as needed

# addding text for third line
    def add_text_third_line(self):
        """Add text with a specific font and position."""
    # adding text for Confirm Password
        text1 = "Confirm Password"
        font1 = ("Arial", 13, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text1, font=font1, bg="#333333", fg='#e7eaec')
        label.place(x=125, y=365)  # Set the x and y coordinates for the position

    # adding text for User Type
        text2 = "User Type"
        font2 = ("Arial", 13, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text2, font=font2, bg="#333333", fg='#e7eaec')
        label.place(x=415, y=365)  # Set the x and y coordinates for the position

    # adding text for User Status
        text3 = "User Status"
        font3 = ("Arial", 13, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text3, font=font3, bg="#333333", fg='#e7eaec')
        label.place(x=695, y=365)  # Set the x and y coordinates for the position

    # adding text for Employee Number
        text4 = "Employee Number"
        font4 = ("Arial", 13, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text4, font=font4, bg="#333333", fg='#e7eaec')
        label.place(x=972, y=365)  # Set the x and y coordinates for the position

# adding a textbox for third line
    def add_textbox_third_line(self):
        """Create and position a text box (Entry widget)."""
    # adding text box for Confirm Password
        text_box = ctk.CTkTextbox(self.window, width=200, height=3, corner_radius=1, border_width=1,border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box.place(x=128, y=400)  # Adjust the x, y coordinates as needed

    # adding text box for User Type
        text_box2 = ctk.CTkTextbox(self.window, width=200, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                  fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box2.place(x=415, y=400)  # Adjust the x, y coordinates as needed

    # adding text box for User Status
        text_box3 = ctk.CTkTextbox(self.window, width=200, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                   fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box3.place(x=698, y=400)  # Adjust the x, y coordinates as needed

    # adding text box for Employee Number
        text_box4 = ctk.CTkTextbox(self.window, width=200, height=3, corner_radius=1, border_width=1, border_color="light gray", border_spacing=1,
                                   fg_color='#f8fbfc', text_color='#292828', font=("Arial", 15))  # This is a text box from customtkinter
        text_box4.place(x=975, y=400)  # Adjust the x, y coordinates as needed

# adding a button
    def create_button(self):
            """Create and position the login button."""
        #adding update button
            self.update_button = ctk.CTkButton(master=self.window, text="Update", font=("Arial", 20), fg_color='black',
                                              border_color="#e7eaec", height=30, width=150, corner_radius=1)
            self.update_button.place(x=350, y=460)  # Adjust x and y coordinates as needed

        # adding delete button
            self.delete_button = ctk.CTkButton(master=self.window, text="Delete", font=("Arial", 20), fg_color='black',
                                               border_color="#e7eaec", height=30, width=150, corner_radius=1)
            self.delete_button.place(x=575, y=460)  # Adjust x and y coordinates as needed

        # adding cancel button
            self.cancel_button = ctk.CTkButton(master=self.window, text="Cancel", font=("Arial", 20), fg_color='dark gray',
                                               border_color="#e7eaec", height=30, width=150, corner_radius=1)
            self.cancel_button.place(x=800, y=460)  # Adjust x and y coordinates as needed
