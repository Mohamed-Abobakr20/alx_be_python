"""
Your task is to create a Python script named explore_datetime.py. This script will demonstrate your ability to use the datetime module for handling dates and times in Python.
"""

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date


def calculate_future_date():
    current = display_current_datetime()
    print(f"Current date and time: {current.strftime("%Y-%m-%d %H:%M:%S")}")
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = (current + timedelta(days=days)).strftime("%Y-%m-%d")   
    return future_date

if __name__ == "__main__":
    print(f"Future date: {calculate_future_date()}")
   