import pandas as pd

# Load the full dataset
file_path = 'data.csv'
df = pd.read_csv(file_path)

# Convert the 'Time' column to datetime
df['Time'] = pd.to_datetime(df['Time'])

# Function to calculate EMA
def calculate_ema(data, span):
    return data.ewm(span=span, adjust=False).mean()

# Calculate the MACD components
def calculate_macd(data):
    # Calculate the 12-period EMA and 26-period EMA
    ema_12 = calculate_ema(data['Close'], 12)
    ema_26 = calculate_ema(data['Close'], 26)
    
    # Calculate the MACD Line
    macd_line = ema_12 - ema_26
    
    # Calculate the Signal Line
    signal_line = calculate_ema(macd_line, 9)
    
    # Calculate the MACD Histogram
    macd_histogram = macd_line - signal_line
    
    return macd_line, signal_line, macd_histogram

# Calculate MACD
df['MACD_Line'], df['Signal_Line'], df['MACD_Histogram'] = calculate_macd(df)

# Save the DataFrame with MACD to a new CSV file
output_path = 'data_with_MACD.csv'
df.to_csv(output_path, index=False)

# Display the resulting DataFrame
print(df.head(20))
