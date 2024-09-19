import tkinter as tk

def create_frame11(parent):
    frame11 = tk.Frame(parent, bg='#333333', bd=2, relief='solid')
    # Adjust the size and position to avoid covering other frames
    frame11.pack(relx=0.02, rely=0.7, relwidth=0.45, relheight=0.26)  # Reduce width so it doesn't overlap other frames

    label11 = tk.Label(frame11, text="Frame 11", bg='#333333', fg='white')
    label11.pack(expand=True)

    return frame11
