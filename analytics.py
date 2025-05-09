import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import datetime

import os
desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')

def create_bar_charts(file_path):
    now = datetime.datetime.now()
    last_month = (now.replace(day=1) - datetime.timedelta(days=1)).strftime("%B")
    
    # Prompt the user for the title
    business = input("What business is this for: ")
    title = business + " " + last_month + " Google Business Profile Analytics"
    # Read the .csv file into a pandas DataFrame
    # df = pd.read_csv(file_path) old code that relies on being in current directory
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
    file_path = os.path.join(desktop, file_path)
    df = pd.read_csv(file_path)

    # Filter the DataFrame to only include rows where the Address column is not null
    df = df[df["Address"].notnull()]

    # Create a list of the columns to include in the bar graph
    # columns = ["Total searches", "Total views", "Search views", "Maps views", "Total actions", "Website actions", "Directions actions", "Phone call actions"]
    columns = [ "Google Search - Mobile", "Google Search - Desktop", "Google Maps - Mobile", "Google Maps - Desktop", "Calls"]

    # Convert the data in the specified columns to numerical format
    for column in columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')

    # Group the data by the "Address" column and calculate the total count for each column
    grouped = df.groupby("Address")[columns].sum()
    
    # Get the number of rows in the grouped dataframe
    rows = grouped.shape[0]
        
    # Create a figure and axis
    fig, axs = plt.subplots(rows, 1, figsize=(20, 5*rows), squeeze=False)
    
      # Loop over each row (address) in the grouped DataFrame
    for i, (address, row) in enumerate(grouped.iterrows()):
        # Plot the bar graph for this row
        bars = axs[i][0].bar(grouped.columns, row, align='center', alpha=0.5)

        # Loop over each bar in the bar graph
        for bar in bars:
         height = bar.get_height()
         axs[i][0].text(bar.get_x() + bar.get_width()/2, height, f'{int(height)}', ha='center', va='bottom')

        # Add a title to the graph
        axs[i][0].set_title(f"{address}")
        # axs[i][0].set_ylim([0, df[columns].sum().max()*1.1])

# Example usage
    # Old code that outputs in the current directory
    # with PdfPages('output.pdf') as pdf: 
    #     fig.suptitle(title, y=1, fontsize=20)
    #     plt.tight_layout()
    #     # plt.show() Uncomment this to show in window
    #     pdf.savefig(fig)
    
    # New code that outputs to the desktop
    output_file = os.path.join(desktop, f'{title}.pdf')
    with PdfPages(output_file) as pdf:
        fig.suptitle(title, y=1, fontsize=20)
        plt.tight_layout()
        pdf.savefig(fig)
        
create_bar_charts("analytics.csv")