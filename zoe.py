# zoe.py

import tkinter as tk
from tkinter import ttk
import ai_trading_bot
import sentiment_analysis
import portfolio_optimization
import fraud_detection
import personal_finance_advisor


# Function for the main application window.
def create_app():
    root = tk.Tk()
    root.title("Zoe, Financial AI Assistant")

    # Background color
    root.configure(bg='#1a1a1a')

    # Set the window screen size 70%
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width * 0.7)
    height = int(screen_height * 0.7)

    # Center window on the screen
    x_offset = int((screen_width - width) / 2)
    y_offset = int((screen_height - height) / 2)

    # Set the initial size and position of the window
    root.geometry(f'{width} x {height} + {x_offset} + {y_offset}')

    # Create a navigation bar.
    nav_bar = ttk.Frame(root, padding="10")
    nav_bar.pack(side="top", fill="x")

    # Create content frame to switch between pages
    content_frame = tk.Frame(root, bg='#1a1a1a')
    content_frame.pack(fill='both', expand=True)

    



    return root
    