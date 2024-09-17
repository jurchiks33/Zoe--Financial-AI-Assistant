import tkinter as tk

def create_frame2(parent):
    frame2 = tk.Frame(parent, bg='#333333', bd=2, relief='solid')
    frame2.place(relx=0.02, rely=0.7, relwidth=0.96, relheight=0.26)

    # frame logic coming below
    label2 = tk.Label(frame2, text="Frame2", bg='#333333', fg='white')
    label2.pack(expand=True) 

    return frame2