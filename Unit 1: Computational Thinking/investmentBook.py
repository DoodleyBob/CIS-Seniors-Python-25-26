'''
Program: investmentBook.py
Author: Elijah Snyder
Course: CIS Seniors
Date 09/23/25

Compute and Investment amount
1. The inputs are:
    starting investment amount
    number of years
    interest rate (an integer percent)

2. The report is displayed in tabular form with a header
3. Computations and outputs:
    for each year of the investment
        compute the interest and add it to the investment print a formatted row of results for that year.
4. the ending investment amount you have paid in total are displayed
'''
print("\n\n")
print("=" * 50)
print("My Investment Tracker")
print("=" * 50)

# Accept the Inputs 
startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))

# Convert the rate to a decimal number
rate = rate / 100

# Initialize the accumulator for the interest
totalInterest = 0.0

# Display the header for the table




# Compute and display the results for each year

print("%4s%18s%10s%16s" % ("Year", "Starting balance", "Interest", "Ending balance"))
for year in range(1, years + 1):
    interest = startBalance *100 rate
    endBalance = startBalance + interest
    totalInterest += interest
    print("%4d%18.2f%10.2f%16.2f" % (year, startBalance, interest, endBalance))
    startBalance = endBalance


# Display the results from
print("Ending Balance: $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % totalInterest)