import pandas as pd

# Load the full dataset
file_path = 'data.csv'
df = pd.read_csv(file_path)

# Convert the 'Time' column to datetime
df['Time'] = pd.to_datetime(df['Time'])

# Function to calculate EMA
def calculate_ema(data, window):
    ema = data['Close'].ewm(span=window, adjust=False).mean()
    return ema

# Calculate the EMA with a 14-day window
df['EMA'] = calculate_ema(df, 14)

# Save the DataFrame with EMA to a new CSV file
output_path = 'data_with_EMA.csv'
df.to_csv(output_path, index=False)

# Display the resulting DataFrame
print(df.head(20))
