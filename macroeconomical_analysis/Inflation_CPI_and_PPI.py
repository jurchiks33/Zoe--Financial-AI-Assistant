import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch CPI and PPI data from FRED
def get_inflation_data(start, end):
    cpi_data = web.DataReader('CPIAUCSL', 'fred', start, end) 
    ppi_data = web.DataReader('PPIACO', 'fred', start, end)  
    return cpi_data, ppi_data

# Function to analyze and plot CPI and PPI data
def analyze_inflation():
    # Define the time range for data retrieval
    start_date = '2000-01-01'
    end_date = pd.to_datetime('today').strftime('%Y-%m-%d') 
    
    # Fetch CPI and PPI data
    cpi_data, ppi_data = get_inflation_data(start_date, end_date)

    # Plot CPI and PPI data on the same chart
    plt.figure(figsize=(10, 6))

    plt.plot(cpi_data, label='CPI (Consumer Price Index)', color='blue')
    plt.plot(ppi_data, label='PPI (Producer Price Index)', color='green')

    plt.title('CPI vs PPI')
    plt.xlabel('Date')
    plt.ylabel('Index Value')
    plt.legend(loc='best')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# Main function script
def main():
    analyze_inflation()

# standalone script
if __name__ == "__main__":
    main()
