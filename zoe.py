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
    root.geometry(f'{width}x{height}+{x_offset}+{y_offset}')

    # Create a navigation bar.
    nav_bar = ttk.Frame(root, padding="10")
    nav_bar.pack(side="top", fill="x")

    # Create content frame to switch between pages
    content_frame = tk.Frame(root, bg='#1a1a1a')
    content_frame.pack(fill='both', expand=True)

    # Define the navigation buttons and their corresponding functions.
    nav_buttons = [
        ("AI-Powered Trading Bot", ai_trading_bot.create_page),
        ("Sentiment Analysis for Market Prediction", sentiment_analysis.create_page),
        ("Portfolio Optimization Tool", portfolio_optimization.create_page),
        ("Fraud Detection System", fraud_detection.create_page),
        ("Personal Finance Advisor", personal_finance_advisor.create_page)
    ]

    # Adding buttons to the navigation bar
    for button_text, command in nav_buttons:
        button = ttk.Button(nav_bar, text=button_text, command=lambda 
                            cmd=command: cmd(content_frame))
        button.pack(side="left", padx=5)

    return root

# Create and run application
app = create_app()
app.mainloop()
    