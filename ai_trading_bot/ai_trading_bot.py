#ai_trading_bot.py

import tkinter as tk
from tkinter import ttk
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# importing frames from the frame folder
from frames.frame1 import create_frame1
from frames.frame2 import create_frame2
from frames.frame3 import create_frame3
from frames.frame4 import create_frame4
from frames.frame5 import create_frame5
from frames.frame6 import create_frame6
from frames.frame7 import create_frame7
from frames.frame8 import create_frame8
from frames.frame9 import create_frame9
from frames.frame10 import create_frame10
from frames.frame11 import create_frame11

current_interval = '1d'  # Default time frame
symbol_entry = None  # Placeholder for symbol entry widget

# Function for stock data plotting with time frame selection
def plot_stock_data(symbol, container, interval='1d'):
    period = '1y'
    if interval == '1m':
        period = '1d'
    elif interval == '2m':
        period = '2d'
    elif interval == '3m':
        period = '3d'
    elif interval == '5m':
        period = '5d'
    elif interval == '15m':
        period = '30d'
    elif interval == '60m':
        period = '50d'
    elif interval == '4h':
        interval = '1h'
        period = '1y'

    stock_data = yf.download(symbol, period=period, interval=interval)
    fig, ax = plt.subplots()
    ax.plot(stock_data['Close'], label='Close Price')
    ax.set_title(f'{symbol} Closing Prices ({interval})')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=container)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='both')

# Trading strategies
def simulate_trading_strategy(symbol, container, interval='1d'):
    period = '1y'
    if interval == '1m':
        period = '1d'
    elif interval == '2m':
        period = '2d'
    elif interval == '3m':
        period = '3d'
    elif interval == '5m':
        period = '5d'
    elif interval == '15m':
        period = '30d'
    elif interval == '60m':
        period = '50d'
    elif interval == '4h':
        interval = '1h'
        period = '1y'

    stock_data = yf.download(symbol, period=period, interval=interval)
    stock_data['SMA50'] = stock_data['Close'].rolling(window=50).mean()
    stock_data['SMA200'] = stock_data['Close'].rolling(window=200).mean()

    fig, ax = plt.subplots()
    ax.plot(stock_data['Close'], label='Close Price')
    ax.plot(stock_data['SMA50'], label='50-Day SMA')
    ax.plot(stock_data['SMA200'], label='200-Day SMA')
    ax.set_title(f'{symbol} Trading Strategy ({interval})')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=container)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill='both')

def create_page(content_frame):
    global current_interval
    global symbol_entry

    # Clear previous content
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Create background frame
    frame = tk.Frame(content_frame, bg='#1a1a1a')
    frame.pack(fill='both', expand=True)

    # frames with their respective setup functions
    create_frame1(frame)
    create_frame2(frame)
    create_frame3(frame)
    create_frame4(frame)
    create_frame5(frame)
    create_frame6(frame)
    create_frame7(frame)
    create_frame8(frame)
    create_frame9(frame)
    create_frame10(frame)
    create_frame11(frame)

    # Container for main content in the middle frame
    container = tk.Frame(frame, bg='#1a1a1a')
    container.pack(fill='both', expand=True, padx=10, pady=10)

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
        if symbol:  # Check if symbol is not empty
            clear_chart_container(container)
            plot_stock_data(symbol, container, interval=current_interval)
            simulate_trading_strategy(symbol, container, interval=current_interval)
            recreate_submit_button()

    def recreate_submit_button():
        submit_button = ttk.Button(container, text='Submit', command=on_submit)
        submit_button.pack(pady=5)

    recreate_submit_button()

    # Add time frame buttons to frame7
    time_frames = ['1m', '2m', '3m', '5m', '15m', '30m', '60m', '4h', '1d', '1wk', '1mo', '1y']

    def update_interval(new_interval):
        global current_interval
        current_interval = new_interval
        if symbol_entry.get().upper():  # Check if symbol entry is not empty
            clear_chart_container(container)
            plot_stock_data(symbol_entry.get().upper(), container, interval=current_interval)
            simulate_trading_strategy(symbol_entry.get().upper(), container, interval=current_interval)

    # Spread buttons evenly across frame7
    for i, tf in enumerate(time_frames):
        button = ttk.Button(container, text=tf, command=lambda tf=tf: update_interval(tf))
        button.place(relx=0.1, rely=i*0.08 + 0.02, relwidth=0.8, relheight=0.06)

def clear_chart_container(frame):
    for widget in frame.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()
        else:
            widget.destroy()


#----------------PROBLEMS-----------------
#Need to fix correct timeframe display, after clicking on a different timeframe.
#new updated timeframe is not displaying, something ith a linking for frame 2 and 3.
#test