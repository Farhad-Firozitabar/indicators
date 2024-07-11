import pandas as pd
import numpy as np

# Load the data
file_path = 'data.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Ensure the data is sorted by date
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)

# Calculate Daily Returns
df['Daily Return'] = df['Close'].pct_change()

# Calculate Rolling Standard Deviation (Historical Volatility)
rolling_window = 30  # You can change this window size as needed
df['Rolling Std Dev'] = df['Daily Return'].rolling(window=rolling_window).std()

# Calculate True Range (TR)
df['High-Low'] = df['High'] - df['Low']
df['High-PrevClose'] = np.abs(df['High'] - df['Close'].shift(1))
df['Low-PrevClose'] = np.abs(df['Low'] - df['Close'].shift(1))
df['True Range'] = df[['High-Low', 'High-PrevClose', 'Low-PrevClose']].max(axis=1)

# Calculate Average True Range (ATR)
df['ATR'] = df['True Range'].rolling(window=rolling_window).mean()

# Calculate Exponential Moving Average of Volatility (EMA)
df['Volatility EMA'] = df['Daily Return'].abs().ewm(span=rolling_window, adjust=False).mean()

# Dropping intermediate calculation columns
df.drop(columns=['High-Low', 'High-PrevClose', 'Low-PrevClose'], inplace=True)

# Save the enhanced dataset to a new CSV file
output_file_path = 'enhanced_data.csv'  # Replace with the desired output path
df.to_csv(output_file_path, index=False)

# Display the resulting dataframe
print(df.head())

print(f"Enhanced dataset saved to {output_file_path}")
