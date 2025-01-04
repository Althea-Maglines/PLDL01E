import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk

# creating a class for login page
class LoginPage:
    # initializing
    def __init__(self):
        self.window = tk.Tk()
        self.configure_window()
        self.create_frames()
        self.add_image()  # Add the image
        self.creating_line()
        self.add_text_box()  # Add text boxes to the window
        self.add_text()
        self.add_checkbox()  # Add checkbox
        self.add_login_button()

# creating a configure window
    def configure_window(self):
        self.window.state('zoomed')  # Adjust size as needed
        self.window.title("Login Page")
        self.window.configure(bg="#3c7962")

# creating frame
    def create_frames(self):
        # Frame configurations (bg, x, y, width, height)
        frames = [
            ("#3c7962", 500, 1, 1, 1)  # frame1
        ]

        for bg, x, y, width, height in frames:
            frame = tk.Frame(self.window, bg=bg, height=height)
            frame.pack(fill=tk.BOTH, expand=True)  # Pack for better resizing

# adding image
    def add_image(self):
        """Load, resize, and place an image on the window."""
        #image green
            # Load and resize the image
        image_path = r"C:\Users\Worldtech Computer\PycharmProjects\PLDL01E\PLDL01E_THEA\green_1.jpeg"
        image = Image.open(image_path)
        image = image.resize((1300, 1500))  # Adjust size as needed
        photo = ImageTk.PhotoImage(image)

            # Create and position the image label
        image_label = tk.Label(self.window, image=photo, bg="#c7d1ce")
        image_label.photo = photo  # Prevent garbage collection
        image_label.place(x=900, y=0)  # Adjust the x, y coordinates as needed

        #Logo
            # Load and resize the image
        image_path = r"C:\Users\Worldtech Computer\PycharmProjects\PLDL01E\PLDL01E_THEA\logo_1.png"
        image1 = Image.open(image_path)
        image1 = image1.resize((100, 80))  # Adjust size as needed
        photo = ImageTk.PhotoImage(image1)

            # Create and position the image label
        image_label = tk.Label(self.window, image=photo, bg="#3c7962")
        image_label.photo = photo  # Prevent garbage collection
        image_label.place(x=390, y=200)  # Adjust the x, y coordinates as needed

# creating a line (horizontal, vertical)
    def creating_line(self):
        """Create and position divider lines."""
        line_vertical = tk.Frame(self.window, bg="#095d40", height=2220)  # Adjust height as needed
        line_vertical.place(x=900, y=1, anchor="w", width=3)  # Full width
        line_horizontal1 = tk.Frame(self.window, bg="#6baa81", height=10)  # Adjust height as needed
        line_horizontal1.place(x=0, y=5, anchor="w", relwidth=1)  # Full width
        line_horizontal2 = tk.Frame(self.window, bg="#095d40", height=100)  # Adjust height as needed
        line_horizontal2.place(x=0, y=65, anchor="w", relwidth=1)  # Full width
        line_horizontal3 = tk.Frame(self.window, bg="#6baa81", height=10)  # Adjust height as needed
        line_horizontal3.place(x=0, y=1052, anchor="w", relwidth=1)  # Full width
        line_horizontal4 = tk.Frame(self.window, bg="#095d40", height=10)  # Adjust height as needed
        line_horizontal4.place(x=0, y=1032, anchor="w", relwidth=1)  # Full width
        line_horizontal5 = tk.Frame(self.window, bg="#6baa81", height=10)  # Adjust height as needed
        line_horizontal5.place(x=0, y=125, anchor="w", relwidth=1)  # Full width

