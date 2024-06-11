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
