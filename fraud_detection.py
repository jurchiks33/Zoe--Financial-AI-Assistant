#fraud_detection.py

import tkinter as tk
from tkinter import ttk

def create_page(content_frame):
    # Create background frame
    frame = tk.Frame(content_frame, bg='yellow')
    frame.pack(fill='both', expand=True)

    # Use container frame inside to manage padding
    container = tk.Frame(frame, bg='yellow', padx=12, pady=12)
    container.pack(expand=True, fill='yellow')

    # Place label inside the container
    label = ttk.Label(container, text="Fraud Detection System", background='yellow')
    label.pack()

    return frame