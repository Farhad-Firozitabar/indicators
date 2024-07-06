import pandas as pd

# Load the full dataset
file_path = 'EURUSD1440.csv'
df = pd.read_csv(file_path)

# Convert the 'Time' column to datetime
df['Time'] = pd.to_datetime(df['Time'])

# Function to calculate RSI using the Wilder's method
def calculate_rsi(data, window):
    delta = data['Close'].diff()
    
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    
    avg_gain = gain.rolling(window=window, min_periods=window).mean()[:window+1]
    avg_loss = loss.rolling(window=window, min_periods=window).mean()[:window+1]
    
    for i in range(window+1, len(gain)):
        avg_gain.loc[i] = (avg_gain.loc[i-1] * (window-1) + gain.loc[i]) / window
        avg_loss.loc[i] = (avg_loss.loc[i-1] * (window-1) + loss.loc[i]) / window
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

# Calculate the RSI with a 14-day window
df['RSI'] = calculate_rsi(df, 14)

# Add columns for analysis
df['Overbought'] = df['RSI'] > 70
df['Oversold'] = df['RSI'] < 30

# Save the DataFrame with RSI to a new CSV file
output_path = 'EURUSD1440_with_RSI.csv'
df.to_csv(output_path, index=False)

# Display the resulting DataFrame
print(df.head(20))
