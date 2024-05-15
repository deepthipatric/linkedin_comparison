import pandas as pd
import matplotlib.pyplot as plt

url = r"xyz.csv"
data = pd.read_csv(url)

# Convert 'Date' column to datetime type
data['Date'] = pd.to_datetime(data['Date'])

# Define the change date
change_date = pd.to_datetime('11/1/2023')

# Split data into before and after change date
data_before = data[data['Date'] <= change_date]
data_after = data[data['Date'] > change_date]

# Create the plot
plt.figure(figsize=(12, 6))

# Plotting impressions
plt.plot(data_before['Date'], data_before['Impressions'], label='Impressions (Before)', marker='o')
plt.plot(data_after['Date'], data_after['Impressions'], label='Impressions (After)', marker='o')

# Plotting engagements
plt.plot(data_before['Date'], data_before['Engagements'], label='Engagements (Before)', marker='o')
plt.plot(data_after['Date'], data_after['Engagements'], label='Engagements (After)', marker='o')

# Marking the change date
plt.axvline(x=change_date, color='r', linestyle='--', linewidth=1, label='Change Date')

plt.title('Impressions and Engagements Before and After Change Date')
plt.xlabel('Date')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
