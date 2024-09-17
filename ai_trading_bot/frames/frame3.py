import tkinter as tk

def create_frame3(parent):
    frame3 = tk.Frame(parent, bg='#333333', bd=2, relief='solid')
    frame3.place(relx=0.02, rely=0.7, relwidth=0.96, relheight=0.26)

    # Example content inside the frame
    label3 = tk.Label(frame3, text="Frame 3", bg='#333333', fg='white')
    label3.pack(expand=True)

    return frame3