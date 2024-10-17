import yfinance as yf
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt

# Function to get S&P 500 stock market data (from Yahoo Finance)
def get_sp500_data(start, end):
    sp500_data = yf.download('^GSPC', start=start, end=end)
    return sp500_data['Adj Close']

# Function to get U.S. Building Permits data (from FRED)
def get_building_permits_data(start, end):
    permits_data = web.DataReader('PERMIT', 'fred', start, end)
    return permits_data

# Function to calculate and plot the moving averages for S&P 500 and Building Permits
def analyze_sp500_and_building_permits():
    # Define the time range
    start_date = '1980-01-01'
    end_date = pd.to_datetime('today').strftime('%Y-%m-%d')  # Set end date as today's date

    # Fetch S&P 500 and Building Permits data
    sp500_data = get_sp500_data(start_date, end_date)
    permits_data = get_building_permits_data(start_date, end_date)

    # Resample data to monthly frequency and calculate 1-month moving average
    sp500_ma = sp500_data.resample('M').last().rolling(window=1).mean()
    permits_ma = permits_data.resample('M').last().rolling(window=1).mean()

    # Calculate the average of the two curves
    avg_curve = (sp500_ma + permits_ma.squeeze()) / 2  # Squeeze to align dimensions

    # Plot S&P 500 and Building Permits Moving Averages
    plt.figure(figsize=(10, 6))

    plt.plot(sp500_ma, label='S&P 500 (1-month MA)', color='blue')
    plt.plot(permits_ma, label='Building Permits (1-month MA)', color='green')

    # Plot the average of the two curves as a red line
    plt.plot(avg_curve, label='Average (S&P 500 & Building Permits)', color='red')

    plt.title('S&P 500 and U.S. Building Permits - 1-Month Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend(loc='best')
    plt.grid(True)
    plt.tight_layout()

    # Show the plot
    plt.show()

# Main function to be called from the main application
def main():
    analyze_sp500_and_building_permits()

# If running this script standalone, execute main function
if __name__ == "__main__":
    main()
