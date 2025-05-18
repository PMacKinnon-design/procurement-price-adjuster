
import pandas as pd

# Example CPI values (static for MVP — in V2 we’ll use FRED API)
cpi_data = {
    '2018': 251.1,
    '2019': 255.7,
    '2020': 258.8,
    '2021': 271.0,
    '2022': 292.7,
    '2023': 305.5,
    '2024': 315.0,
    '2025': 320.0  # Estimated
}

def adjust_prices(df):
    df = df.copy()
    df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
    df['Year'] = df['Purchase Date'].dt.year.astype(str)

    df['Original Price'] = df['Price']
    df['CPI Then'] = df['Year'].map(cpi_data)
    df['CPI Now'] = cpi_data['2025']
    df['Adjusted Price'] = df['Original Price'] * (df['CPI Now'] / df['CPI Then'])
    df['% Change'] = ((df['Adjusted Price'] - df['Original Price']) / df['Original Price']) * 100

    return df[['Item', 'Purchase Date', 'Original Price', 'Adjusted Price', '% Change']]
