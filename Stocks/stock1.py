'''Programming Assignment 1: Stock Earnings Summary

This program will ask for current owned stock, number of shares owned, purhcase price, and current price.
It will calculate the earnings or loss of owned stock.
A terminal display will provide the stock infromation and earnings/loss.

Developed by Kyle DuBois. Version 1. Written 1/8/2020'''


# Ask for name, stock, share, purhcase price, and current price.
name = input('What is your name? ')
stock = input('Provide a stock symbol you own: ')
shares = input('How many shares do you own? ')
purchase_price = input('What was the purchase price of the stock? ')
current_price = input('What is the current price of the stock? ')
print('')

# Calculate Earnings/loss of stock.
base_cost = int(shares) * float(purchase_price)
current_cost = int(shares) * float(current_price)
stock_value = current_cost - base_cost


# Display stock information in terminal.
print('Stock ownership for ' + name.title())
print('------------------------------------------')
print(stock.upper() + ': ' + shares + ' shares')
print('Purhcase Price: ' + purchase_price)
print('Current Price per Share: ' + current_price)
print('Earnings/Loss to-date: $' + str(stock_value))
