#ai_trading_bot.py

import tkinter as tk
from tkinter import ttk

def create_page(content_frame):
    # Clear previous content
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Create background frame
    frame = tk.Frame(content_frame, bg='red')
    frame.pack(fill='both', expand=True)

    #Use container frame inside to manage padding
    container = tk.Frame(frame, bg='red', padx=12, pady=12)
    container.pack(expand=True, fill='both')

    # Place a label inside container
    label = ttk.Label(container, text="AI-Powered Trading Bot", background='red')
    label.pack()

    return frame