#!/usr/bin/env python
import sys
import pandas as pd

# Define your address
file_path = sys.argv[1]
my_address = sys.argv[2]  # Replace this with your actual address

# Load the CSV file
df = pd.read_csv(file_path)

# Filter rows where address matches your address
filtered_df = df[df['address'] == my_address]

# Extract the dates from startTime and endTime
filtered_df['startDate'] = pd.to_datetime(filtered_df['startTime'],format='mixed').dt.date
filtered_df['startTime'] = pd.to_datetime(filtered_df['startTime'],format='mixed')
filtered_df['endTime'] = pd.to_datetime(filtered_df['endTime'],format='mixed')

# Filter for dates between 1 July 2023 and 20 June 2024
filtered_df = filtered_df[(filtered_df['startDate'] >= pd.to_datetime('2023-07-01').date()) & 
                          (filtered_df['startDate'] <= pd.to_datetime('2024-06-20').date())]

# Calculate the duration spent at home
filtered_df['duration'] = (filtered_df['endTime'] - filtered_df['startTime']).dt.total_seconds() / 3600

# Filter for significant duration (e.g., more than 18 hours)
filtered_df = filtered_df[filtered_df['duration'] > 18]

# Find unique dates
unique_dates = filtered_df['startDate'].unique()

# Count the number of weekdays
weekday_count = sum(pd.to_datetime(date).weekday() < 5 for date in unique_dates)

print("Dates where you worked from home between 1 July 2023 and 20 June 2024:")
for date in unique_dates:
    print(date)

print(f"\nTotal number of weekday dates: {weekday_count}")