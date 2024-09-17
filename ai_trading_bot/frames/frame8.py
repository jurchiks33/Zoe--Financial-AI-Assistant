import tkinter as tk

def create_frame8(parent):
    frame8 = tk.Frame(parent, bg='#333333', bd=2, relief='solid')
    frame8.place(relx=0.15, rely=0.49, relwidth=0.7, relheight=0.2)

    # frame logic coming below
    label8 = tk.Label(frame8, text="Frame8", bg='#333333', fg='white')
    label8.pack(expand=True)

    return frame8
