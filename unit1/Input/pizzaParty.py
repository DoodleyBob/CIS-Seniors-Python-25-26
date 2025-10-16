'''
Program: pizzaParty.py
Author: Elijah Snyder
Date: 10/16/2025


Program Specifications. Write a program to calculate the cost of hosting three pizza parties on Friday, Saturday and Sunday. Read from input the number of people attending, the average number of slices per person and the cost of one pizza. Dollar values are output with two decimals. For example, print(f"Cost: ${cost:.2f}").

'''
import math

SLICES = 8
TAX_RATE = 0.07
DELIVERY = 0.2


# INPUTS
num_people = int(input("Enter the number of people attending: "))
avg_slices = float(input("Enter the average number of slices per person: "))
pizza_cost = float(input("Enter the cost of the pizza: "))
weekend_cost = 0

# Calculate cost
pizzas = (avg_slices * num_people) / SLICES
num_pizzas = math.ceil(pizzas)
cost = num_pizzas * pizza_cost
tax = cost * TAX_RATE
delivery_fee = (cost + TAX_RATE) * DELIVERY
total_cost = cost + tax + delivery_fee
weekend_cost += total_cost

# Output the bill summary
print("\nFriday Night Party")
print(f"{num_pizzas} Pizzas: ${cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Delivery: ${delivery_fee:.2f}")
print(f"Total: ${total_cost:.2f}")



# Input info for Saturday party
print("\nFor Saturday Night Party, add the num_people, avg_slices, and pizza_cost all seperated by a space.")
num_people, avg_slices, pizza_cost = input().split()
num_people = int(num_people)
avg_slices = float(avg_slices)
pizza_cost = float(pizza_cost)

# Calculate cost
pizzas = (avg_slices * num_people) / SLICES
num_pizzas = math.ceil(pizzas)
cost = num_pizzas * pizza_cost
tax = cost * TAX_RATE
delivery_fee = (cost + TAX_RATE) * DELIVERY
total_cost = cost + tax + delivery_fee
weekend_cost += total_cost

#Output bill summary
print("\nSaturday Night Party")
print(f"{num_pizzas} Pizzas: ${cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Delivery: ${delivery_fee:.2f}")
print(f"Total: ${total_cost:.2f}")


# Input info for Sunday party
print("\nFor Sunday Night Party, add the num_people, avg_slices, and pizza_cost all seperated by a space.")
num_people, avg_slices, pizza_cost = input().split()
num_people = int(num_people)
avg_slices = float(avg_slices)
pizza_cost = float(pizza_cost)

# Calculate cost
pizzas = (avg_slices * num_people) / SLICES
num_pizzas = math.ceil(pizzas)
cost = num_pizzas * pizza_cost
tax = cost * TAX_RATE
delivery_fee = (cost + TAX_RATE) * DELIVERY
total_cost = cost + tax + delivery_fee
weekend_cost += total_cost

#Output bill summary
print("\nSunday Night Party")
print(f"{num_pizzas} Pizzas: ${cost:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Delivery: ${delivery_fee:.2f}")
print(f"Total: ${total_cost:.2f}")

# Print out a weekend total
print("The weekend total is: $" + str(weekend_cost))