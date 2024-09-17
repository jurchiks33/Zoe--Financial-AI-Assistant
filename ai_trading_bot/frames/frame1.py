import tkinter as tk

def create_frame1(parent):
    frame1 = tk.Frame(parent, bg='#333333', bd=2, relief='solid')
    frame1.place(relx=0.02, rely=0.7, relwidth=0.96, relheight=0.26)

    # frame logic coming below
    label1 = tk.Label(frame1, text="Frame1", bg='#333333', fg='white')
    label1.pack(expand=True) 

    return frame1