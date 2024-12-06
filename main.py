import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk
from gui_handler import create_file, add_entry, entry, label, check_button, passwd_toggle_entry, change_pwd, create_button, toggle_alpha_omega, open_website, select_excel_file,show_author_message

global username_entry, passwd_entry, email_entry, alpha_var, omega_var
h_label = {}
h_entry = {}
h_button = {}

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    

def submit_create_file():
    create_file(username_entry, passwd_entry, email_entry, default_passwd_var, alpha_var, omega_var)

def show_excel_entry():
    for i in range(len(h_label)):
        h_label[i].grid()
        for i in range(len(h_entry)):
            h_entry[i].grid()
            for i in range(len(h_button)):
                h_button[i].grid()

def hide_excel_entry():
    for i in range(len(h_label)):
        h_label[i].grid_remove()
        for i in range(len(h_entry)):
            h_entry[i].grid_remove()
            for i in range(len(h_button)):
                h_button[i].grid_remove()

def submit_add_entry():
    add_entry(username_entry, passwd_entry, email_entry, alpha_var, omega_var, default_passwd_var)

def new_file():
    print("New File!")

root = tk.Tk()
root.title("Config Creator")
root.geometry("500x420")
root.resizable(False, False)
root.configure(bg="#add8e6")
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)
menu_bar = Menu(root)

# Load and set the icon
icon_path = resource_path("icon.png")
icon = tk.PhotoImage(file=icon_path)
root.iconphoto(False, icon)

root.config(menu=menu_bar)
option_menu = Menu(menu_bar, tearoff=0)
about_menu = Menu(menu_bar, tearoff=0)

option_menu.add_command(label="Edit default password", command=lambda: change_pwd(root))
option_menu.add_command(label="Show Excel", command=show_excel_entry)
option_menu.add_command(label="Hide Excel", command=hide_excel_entry)
option_menu.add_command(label="Excel path", command=select_excel_file)
menu_bar.add_cascade(label="Options", menu=option_menu)

about_menu.add_command(label="author", command=lambda: show_author_message(root))
menu_bar.add_cascade(label="About", menu=about_menu)

label(frame, "Select Server:", 0, 0)
alpha_var = tk.IntVar()
omega_var = tk.IntVar()
check_button(frame, "alpha", alpha_var, 1, 0, lambda: toggle_alpha_omega(alpha_var, omega_var), 0, 1, 1, 10, 10)
check_button(frame, "omega", omega_var, 1, 0, lambda: toggle_alpha_omega(omega_var, alpha_var), 0, 2, 1, 10, 10)

label(frame, "Enter your username:", 1, 0)
username_entry = entry(frame, 1, 1, 2)

label(frame, "Enter your password:", 2, 0)
passwd_entry = entry(frame, 2, 1, 2)
passwd_entry.config(state=tk.DISABLED)

h_label[0] = label(frame, "Enter your Email:", 4, 0)
h_entry[0] = email_entry = entry(frame, 4, 1, 2)

default_passwd_var = tk.IntVar(value=1)
check_button(frame, "Use default password", default_passwd_var, 1, 0, lambda: passwd_toggle_entry(passwd_entry, default_passwd_var), 3, 0, 4, sticky="we")

create_button(frame, "Create File", submit_create_file, 5, 1, bg="#4CAF50", fg="black")
h_button[0] = create_button(frame, "Excel", submit_add_entry, 6, 2, bg="#FF9800", fg="white")
create_button(frame, "Sign up", open_website, 5, 2, bg="#FF5100", fg='#000000')

root.mainloop()
