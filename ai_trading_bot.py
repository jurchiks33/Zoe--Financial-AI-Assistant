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

    # Manual positioning of frames
    frame1 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame2 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame3 = tk.Frame(frame, bg='#1a1a1a', bd=2, relief='solid')
    frame4 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame5 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame6 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame7 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame8 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame9 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame10 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')
    frame11 = tk.Frame(frame, bg='#333333', bd=2, relief='solid')

    # Place frames in a layout
    frame1.place(relx=0.02, rely=0.05, relwidth=0.2, relheight=0.2)
    frame2.place(relx=0.02, rely=0.28, relwidth=0.2, relheight=0.2)
    frame3.place(relx=0.3, rely=0.05, relwidth=0.4, relheight=0.43)
    frame4.place(relx=0.78, rely=0.05, relwidth=0.2, relheight=0.2)
    frame5.place(relx=0.78, rely=0.28, relwidth=0.2, relheight=0.2)
    frame6.place(relx=0.228, rely=0.05, relwidth=0.06, relheight=0.43)  # Long vertical left
    frame7.place(relx=0.71, rely=0.05, relwidth=0.06, relheight=0.43)  # Long vertical right
    frame8.place(relx=0.15, rely=0.49, relwidth=0.7, relheight=0.20)
    frame9.place(relx=0.02, rely=0.49, relwidth=0.125, relheight=0.20)
    frame10.place(relx=0.855, rely=0.49, relwidth=0.125, relheight=0.20)
    frame11.place(relx=0.02, rely=0.70, relwidth=0.96, relheight=0.26)

    # Labels to place text inside the frames (for now to identify correct frame)
    label1 = tk.Label(frame1, text="Frame1", bg='#333333', fg='white')
    label1.pack(expand=True)
    label2 = tk.Label(frame2, text="Frame2", bg='#333333', fg='white')
    label2.pack(expand=True)
    label3 = tk.Label(frame3, text="Frame3", bg='#333333', fg='white')
    label3.pack(expand=True)
    label4 = tk.Label(frame4, text="Frame4", bg='#333333', fg='white')
    label4.pack(expand=True)
    label5 = tk.Label(frame5, text="Frame5", bg='#333333', fg='white')
    label5.pack(expand=True)
    label6 = tk.Label(frame6, text="Frame6", bg='#333333', fg='white')
    label6.pack(expand=True)
    label7 = tk.Label(frame7, text="Frame7", bg='#333333', fg='white')
    label7.pack(expand=True)
    label8 = tk.Label(frame8, text="Frame8", bg='#333333', fg='white')
    label8.pack(expand=True)
    label9 = tk.Label(frame9, text="Frame9", bg='#333333', fg='white')
    label9.pack(expand=True)
    label10 = tk.Label(frame10, text="Frame10", bg='#333333', fg='white')
    label10.pack(expand=True)
    label11 = tk.Label(frame11, text="Frame11", bg='#333333', fg='white')
    label11.pack(expand=True)

    # Container for main content in the middle frame
    container = tk.Frame(frame3, bg='#1a1a1a')
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

# Test for page creation function
if __name__ == "__main__":
    root = tk.Tk()
    root.title("AI-Powered Trading Bot")
    root.geometry("1000x700")
    content_frame = tk.Frame(root, bg='#1a1a1a')
    content_frame.pack(fill='both', expand=True)
    create_page(content_frame)
    root.mainloop()
