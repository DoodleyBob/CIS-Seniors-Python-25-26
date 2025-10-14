# import the random module
import random

#Generate a random floating point number
print(random.random())
print(random.random())
print(random.random())
print()

# Using randrange()
print(random.randrange(5))
print(random.randrange(5))
print(random.randrange(5))
print(random.randrange(5))
print(random.randrange(5))

print()
print("Using a seed.")
print(random.seed(15))

print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))