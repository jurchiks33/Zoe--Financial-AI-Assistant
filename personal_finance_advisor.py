#personal_finance_advisor.py

import tkinter as tk
from tkinter import ttk

def create_page(content_frame):
    # Create background frame
    frame = tk.Frame(content_frame, bg='purple')
    frame.pack(fill='both', expand=True)

    # Use container frame inside to manage padding  
    container = tk.Frame(frame, bg='purple', padx=12, pady=12)
    container.pack(expand=True, fill='both')

    # Place label inside the container
    label = ttk.Label(container, text='Personal Finance Advisor', background='purple')
    label.pack()

    return frame