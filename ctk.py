import customtkinter as ctk
from auth import register_user, login_user, log_activity

# Function to handle user registration
def handle_register():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    success, message = register_user(first_name, last_name, email, password, confirm_password)
    label_message.configure(text=message)

# Function to handle user login
def handle_login():
    email = entry_login_email.get()
    password = entry_login_password.get()

    success, message = login_user(email, password)
    label_login_message.configure(text=message)
    if success:
        log_activity(f"User logged in: {email}")
        # Continue with the rest of your application logic after successful login

# Function to switch frames
def show_frame(frame):
    frame.tkraise()

# Create main application window
app = ctk.CTk()
app.title("Banking App")
app.geometry("400x600")

# Define frames
frame_login = ctk.CTkFrame(app)
frame_register = ctk.CTkFrame(app)

for frame in (frame_login, frame_register):
    frame.grid(row=0, column=0, sticky='nsew')

# Login Frame
label_login = ctk.CTkLabel(frame_login, text="Login", font=("Arial", 20))
label_login.pack(pady=10)

entry_login_email = ctk.CTkEntry(frame_login, placeholder_text="Email")
entry_login_email.pack(pady=5)

entry_login_password = ctk.CTkEntry(frame_login, placeholder_text="Password", show="*")
entry_login_password.pack(pady=5)

button_login = ctk.CTkButton(frame_login, text="Login", command=handle_login)
button_login.pack(pady=10)

label_login_message = ctk.CTkLabel(frame_login, text="")
label_login_message.pack(pady=5)

button_to_register = ctk.CTkButton(frame_login, text="Go to Register", command=lambda: show_frame(frame_register))
button_to_register.pack(pady=5)

# Register Frame
label_register = ctk.CTkLabel(frame_register, text="Register", font=("Arial", 20))
label_register.pack(pady=10)

entry_first_name = ctk.CTkEntry(frame_register, placeholder_text="First Name")
entry_first_name.pack(pady=5)

entry_last_name = ctk.CTkEntry(frame_register, placeholder_text="Last Name")
entry_last_name.pack(pady=5)

entry_email = ctk.CTkEntry(frame_register, placeholder_text="Email")
entry_email.pack(pady=5)

entry_password = ctk.CTkEntry(frame_register, placeholder_text="Password", show="*")
entry_password.pack(pady=5)

entry_confirm_password = ctk.CTkEntry(frame_register, placeholder_text="Confirm Password", show="*")
entry_confirm_password.pack(pady=5)

button_register = ctk.CTkButton(frame_register, text="Register", command=handle_register)
button_register.pack(pady=10)

label_message = ctk.CTkLabel(frame_register, text="")
label_message.pack(pady=5)

button_to_login = ctk.CTkButton(frame_register, text="Go to Login", command=lambda: show_frame(frame_login))
button_to_login.pack(pady=5)

# Initialize with login frame
show_frame(frame_login)

# Start the main application loop
app.mainloop()
