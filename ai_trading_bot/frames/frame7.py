import tkinter as tk

def create_frame7(parent):
    frame7 = tk.Frame(parent, bg='#333333', bd=2, relief='solid')
    frame7.place(relx=0.71, rely=0.05, relwidth=0.06, relheight=0.43)  # Long vertical right

    # frame logic is coming below
    label7 = tk.Label(frame7, text="Frame7", bg='#333333', fg='white')
    label7.pack(expand=True)

    return frame7