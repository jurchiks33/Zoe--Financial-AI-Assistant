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

    # Set the window size and position it in the center, screen size 70%
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    width = int(screen_width * 0.7)
    height = int(screen_height * 0.7)
    


    return root
    