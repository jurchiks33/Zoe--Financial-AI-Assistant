#ai_trading_bot.py

import tkinter as tk
from tkinter import ttk
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Function for stock data plotting
def plot_stock_data(symbol, container):
    stock_data = yf.download(symbol, period = "1y")
    fig, ax = plt.subplots()
    ax.plot(stock_data['Close'], label='Close Price')
    ax.set_title(f'{symbol} Closing Prices')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=container)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='both')

# trading strategies
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
    # clear previous content
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    #create background frame
    frame = tk.Frame(content_frame, bg='#1a1a1a')
    frame.pack(fill='both', expand=True)

    # Manual positioning of frames
    frame1 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame2 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame3 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame4 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame5 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame6 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame7 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame8 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame9 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame10 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame11 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')

    # placing frames on a page

    
