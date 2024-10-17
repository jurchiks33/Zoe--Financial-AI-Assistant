import pandas_datareader.data as web
import pandas as pd
import matplotlib.pyplot as plt

# Function to fetch 10-year and 2-year US Treasury yields from FRED
def get_yield_data(start, end):
    dgs10 = web.DataReader('DGS10', 'fred', start, end)
    dgs2 = web.DataReader('DGS2', 'fred', start, end)
    return dgs10, dgs2

# Function to analyze and plot the US Treasury yield curve spread
def analyze_yield_curve():
    # Define the time range for data retrieval
    start_date = '2000-01-01'
    end_date = pd.to_datetime('today').strftime('%Y-%m-%d')  # Set end date as today's date


    # Get 10-year and 2-year yield data
    dgs10, dgs2 = get_yield_data(start_date, end_date)

    # Merge the data into a single DataFrame
    data = pd.merge(dgs10, 
                    dgs2, 
                    left_index=True, 
                    right_index=True, 
                    how='inner')
    data.columns = ['10_Year', '2_Year']

    # Calculate the yield curve spread (10-year - 2-year)
    data['Yield_Spread'] = data['10_Year'] - data['2_Year']

    # Plotting the yield curve spread
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, 
             data['Yield_Spread'], 
             label='10-Year Minus 2-Year Yield Curve Spread', 
             color='blue')
    plt.axhline(0, 
                color='red', 
                linestyle='--', 
                label='Inversion Threshold (Zero)')
    plt.title('US Treasury 10-Year vs 2-Year Yield Curve Spread')
    plt.xlabel('Date')
    plt.ylabel('Yield Spread (%)')
    plt.legend(loc='best')
    plt.grid(True)
    
    # Show the plot
    plt.tight_layout()
    plt.show()

# Main function to be called from the main application
def main():
    analyze_yield_curve()

# If running this script standalone, execute main function
if __name__ == "__main__":
    main()
