import tkinter as tk
from tkinter import ttk

def create_frame7(parent, update_interval):
    # Create the frame for time frame buttons
    frame7 = tk.Frame(parent, bg='#333333', bd=2, relief='solid')
    frame7.place(relx=0.71, rely=0.05, relwidth=0.05, relheight=0.43)  # Adjust as needed

    # Optional: Add a label for identification
    label7 = tk.Label(frame7, text="Time Frames", bg='#333333', fg='white')
    label7.pack(pady=1)  # Slight padding for label

    # Time frame buttons logic
    time_frames = ['1m', '2m', '3m', '5m', '15m', '30m', '60m', '4h', '1d', '1wk', '1mo', '1y']

    # button font
    button_font = ('Arial', 6)

    # Spread buttons vertically in the frame
    for i, tf in enumerate(time_frames):
        button = ttk.Button(frame7, text=tf, command=lambda tf=tf: update_interval(tf))
        button.pack(padx=5, pady=2, fill='x')  # Adjust padding and fill to layout buttons nicely
        button.config(style='small.TButton')
    
    # custom styling
    style = ttk.Style()
    style.configure('small.TButton', font=button_font, padding=(2, 0.1))

    return frame7
