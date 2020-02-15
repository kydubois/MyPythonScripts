'''Programming Assignment 3: Using Dictionaries

This program will ask for users name. Stock info is stored in dictionaries.
Disctionaries are added to a master list.  The master list is iterated through to calculate values for
current cost, base cost, and earning/losses for each stock.  These values are then appened to the dictionaries.
New calculated values are then printed on the terminal. 

Developed by Kyle DuBois. Version 1. Written 1/23/2020'''


# Generate dictionaries for stock details.
stock1 = {'symbol':'GOOGL', 'no_shares':125, 'pPrice':772.88, 'cPrice': 941.53, 'bCost':0, 'cCost':0, 'value':0}
stock2 = {'symbol':'MSFT', 'no_shares':85, 'pPrice':56.60, 'cPrice':73.04, 'bCost':0, 'cCost':0, 'value':0}
stock3 = {'symbol':'RDS-A', 'no_shares':400, 'pPrice':49.58, 'cPrice':55.74, 'bCost':0, 'cCost':0, 'value':0}
stock4 = {'symbol':'AIG', 'no_shares':235, 'pPrice':54.21, 'cPrice':65.27, 'bCost':0, 'cCost':0, 'value':0}
stock5 = {'symbol':'FB', 'no_shares':150, 'pPrice':124.31, 'cPrice':172.45, 'bCost':0, 'cCost':0, 'value':0}

# Generate a list of my stock dictionaries
myStocks = [stock1, stock2, stock3, stock4, stock5]

# Iterate through myStock list.  
for stock in myStocks:
    # Refernece stock key for number of shares and purchase price.  Calc base cost.
    base_cost = stock['no_shares'] * stock['pPrice']
    # Append new base cost to dictionary using key.
    stock['bCost'] = base_cost
    # Refence stock key for number of shares and current value.  Calc current cost.
    current_cost = stock['no_shares'] * stock['cPrice']
    # Appned new current cost to dictionary using key.
    stock['cCost'] = current_cost

# Iterate through myStock list again with newly appened dictionary values added.
for stock in myStocks:
    # Reference stock key for current cost and base cost.  Calc earnings/loss for each stock.
    stock_value = stock['cCost'] - stock['bCost']
    # Round value to two decimal places.
    round_value = '$' + str(round(stock_value, 2))
    # Append new value to total value in each dictionary using key.
    stock['value'] = round_value

# Ask for stock owners name
name = input('What is your name? ')


# Display name, stock, shares, and current value information in terminal.
print('\nStock ownership for ' + name.title())
print('----------------------------------\n')
print('\nSTOCK\tSHARE#\tEARNINGS/LOSS')
print('-----------------------------------------')
# iterate through myStocks list. 
# refernce dictionary keys for stock symbol, number of shares, and total value.
for stock in myStocks:
    print(stock['symbol'] + "\t" + str(stock['no_shares']) + "\t" + stock['value'])
