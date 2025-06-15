# Juan Macias Vasquez
# Date 06/15/2025
# Module 4.2
# sitka_high_low_JCMV

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import sys

# Load data from CSV
filename = 'sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            # Skip missing or invalid data
            continue
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Menu loop for returning to see other graph or quiting
while True:
    print("\nTemperature Viewer")
    print("1. Show HIGH temperatures")
    print("2. Show LOW temperatures")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        plt.figure()
        plt.plot(dates, highs, c='red')
        plt.title("Daily High Temperatures - 2018", fontsize=20)
        plt.xlabel('', fontsize=14)
        plt.ylabel("Temperature (F)", fontsize=14)
        plt.tick_params(axis='both', labelsize=12)
        plt.gcf().autofmt_xdate()
        plt.show()

    elif choice == '2':
        plt.figure()
        plt.plot(dates, lows, c='blue')
        plt.title("Daily Low Temperatures - 2018", fontsize=20)
        plt.xlabel('', fontsize=14)
        plt.ylabel("Temperature (F)", fontsize=14)
        plt.tick_params(axis='both', labelsize=12)
        plt.gcf().autofmt_xdate()
        plt.show()

    elif choice == '3':
        print("Exiting the program. Goodbye!")
        sys.exit()

    else:# error if the user didnt put a correct number
        print("Invalid choice. Please enter 1, 2, or 3.")


