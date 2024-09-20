import tkinter as tk

def create_frame6(parent):
    frame6 = tk.Frame(parent, bg='#333333', bd=2, relief='solid')
    frame6.place(relx=0.228, rely=0.15, relwidth=0.06, relheight=0.43)  # Long vertical left

    # frame logic is coming below
    label6 = tk.Label(frame6, text="Frame6", bg='#333333', fg='white')
    label6.pack(expand=True)

    return frame6

