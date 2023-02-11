# 'Hello World Step 1
greeting = "Hello World!"
print(greeting)

# Creating a list with strings, ints, etc. 
candies = ["gummy", "sour", "spicy", "chocolate"]
price = [2, 2.5, 3, 3.5]
print(candies)
for x in candies:
    print(x)
 
   # Creating a dictionary
candy_prices = {}
prices = 0.50
for item in candies:
    candy_prices[item] = prices
    prices = (prices + 1)
print(candy_prices)

# Tuple
random_things = ("Star", [14, 23], (2, 4, 6), "The Color Green")
print(random_things)
