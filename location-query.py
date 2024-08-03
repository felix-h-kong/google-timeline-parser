#!/usr/bin/env python3
import sys
import pandas as pd

# Load the CSV file
file_path = sys.argv[1]
location_name = sys.argv[2]
df = pd.read_csv(file_path)

filtered_df = df[df['locationName'] == ']

# Extract the dates from startTime
filtered_df['startDate'] = pd.to_datetime(filtered_df['startTime'],format="mixed").dt.date
filtered_df = filtered_df[filtered_df['startDate'] >= pd.to_datetime('2023-07-01').date()]
filtered_df = filtered_df[filtered_df['startDate'] <= pd.to_datetime('2024-06-30').date()]

# Find unique dates
unique_dates = filtered_df['startDate'].unique()

# Count the number of weekdays
weekday_count = sum(pd.to_datetime(date).weekday() < 5 for date in unique_dates)

print(f"Dates where locationName is {location_name}:")
for date in unique_dates:
    print(date)

print(f"\nTotal number of weekday dates: {weekday_count}")
