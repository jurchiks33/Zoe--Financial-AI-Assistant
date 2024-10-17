import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Helper function to convert text to float if possible
def convert_to_float(text):
    try:
        return float(text)
    except ValueError:
        return np.nan  

# Function to scrape ISM report on Business - Services for September
def scrape_ism_services_report():
    url = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/services/september/"
    
    # Send a request to fetch the page content
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve ISM Services report. Status code: {response.status_code}")
        return None
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Hardcode the 'Index' column names for ISM Services
    index_names = [
        "Services PMI®", "Business Activity/Production", 
        "New Orders", "Employment", 
        "Supplier Deliveries", "Inventories", 
        "Prices", "Backlog of Orders", 
        "New Export Orders", "Imports", 
        "Inventory Sentiment", "Customers' Inventories"
    ]
    
    # Prepare a dictionary to store the extracted data
    data = {
        'Index': index_names,
        'Series Index Sep': [],  # September data
        'Series Index Aug': [],  # August data
    }
    
    # Extract the table with ISM data
    table = soup.find('table')

    # Extract the rows from the table
    rows = table.find_all('tr')

    # Start processing from the second row, shift all data up by one)
    for i in range(1, len(index_names) + 1):
        try:
            cols = rows[i].find_all('td')  # Skip the first row
            
            # Extract September and August data if available
            if len(cols) >= 2:
                sep_value = convert_to_float(cols[0].get_text(strip=True))  # September data
                aug_value = convert_to_float(cols[1].get_text(strip=True))  # August data
            else:
                sep_value = np.nan
                aug_value = np.nan
        except IndexError:
            sep_value = np.nan
            aug_value = np.nan
        
        # Append the values (including NaN to maintain equal length)
        data['Series Index Sep'].append(sep_value)
        data['Series Index Aug'].append(aug_value)

    # Shift the data up by one row and move top row to the bottom
    data['Series Index Sep'] = data['Series Index Sep'][1:] + [np.nan]
    data['Series Index Aug'] = data['Series Index Aug'][1:] + [np.nan]

    return pd.DataFrame(data)

# Function to display the table
def display_ism_services_report(df):
    # Plotting the table
    fig, ax = plt.subplots(figsize=(10, 6))

    # Hide axes
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_frame_on(False)

    # Create a table
    table = ax.table(cellText=df.values, 
                     colLabels=df.columns, 
                     cellLoc='center', 
                     loc='center')

    # Format the table
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.2) 

    # Display the table
    plt.title('ISM Report - Services Growth (September)', 
              fontsize=14, 
              fontweight='bold')
    plt.tight_layout()
    plt.show()

# Main function to run the scraper and display the data
def main():
    # Scrape the ISM Services report data
    df = scrape_ism_services_report()
    
    if df is not None:
        # Display the data as a table
        display_ism_services_report(df)

# Run the main function
if __name__ == "__main__":
    main()