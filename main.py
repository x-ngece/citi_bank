import customtkinter

customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("dark-blue")

def button_callback():
    print("button pressed")

app = customtkinter.CTk()
app.title("Citi Bank App")
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="Click", command=button_callback)
button.grid(row=0, column=0, padx=20, pady=20)

app.mainloop()