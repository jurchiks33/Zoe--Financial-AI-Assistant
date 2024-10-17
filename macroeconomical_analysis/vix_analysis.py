import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Function to fetch VIX (Volatility Index) data
def get_vix_data(start, end):
    vix_data = yf.download('^VIX', start=start, end=end)
    return vix_data['Adj Close']

# Function to analyze and plot VIX data
def analyze_vix():
    # Define the time range for VIX data retrieval
    start_date = '2010-01-01'
    end_date = pd.to_datetime('today').strftime('%Y-%m-%d')  # Set end date as today's date

    # Retrieve the VIX data
    vix_data = get_vix_data(start_date, end_date)

    # Plotting the VIX data
    plt.figure(figsize=(10, 6))
    plt.plot(vix_data, 
             label='VIX (S&P 500 Volatility Index)', 
             color='blue')
    plt.title('S&P 500 Volatility Index (VIX)')
    plt.xlabel('Date')
    plt.ylabel('VIX Value')
    
    # Horizontal line at volatility threshold
    plt.axhline(20, 
                color='red', 
                linestyle='--', 
                label='Normal Volatility Threshold')
    
    plt.legend(loc='best')
    plt.grid(True)

    # Show the plot
    plt.tight_layout()
    plt.show()

# Main function to be called from the main application
def main():
    analyze_vix()

# If running this script standalone, execute main function
if __name__ == "__main__":
    main()
