"""
This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).
"""

size = int(input("Enter the size of the pattern: "))

counter = 0
while counter < size:
    for i in range(size):
        print("*", end="")
    print("")
    counter = counter + 1    