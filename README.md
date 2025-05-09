# Google Business Profile Analytics Chart Generator

This Python script generates bar chart visualizations from a `.csv` file containing Google Business Profile analytics data. It groups performance metrics by business address and outputs a multi-page PDF report saved to the user's Desktop.

## 📊 What It Does

- Prompts for the business name to customize the report title.
- Automatically determines the **previous month** for labeling.
- Loads an analytics CSV file named `analytics.csv` from the Desktop.
- Filters out rows missing address data.
- Aggregates the following metrics by address:
  - `Google Search - Mobile`
  - `Google Search - Desktop`
  - `Google Maps - Mobile`
  - `Google Maps - Desktop`
  - `Calls`
- Converts data to numeric format for reliable plotting.
- Creates individual bar charts for each address in the data.
- Outputs the full report as a PDF titled:
<Business Name> <Last Month> Google Business Profile Analytics.pdf
and saves it to the Desktop.

## 🛠️ Requirements

- Python 3.x
- `pandas`
- `matplotlib`

Install dependencies using pip:

```bash
pip install pandas matplotlib

▶️ How to Use
Place the script in a convenient directory and name it something like analytics_report.py.

Ensure the CSV file (analytics.csv) is located on your Desktop.

Run the script using:
python analytics_report.py
When prompted, enter the business name (e.g., Cup O Code).

The output PDF will appear on your Desktop.

📁 Input File Format
The CSV file should include the following columns:

Address

Google Search - Mobile

Google Search - Desktop

Google Maps - Mobile

Google Maps - Desktop

Calls

Each row should represent a unique location or instance of Google Business Profile data.


