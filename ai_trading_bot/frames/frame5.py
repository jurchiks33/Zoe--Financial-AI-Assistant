import tkinter as tk

def create_frame5(parent):
    frame5 = tk.Frame(parent, bg='#333333', bd=2, relief='solid')
    frame5.place(relx=0.78, rely=0.28, relwidth=0.2, relheight=0.2)

# frame logic coming below
    label5 = tk.Label(frame5, text="Frame5", bg='#333333', fg='white')
    label5.pack(expand=True)

    return frame5
