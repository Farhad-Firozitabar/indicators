import pandas as pd

# Load the full dataset
file_path = 'data.csv'
df = pd.read_csv(file_path)

# Convert the 'Time' column to datetime
df['Time'] = pd.to_datetime(df['Time'])

# Function to calculate SMA
def calculate_sma(data, window):
    sma = data['Close'].rolling(window=window).mean()
    return sma

# Calculate the SMA with a 14-day window
df['SMA'] = calculate_sma(df, 14)

# Save the DataFrame with SMA to a new CSV file
output_path = 'data_with_SMA.csv'
df.to_csv(output_path, index=False)

# Display the resulting DataFrame
print(df.head(20))
