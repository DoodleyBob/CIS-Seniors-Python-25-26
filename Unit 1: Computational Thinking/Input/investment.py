'''
Program: investment.py
Author: Elijah Snyder
Class: CIS Seniors
Date: 9/22/25

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
print("My Investment Calculator.")
print("=" * 25)

# Accept the Inputs

startingInvestment = float(input("Starting Investment: "))
numYearsInvesting = int(input("Years Investing "))
interestRate = float(input("Interest rate: "))

# Convert the rates to decimal
rate = interestRate / 100

#