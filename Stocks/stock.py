'''Programming Assignment 5: Stock Earnings Summary Using Classes


Developed by Kyle DuBois. Version 1.2. Written 2/7/2020'''

from datetime import datetime
from datetime import date 

class Stock:
    """Simple representation of a stock."""

    def __init__(self, symbol, no_shares, purchase_price, current_price, purchase_date):
        """Initialize symbol, no_shares, purchase_price, current_price, and purchase_date attribues of a stock."""
        self.symbol = symbol
        self.no_shares = no_shares
        self.purchase_price = purchase_price
        self.current_price = current_price
        self.purchase_date = purchase_date

    # Create date object
    d1 = date.today()  # Get todays date
    today = d1.strftime("%m/%d/%Y")  # Set todays date in string object. 

    def build_stock(self): 
        """Build a new dictionary item for a stock."""
        stock = {'symbol':self.symbol, 
                 'no_shares':self.no_shares, 
                 'purchase_price':self.purchase_price, 
                 'current_price':self.current_price, 
                 'purchase_date':self.purchase_date
                 }
        return stock

    def investment_returns(self):
        """Calculates the earnings or losses for a stock"""
        investmentRet = (stock['current_price'] - stock['purchase_price']) * stock['no_shares']  # Calculate earnings/loss for each stock.
        return investmentRet  # Return the return on invesement.

    def percentage_yield(self):
        """Calculates the percentage yield for a stock"""
        percentYield = ((stock['current_price'] - stock['purchase_price'])/stock['purchase_price'])  # Calculate percentage yield for each stock
        return percentYield  # Return percentage yield.

    def yearly_return(self):
        """Calculate the yearly percentage of earnings or losses for a stock"""
        current_date = datetime.strptime(Stock.today,"%m/%d/%Y") # Create datetime object from string of current date
        purchase_date = datetime.strptime(stock['purchase_date'],"%m/%d/%Y") # Create datetime object from string of sotck purchase data.
        no_days = (current_date-purchase_date).days  #  Calc number of days between two datetime objects. 
        yearlyVal = 365.2425  # Constant year value
        yearlyReturn = (Stock.percentage_yield(self)/(no_days/yearlyVal))*100  # Calc the yearly return on investment
        return yearlyReturn  # Return yearly return on investment.

class Bond(Stock):
    """Simple representation of a bond that inherits from a stock."""

    def __init__(self, symbol, no_shares, purchase_price, current_price, purchase_date, coupon, bond_yield):
        """Initialize symbol, no_shares, purchase_price, current_price, purchase_date, coupon, and bond_yield attributes of a bond."""
        super().__init__(symbol, no_shares, purchase_price, current_price, purchase_date)
        self.coupon = coupon
        self.bond_yield = bond_yield
    
    def build_stock(self):
        """Builds a new dictionary item for a bond."""
        bond = {'symbol':self.symbol, 
            'no_shares':self.no_shares, 
            'purchase_price':self.purchase_price, 
            'current_price':self.current_price, 
            'purchase_date':self.purchase_date,
            'coupon':self.coupon,
            'bond_yield':self.bond_yield
            }
        return bond  

class Investor:
    """Simple representation of an investor."""

    def __init__(self, name, address, phone):
        """Initialize name, address, and phone attributes."""
        self.name = name.title()
        self.address = address
        self.phone = phone
        self.investor_ID = 1

    def get_investor(self):
        """Returns the investors name"""
        print(f"\nStock ownership for {self.name}")
        print('----------------------------------\n')

# Create list to put the newly created stocks
investor_holdings = []

# Instantiate all the stocks and one bond class, build a stock dictionary, and appned to stock list
investor_holdings.append(Stock('GOOGL', 125, 772.88, 941.53, '8/1/2019').build_stock())
investor_holdings.append(Stock('MSFT', 85, 56.60, 73.04, '8/1/2015').build_stock())
investor_holdings.append(Stock('RDS-A', 400, 49.58, 55.74, '8/1/2015').build_stock())
investor_holdings.append(Stock('AIG', 235, 54.21, 65.27, '8/1/2015').build_stock())
investor_holdings.append(Stock('FB', 150, 124.31, 172.45, '8/1/2015').build_stock())
investor_holdings.append(Stock('M', 425, 30.30, 23.98, '1/10/2017').build_stock())
investor_holdings.append(Stock('F', 85, 12.58, 10.95, '2/17/2017').build_stock())
investor_holdings.append(Stock('IBM', 80, 150.37, 145.30, '5/12/2017').build_stock())
investor_holdings.append(Bond('GT2:GOV', 200, 100.02, 100.05, '8/1/2017', 1.38, 1.35).build_stock())

new_investor = Investor('Bob Smith', '123 Main St', '123-456-7890')  # Instantiate Investor class
new_investor.get_investor()  # Call Investor class function to get investor name.
print('\nSTOCK            SHARE#         EARNINGS/LOSS        YEARLY% EARNINGS/LOSS')
print('----------------------------------------------------------------------------')
for stock in investor_holdings:  # Iterate through investor holdings list. 
    returns = Stock.investment_returns(stock)  # Call Stock class function to get investment returns.
    yearly = Stock.yearly_return(stock)  # Call Stock class function to get yearly return percentage.
    print('{symbol}            {shares}            ${returns:.2f}            {yearly:.2f}%'.format(symbol=stock['symbol'], 
                                                                                                   shares=stock['no_shares'], 
                                                                                                   returns=returns, 
                                                                                                   yearly=yearly))
