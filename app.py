import ttkbootstrap as ttkb
from ttkbootstrap.constants import *
from ttkbootstrap import Button, Label, Frame, Style
from ttkbootstrap.dialogs import Messagebox

def login():
    Messagebox.show_info("Login", "Login function called")

def sign_up():
    Messagebox.show_info("Sign Up", "Sign-up function called")

def find_match():
    Messagebox.show_info("Find a Match", "Find a match function called")

def exit_program():
    root.destroy()

def toggle_theme():
    current_theme = style.theme.name
    if current_theme == "darkly":
        style.theme_use("cosmo")
        theme_button.config(text="🌙 Dark Mode")
    else:
        style.theme_use("darkly")
        theme_button.config(text="☀️ Light Mode")

def main_menu():
    global root, style, theme_button
    root = ttkb.Window(themename="darkly")
    root.title("Friend Matcher")
    root.geometry("500x400")

    style = Style()
    
    # Main Frame
    main_frame = Frame(root)
    main_frame.pack(expand=True, fill='both')

    # Top spacer
    Frame(main_frame).pack(expand=True)

    # Center Frame for title and buttons
    center_frame = Frame(main_frame)
    center_frame.pack()

    # Title Label
    title_label = Label(center_frame, text="Welcome to GINGER", font=('Helvetica', 24, 'bold'))
    title_label.pack(pady=(0, 20))

    # Buttons
    login_button = Button(center_frame, text="Login to existing ID", command=login, width=25)
    sign_up_button = Button(center_frame, text="Sign Up", command=sign_up, width=25)
    find_match_button = Button(center_frame, text="Find a Match", command=find_match, width=25)
    exit_button = Button(center_frame, text="Exit", command=exit_program, bootstyle="danger-outline", width=25)

    # Position buttons
    login_button.pack(pady=5)
    sign_up_button.pack(pady=5)
    find_match_button.pack(pady=5)
    exit_button.pack(pady=5)

    # Bottom spacer
    Frame(main_frame).pack(expand=True)

    # Theme toggle button
    theme_button = Button(main_frame, text="☀️ Light Mode", command=toggle_theme, bootstyle="info-outline", width=15)
    theme_button.pack(side="bottom", pady=10)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main_menu()
