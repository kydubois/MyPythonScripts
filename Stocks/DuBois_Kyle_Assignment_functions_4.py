'''Programming Assignment 4: Adding Functions to the Stock Problem

These functions are called to calculate the return investment, percentage yield, and yearly return for each stock.
These calculated values are then appened to the stock dictionaries for storage.

Developed by Kyle DuBois. Version 1. Written 2/1/2020'''

from datetime import datetime
from datetime import date

d1 = date.today()  # Get todays date
today = d1.strftime("%m/%d/%Y")  # Set todays date in string object. 

def investment_returns(stockList):
    """Calculates the earnings or losses for a stock"""
    for stock in stockList:  # Iterate through list of stock dictionaries
        investmentRet = (stock['current_price'] - stock['purchase_price']) * stock['no_shares']  # Calculate earnings/loss for each stock.
        stock['invest_return'] = investmentRet   # Append new value to investment return in each dictionary using key.

def percentage_yield(stockList):
    """Calculates the percentage yield for a stock"""
    for stock in stockList:  # Iterate through list of stock dictionaries
        percentYield = ((stock['current_price'] - stock['purchase_price'])/stock['purchase_price'])  # Calculate percentage yield for each stock
        stock['percentage_yield'] = percentYield # Append new value to percentage yield value in dictionary.

def yearly_return(stockList):
    """Calculate the yearly percentage of earnings or losses for a stock"""
    for stock in stockList:  # Iterate through list of stock dictionaries
        current_date = datetime.strptime(today,"%m/%d/%Y")  # Create datetome object from string of current date
        purchase_date = datetime.strptime(stock['purchaseDate'],"%m/%d/%Y") # Create datetime object from string of sotck purchase data.
        no_days = (current_date-purchase_date).days  #  Calc number of days between two datetime objects. 
        yearlyVal = 365.2425  # Constant year value
        yearlyReturn = (stock['percentage_yield']/(no_days/yearlyVal)) * 100  # Calculate the perctnage of yearly loss/earnings for each stock
        stock['yearly_return'] = yearlyReturn  # Append new value tp yearly_return in stock dictionary.
