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
    ax.plot(stock_data['Close'], label='Close Price')  
    ax.set_title(f'{symbol} Closing Prices')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=container)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='both')

# Trading strategies
def simulate_trading_strategy(symbol, container):
    stock_data = yf.download(symbol, period="1y")
    stock_data['SMA50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['SMA200'] = stock_data['Close'].rolling(window=200).mean()

    fig, ax = plt.subplots()
    ax.plot(stock_data['Close'], label='Close Price')
    ax.plot(stock_data['SMA50'], label='50-Day SMA')
    ax.plot(stock_data['SMA200'], label='200-Day SMA')
    ax.set_title(f'{symbol} Trading Strategy')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=container)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='both')

def create_page(content_frame):
    # Clear previous content
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Create background frame
    frame = tk.Frame(content_frame, bg='#1a1a1a')
    frame.pack(fill='both', expand=True)

    # Use container frame inside to manage padding
    container = tk.Frame(frame, bg='#1a1a1a', padx=12, pady=12)
    container.pack(expand=True, fill='both')

    # Place a label inside container
    label = ttk.Label(container, text="AI-Powered Trading Bot", background='#1a1a1a', 
                      foreground='white', font=("Helvetica", 18))
    label.pack(pady=10)

    symbol_label = ttk.Label(container, text="Enter Stock Symbol:", 
                             background='#1a1a1a', foreground='white')
    symbol_label.pack(pady=5)
    symbol_entry = ttk.Entry(container)
    symbol_entry.pack(pady=5)

    def on_submit():
        symbol = symbol_entry.get().upper()
        clear_frame(container)
        plot_stock_data(symbol, container)
        simulate_trading_strategy(symbol, container)
    
    submit_button = ttk.Button(container, text='Submit', command=on_submit)
    submit_button.pack(pady=5)

def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()

# Test for a page creation function
if __name__ == "__main__":
    root = tk.Tk()
    root.title("AI-Powered Trading Bot")
    root.geometry("800x600")
    content_frame = tk.Frame(root, bg='#1a1a1a')
    content_frame.pack(fill='both', expand=True)
    create_page(content_frame)
    root.mainloop()
