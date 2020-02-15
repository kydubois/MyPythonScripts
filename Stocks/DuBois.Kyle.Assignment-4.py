'''Programming Assignment 4: Adding Functions to the Stock Problem

This program stores stock info in dictionaries. Dictionaries are added to a master list of myStocks.  
Three functions are called to calculate the return investment, percentage yield, and yearly return for each stock.
These calculated values are then appened to the stock dictionaries. Newly calculated values are then printed to the terminal. 

Developed by Kyle DuBois. Version 1. Written 2/1/2020'''

from DuBois_Kyle_Assignment_functions_4 import investment_returns, percentage_yield, yearly_return

# Generate dictionaries for stock details.
stock1 = {'symbol':'GOOGL', 'no_shares':125, 'purchase_price':772.88, 'current_price': 941.53, 'purchaseDate':'8/1/2019', 'invest_return':0.00, 'percentage_yield':0.00, 'yearly_return':0.00}
stock2 = {'symbol':'MSFT', 'no_shares':85, 'purchase_price':56.60, 'current_price':73.04, 'purchaseDate':'8/1/2015', 'invest_return':0.00, 'percentage_yield':0.00, 'yearly_return':0.00}
stock3 = {'symbol':'RDS-A', 'no_shares':400, 'purchase_price':49.58, 'current_price':55.74, 'purchaseDate':'8/1/2015', 'invest_return':0.00, 'percentage_yield':0.00, 'yearly_return':0.00}
stock4 = {'symbol':'AIG', 'no_shares':235, 'purchase_price':54.21, 'current_price':65.27, 'purchaseDate':'8/1/2015', 'invest_return':0.00, 'percentage_yield':0.00, 'yearly_return':0.00}
stock5 = {'symbol':'FB', 'no_shares':150, 'purchase_price':124.31, 'current_price':172.45, 'purchaseDate':'8/1/2015', 'invest_return':0.00, 'percentage_yield':0.00, 'yearly_return':0.00}
stock6 = {'symbol':'M', 'no_shares':425, 'purchase_price':30.30, 'current_price':23.98, 'purchaseDate':'1/10/2017', 'invest_return':0.00, 'percentage_yield':0.00, 'yearly_return':0.00}
stock7 = {'symbol':'F', 'no_shares':85, 'purchase_price':12.58, 'current_price':10.95, 'purchaseDate':'2/17/2017', 'invest_return':0.00, 'percentage_yield':0.00, 'yearly_return':0.00}
stock8 = {'symbol':'IBM', 'no_shares':80, 'purchase_price':150.37, 'current_price':145.30, 'purchaseDate':'5/12/2017', 'invest_return':0.00, 'percentage_yield':0.00, 'yearly_return':0.00}

myStocks = [stock1, stock2, stock3, stock4, stock5, stock6, stock7, stock8]      # Generate a list of my stock dictionaries

# call functions
investment_returns(myStocks)
percentage_yield(myStocks)
yearly_return(myStocks)


print('\nStock ownership for Bob Smith')
print('----------------------------------\n')
print('\nSTOCK            SHARE#            EARNINGS/LOSS            YEARLY% EARNINGS/LOSS')
print('-----------------------------------------------------------------------------------')
# iterate through myStocks list. 
# refernce dictionary keys for stock symbol, number of shares, and total value.
for stock in myStocks:
    print('{symbol}            {shares}            ${returns:.2f}            {yearly:.2f}%'.format(symbol=stock['symbol'], shares=stock['no_shares'], returns=stock['invest_return'], yearly=stock['yearly_return']))


