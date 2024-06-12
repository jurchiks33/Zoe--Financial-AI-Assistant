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

    frame1.place(relx=0.05, rely=0.05, relwidth=0.2, relheight=0.2)
    frame2.place(relx=0.05, rely=0.28, relwidth=0.2, relheight=0.2)
    frame3.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.43)
    frame4.place(relx=0.75, rely=0.05, relwidth=0.2, relheight=0.2)
    frame5.place(relx=0.75, rely=0.28, relwidth=0.2, relheight=0.2)
    frame6.place(relx=0.26, rely=0.05, relwidth=0.03, relheight=0.43)  # Long vertical left
    frame7.place(relx=0.71, rely=0.05, relwidth=0.03, relheight=0.43)  # Long vertical right
    frame8.place(relx=0.15, rely=0.49, relwidth=0.7, relheight=0.15)
    frame9.place(relx=0.05, rely=0.49, relwidth=0.095, relheight=0.15)
    frame10.place(relx=0.855, rely=0.49, relwidth=0.095, relheight=0.15)
    frame11.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.2)

    # container for main content frame
    container = tk.Frame(frame3, bg='#1a1a1a')
    container.pack(fill='both', expand=True, padx=10, pady=10)

    # label for container
    label = ttk.Label(container, text='AI-Powered Trading Bot', background='1a1a1a', 
                      foreground='white', font=("Helvetica", 18))
    label.pack(pady=10)

    symbol_label = ttk.Label(container, text="Enter Stock Symbol:",
                             background='1a1a1a', foreground='white')
    
    symbol_label.pack(pady=5)
    symbol_entry = ttk.Entry(container)
    symbol_entry.pack(pady=5)

    def on_submit():
        symbol = symbol_entry.get().upper()
        clear_frame(container)
        plot_stock_data(symbol, container)
        simulate_trading_strategy(symbol, container)
        recreate_submit_button()
    
    def recreate_submit_button():
        submit_button = ttk.Button(container, text='Submit', command=on_submit)
        submit_button.pack(pady=5)

    recreate_submit_button()
    

def clear_frame(frame):
    for widget in frame.winfo_children():
        if isinstance(widget, FigureCanvasTkAgg):
            widget.get_tk_widget().destroy()
        else:
            widget.destroy()


