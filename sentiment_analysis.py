#sentiment_analysis.py

import tkinter as tk
from tkinter import ttk

def create_page(content_frame):
    # Clear previous content
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Crete background frame
    frame = tk.Frame(content_frame, bg='blue')
    frame.pack(fill='both', expand=True)

    # USe container frame inside to manage padding
    container = tk.Frame(frame, bg='blue', padx=12, pady=12)
    container.pack(expand=True, fill='both')

    # Place label inside the container
    label = ttk.Label(container, text="Sentiment Analysis for Market Predictions", background='blue')
    label.pack()

    return frame