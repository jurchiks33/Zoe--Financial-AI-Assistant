import tkinter as tk

def create_frame10(parent):
    frame10 = tk.Frame(parent, bg='#333333', bd=2, relief='solid')
    frame10.place(relx=0.855, rely=0.49, relwidth=0.125, relheight=0.2)

    # frame logic coming below
    label10 = tk.Label(frame10, text="Frame10", bg='#333333', fg='white')
    label10.pack(expand=True)

    return frame10