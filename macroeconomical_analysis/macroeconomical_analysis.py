# macroeconomical_analysis.py

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Import your indicator modules here
from .Benchmark_Yield_US import Benchmark_Yield_US
from .ism_report_on_business_SERVICES import ism_report_on_business_SERVICES
from .ism_report_scraper import ism_report_scraper
from .M2_Money_Supply import M2_Money_Supply
from .us_building_permits import us_building_permits
from .umsci_scrapper import umsci_scrapper
from .vix_analysis import vix_analysis
from .sp500_building_permits_ma import sp500_building_permits_ma
from .Inflation_CPI_and_PPI import Inflation_CPI_and_PPI


def create_page(content_frame):
    # Clear previous content from content_frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Create background frame for macroeconomic analysis
    frame = tk.Frame(content_frame, bg='blue')
    frame.pack(fill='both', expand=True)

    # Use container frame inside to manage padding
    container = tk.Frame(frame, bg='blue', padx=12, pady=12)
    container.pack(expand=True, fill='both')

    # Label for "Macroeconomical Analysis"
    label = ttk.Label(container, text="Macroeconomical Analysis", background='blue', font=("Arial", 16))
    label.pack(pady=20)

    # Define buttons for different indicators and functionalities
    def clear_canvas():
        for widget in content_frame.winfo_children():
            widget.destroy()

    button_style = {
        'font': ('Arial', 12),
        'width': 25,
        'bg': 'lightgrey',
        'fg': 'black',
        'activebackground': 'grey',
        'activeforeground': 'white'
    }

    # Add buttons for different indicators within the container
    btn_m2_money = tk.Button(container, 
                             text="M2 Money Supply",
                             command=lambda: display_indicator(M2_Money_Supply.main),
                             **button_style)
    btn_m2_money.pack(pady=10)

    btn_us_buildings = tk.Button(container, 
                                 text="U.S. Building Permits",
                                 command=lambda: display_indicator(us_building_permits.main),
                                 **button_style)
    btn_us_buildings.pack(pady=10)

    btn_ism_manufacturing = tk.Button(container,
                                      text="ISM Report - Manufacturing", 
                                      command=lambda: display_indicator(ism_report_scraper.main),
                                      **button_style)
    btn_ism_manufacturing.pack(pady=10)

    btn_ism_services = tk.Button(container,
                                 text="ISM Report - Services",
                                 command=lambda: display_indicator(ism_report_on_business_SERVICES.main),
                                 **button_style)
    btn_ism_services.pack(pady=10)

    btn_umsci = tk.Button(container,
                          text="U. of Michigan Sentiment Index", 
                          command=lambda: display_indicator(umsci_scrapper.main),
                          **button_style)
    btn_umsci.pack(pady=10)

    btn_vix_analysis = tk.Button(container, 
                                 text="VIX Analysis", 
                                 command=lambda: display_indicator(vix_analysis.main),
                                 **button_style)
    btn_vix_analysis.pack(pady=10)

    btn_benchmark_yield = tk.Button(container, 
                                    text="Benchmark Yield", 
                                    command=lambda: display_indicator(Benchmark_Yield_US.main),
                                    **button_style)
    btn_benchmark_yield.pack(pady=10)

    btn_sp500_permits_pct = tk.Button(container, 
                                     text="SP500 & Building Permits MA",
                                     command=lambda: display_indicator(sp500_building_permits_ma.main),
                                     **button_style)
    btn_sp500_permits_pct.pack(pady=10)

    btn_inflation = tk.Button(container, 
                              text="Inflation: CPI & PPI",
                              command=lambda: display_indicator(Inflation_CPI_and_PPI.main),
                              **button_style)
    btn_inflation.pack(pady=10)

    return frame

# Helper function to display individual indicators by clearing the content
def display_indicator(indicator_function):
    clear_canvas()
    indicator_function()

