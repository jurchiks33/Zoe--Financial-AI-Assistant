import pandas_datareader.data as web
import matplotlib.pyplot as plt
import pandas as pd

# function to get U.S. building permits from FRED
def fetch_building_permits_data():
    series_id = "PERMIT"

    # defining start and end data for our dataset
    start_date = '1980-01-01'
    end_date = pd.to_datetime('today').strftime('%Y-%m-%d')

    #getting data from FRED
    df = web.DataReader(series_id, 'fred', start_date, end_date)

    # renaming collumns
    df.columns = ['Building Permits']

    return df

# function to plot U.S Building Permits data
def plot_building_permits(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Building Permits'], 
             label='Building Permits', 
             color='blue', 
             linewidth=2)
    
    # plotting
    plt.title('U.S. Building Permits', fontsize=14)
    plt.xlabel('Date')
    plt.ylabel('Number of Permits')
    plt.grid(True)
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()

# main function for a data fetching
def main():
    df = fetch_building_permits_data()

    if df is not None:
        plot_building_permits(df)

if __name__ == "__main__":
    main()
