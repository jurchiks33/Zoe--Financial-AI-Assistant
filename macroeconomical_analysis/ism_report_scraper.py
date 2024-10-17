import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# Helper function to convert text to float if possible
def convert_to_float(text):
    try:
        return float(text)
    except ValueError:
        return None  # Return None if the conversion fails

# Function to scrape ISM report from the specific September page
def scrape_ism_report():
    url = "https://www.ismworld.org/supply-management-news-and-reports/reports/ism-report-on-business/pmi/september/"
    
    # Send a request to fetch the page content
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve ISM report. Status code: {response.status_code}")
        return None
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Hardcode the 'Index' column names 
    index_names = [
        "Manufacturing PMI®", "New Orders", 
        "Production", "Employment", 
        "Supplier Deliveries",
        "Inventories", "Customers' Inventories", 
        "Prices", "Backlog of Orders", 
        "New Export Orders", "Imports"
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
    
    for i, row in enumerate(rows[1:]):
        cols = row.find_all('td')
        
        # Only extract the first two data columns (September and August data)
        sep_value = convert_to_float(cols[0].get_text(strip=True))  # First data column (September)
        aug_value = convert_to_float(cols[1].get_text(strip=True))  # Second data column (August)
        
        # Append values only if they are numeric (skip non-numeric)
        if sep_value is not None and aug_value is not None:
            data['Series Index Sep'].append(sep_value)  # September data into Series Index Sep
            data['Series Index Aug'].append(aug_value)  # August data into Series Index Aug
    
    return pd.DataFrame(data)

# Function to display the table
def display_ism_report(df):
    # Plotting the table
    fig, ax = plt.subplots(figsize=(10, 6))  # Set the figure size

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
    plt.title('ISM Report - Business Growth (September)', 
              fontsize=14, 
              fontweight='bold')
    plt.tight_layout()
    plt.show()

# Main function to run the scraper and display the data
def main():
    # Scrape the ISM report data
    df = scrape_ism_report()
    
    if df is not None:
        # Display the data as a table
        display_ism_report(df)

# Run the main function
if __name__ == "__main__":
    main()
