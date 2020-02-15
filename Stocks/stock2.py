'''Programming Assignment 2: Stock Earning Summary for Multiple Stocks

This program will ask for users name. Stock info is stored in lists.
Will generate lists for the stock base cost and current price.
It will calculate the earnings/loss of owned stocks and store in new list
A terminal display will provide the stock infromation and earnings/loss.

Developed by Kyle DuBois. Version 1. Written 1/17/2020'''


# Generate lists
stock_symbol = ["GOOGL","MSFT","RDS-A","AIG","FB"]
no_shares = [125,85,400,235,150]
purchase_price = [772.88,56.60,49.58,54.21,124.31]
current_value = [941.53,73.04,55.74,65.27,172.45]

# Generate new lists for base cost, current cost, and stock value
base_cost = []
current_cost = []
stock_value = []

# Iterate through list data to calculate base cost and add to base cost list
for shares, price in zip(no_shares,purchase_price):
    b_cost = float(shares) * float(price)
    base_cost.append(b_cost)

# Iterate through list data to calculate current cost and add to current cost list
for shares, current in zip(no_shares,current_value):
    c_cost = float(shares) * float(current)
    current_cost.append(c_cost)   

# Iterate through list data to calculate stock value and add to stock value list
for current, base in zip(current_cost,base_cost):
    value = float(current) - float(base)
    round_value = '$' + str(round(value, 2))
    stock_value.append(round_value)   

# Ask for name
name = input('What is your name? ')

# Display name, stock, shares, and current value information in terminal.
print(f'\nStock ownership for {name.title()}')
print(f'----------------------------------\n')


# Create lists for output titles
titles = ["STOCK", "SHARE#", "EARNINGS/LOSS"]
# Combine titles with data and convert to tuples for enumrate method
data = [titles] + list(zip(stock_symbol, no_shares, stock_value))


# We use enumerate method to count the rows and print --- at row 0
for i, d in enumerate(data):
    # Adds | followed by data element and 12 spaces to the left
    line = '| '.join(str(x).ljust(12) for x in d)
    print(line)
    if i == 0:
        print('-' * len(line))
