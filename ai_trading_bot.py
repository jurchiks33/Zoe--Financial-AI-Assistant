#ai_trading_bot.py

import tkinter as tk
from tkinter import ttk
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Function for stock data plotting
def plot_stock_data(symbol, container):
    stock_data = yf.download(symbol, period="1y")
    fig, ax = plt.subplots()
    ax.plot(stock_data['close'], label='Close Price')
    ax.set_title(f'{symbol} Closing Prices')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legende()

    canvas = FigureCanvasTkAgg(fig, master=container)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='both')

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