#creating a text
    def add_text(self):
        """Add text with a specific font and position."""
    # adding text for the title
        text1 = "MYLONA CORPORATED"
        font1 = ("Arial", 40, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text1, font=font1, bg="#095d40", fg='#efefef')
        label.place(x=590, y=30)  # Set the x and y coordinates for the position

    # adding text for welcome again
        text2 = "Welcome Again!"
        font2 = ("Arial", 40, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text2, font=font2, bg="#3c7962", fg='#efefef')
        label.place(x=240, y=300)  # Set the x and y coordinates for the position

    # adding text for please enter your details
        text2 = "Please enter your details"
        font2 = ("Arial", 15, "bold")  # Specify the font, size, and style
        label = tk.Label(self.window, text=text2, font=font2, bg="#3c7962", fg='#efefef')
        label.place(x=325, y=370)  # Set the x and y coordinates for the position

    # adding text for email
        text3 = "Email"
        font3 = ("Arial", 15)  # Specify the font, size, and style
        label = tk.Label(self.window, text=text3, font=font3, bg="#3c7962", fg='#efefef')
        label.place(x=225, y=465)  # Set the x and y coordinates for the position

    # adding text for password
        text3 = "Password"
        font3 = ("Arial", 15, )  # Specify the font, size, and style
        label = tk.Label(self.window, text=text3, font=font3, bg="#3c7962", fg='#efefef')
        label.place(x=225, y=600)  # Set the x and y coordinates for the position

    # adding text for forgot password
        text4 = "Forgot Password?"
        font4 = ("Arial", 15)  # Specify the font, size, and style
        label = tk.Label(self.window, text=text4, font=font4, bg="#3c7962", fg='#efefef')
        label.place(x=500, y=720)  # Set the x and y coordinates for the position

    #adding text for dont have an acccount?
        text5 = "Don't have an account?"
        font5 = ("Arial", 13)  # Specify the font, size, and style
        label = tk.Label(self.window, text=text5, font=font5, bg="#3c7962", fg='#efefef')
        label.place(x=310, y=845)  # Set the x and y coordinates for the position

    # adding text for sign up
        text6 = "Sign Up"
        font6 = ("Arial", 13, 'bold')  # Specify the font, size, and style
        label = tk.Label(self.window, text=text6, font=font6, bg="#3c7962", fg='#efefef')
        label.place(x=490, y=845)  # Set the x and y coordinates for the position

#creating a text box
    def add_text_box(self):
        """Create and position a text box (Entry widget)."""
    # adding text box for email
        text_box = ctk.CTkTextbox(self.window, width=450, height=5, corner_radius=20, border_width=3,
                                  border_color="#efefef", border_spacing=1, fg_color='#efefef', text_color='black',
                                  font=("Arial", 20))  # This is a text box from customtkinter
        text_box.place(x=220, y=500)  # Adjust the x, y coordinates as needed
        text_box.insert("0.0", "Enter your Email")  # Placeholder text

    # adding text box for password
        text_box2 = ctk.CTkTextbox(self.window, width=450, height=5, corner_radius=20, border_width=3,
                                  border_color="#efefef", border_spacing=1, fg_color='#efefef', text_color='black',
                                  font=("Arial", 20))  # This is a text box from customtkinter
        text_box2.place(x=220, y=635)  # Adjust the x, y coordinates as needed
        text_box2.insert("0.0", "Enter your Password")  # Placeholder text

# adding check box
    def add_checkbox(self):
        """Add a checkbox to the window."""
    # adding checkbox for remember me
        my_check = ctk.CTkCheckBox(self.window, border_color="#efefef", text_color='#efefef', font=("Arial", 20 ), text="Remember me")
        my_check.pack(pady=40)  # Adjust the padding as needed
        my_check.place(x=225, y=720)

# adding a button
    def add_login_button(self):
        """Create and position the login button."""
    # adding log in button
        self.login_button = ctk.CTkButton(master=self.window,text="Log In", font=("Arial", 20 ),fg_color='#095d40',
                            border_color="#efefef", height=50, width=400, corner_radius=50)
        self.login_button.place(x=250, y=775)  # Adjust x and y coordinates as needed
