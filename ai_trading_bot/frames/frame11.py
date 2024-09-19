import tkinter as tk

def create_frame11(parent):
    frame11 = tk.Frame(parent, bg='#333333', bd=2, relief='solid')
    frame11.place(relx=0.02, rely=0.7, relwidth=0.45, relheight=0.26)  # Correctly using place()
    
    # frame logic coming below
    label11 = tk.Label(frame11, text="Frame 11", bg='#333333', fg='white')
    label11.pack(expand=True)

    return frame11

