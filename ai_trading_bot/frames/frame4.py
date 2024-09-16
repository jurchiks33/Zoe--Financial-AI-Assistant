import tkinter as tk

def create_frame4(parent):
    frame4 = tk.Frame(parent, bg='#333333', bd=2, relief='solid')
    frame4.place(relx=0.78, rely=0.05, relwidth=0.2, relheight=0.2)

# frame logic coming below
    label4 = tk.Label(frame4, text="Frame4", bg='#333333', fg='white')
    label4.pack(expand=True)

    return frame4
