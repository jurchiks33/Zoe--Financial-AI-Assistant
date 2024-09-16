import tkinter as tk

def create_frame9(parent):
    frame9 = tk.Frame(parent, bg='#333333', bd=2, relief='solid')
    frame9.place(relx=0.02, rely=0.49, relwidth=0.125, relheight=0.2)

    # frame logic coming below
    label9 = tk.Label(frame9, text="Frame9", bg='#333333', fg='white')
    label9.pack(expand=True)

    return frame9
