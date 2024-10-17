import yfinance as yf
import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Function to get M2 supply data
def get_m2_data(start, end):
    m2_data = web.DataReader('M2SL', 'fred', start, end)
    return m2_data

# Function to get stock market data (S&P 500)
def get_stock_data(ticker, start, end):
    stock_data = yf.download(ticker, start=start, end=end)
    return stock_data['Adj Close']

# Function to perform M2 money supply analysis
def analyze_m2_money_supply():
    # Define the date range
    start_date = '2000-01-01'
    end_date = pd.to_datetime('today').strftime('%Y-%m-%d')  # Set end date as today's date

    # Get M2 money supply data
    m2 = get_m2_data(start_date, end_date)

    # Get S&P 500 stock market data
    sp500 = get_stock_data('^GSPC', start_date, end_date)

    # Resample M2 and S&P 500 data to a monthly frequency and merge them
    m2_monthly = m2.resample('M').last()
    sp500_monthly = sp500.resample('M').last()

    # Merge the two datasets into a single dataframe
    data = pd.merge(m2_monthly, sp500_monthly, left_index=True, right_index=True)

    # Rename columns for clarity
    data.columns = ['M2_Supply', 'S&P500']

    # Drop any NaN values
    data = data.dropna()

    # Plotting data trend visualization
    plt.figure(figsize=(10, 6))
    plt.plot(data['M2_Supply'], label='M2 Money Supply', color='blue')
    plt.twinx().plot(data['S&P500'], label='S&P500', color='green')
    plt.title('M2 Money Supply vs S&P 500')
    plt.legend(loc='upper left')
    plt.show()

    # Correlation analysis
    correlation = data['M2_Supply'].pct_change().corr(data['S&P500'].pct_change())
    print(f"Correlation between M2 Money Supply and S&P 500: {correlation:.2f}")

    # Regression analysis M2 vs S&P 500
    m2_change = data['M2_Supply'].pct_change().dropna()
    sp500_change = data['S&P500'].pct_change().dropna()

    aligned_data = pd.concat([m2_change, sp500_change], axis=1).dropna()
    slope, intercept, r_value, p_value, std_err = linregress(aligned_data['M2_Supply'], aligned_data['S&P500'])

    print(f"Linear Regression Slope: {slope}")
    print(f"R-squared: {r_value**2:.2f}")
    print(f"P-value: {p_value:.4f}")

    # Create signal if M2 increases more than 2% monthly
    data['M2_pct_change'] = data['M2_Supply'].pct_change()

    # Signal: 1 if M2 > 2%, 0 otherwise
    data['Signal'] = data['M2_pct_change'].apply(lambda x: 1 if x > 0.02 else 0)

    # Display data with signal
    print(data.tail())

# Main function to be called from the main application
def main():
    analyze_m2_money_supply()

# If running this script standalone, execute main function
if __name__ == "__main__":
    main()
