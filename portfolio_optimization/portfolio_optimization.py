#portfolio_optimization.py

import tkinter as tk
from tkinter import ttk

def create_page(content_frame):
    # Clear previous content
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Crete background frame
    frame = tk.Frame(content_frame, bg='green')
    frame.pack(fill='both', expand=True)

    # Use container frame inside to manage padding
    container = tk.Frame(frame, bg='green', padx=12, pady=12)
    container.pack(expand=True, fill='both')

    # Place label inside container
    label = ttk.Label(container, text="Portfolio Optimization Tool", background='green')
    label.pack()

    return frame