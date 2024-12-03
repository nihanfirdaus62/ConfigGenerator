import tkinter as tk
import webbrowser

def open_facebook(event=None):
    webbrowser.open("https://www.facebook.com")

def show_custom_message():
    custom_msg = tk.Toplevel(root)
    custom_msg.title("Custom Message")
    custom_msg.geometry("300x100")
    custom_msg.resizable(False, False)

    msg = tk.Label(custom_msg, text="Click here to open Facebook", fg="blue", cursor="hand2")
    msg.pack(pady=20)

    msg.bind("<Button-1>", open_facebook)

root = tk.Tk()
root.geometry("300x200")

btn = tk.Button(root, text="Show Custom Message", command=show_custom_message)
btn.pack(pady=20)

root.mainloop()
