'''Programming Assignment 5: Stock Earnings Summary Using Classes

This script defines three classes.  The Stock class which contains funcitons for creating a stock
calculating its return on investment, percentage yield, and yearly return on investment.
The Bond class inherits from the Stock class but also includes attributs for coupon and yield.
The Investor class takes attributes to create investor details and returns that information.
The final part of this script will instantiate each class and call functions to return impormation.

Developed by Kyle DuBois. Version 1. Written 2/8/2020'''

from datetime import datetime
from datetime import date

class Stock:
    """Simple representation of a stock."""

    def __init__(self, purchase_ID, symbol, no_shares, purchase_price, current_price, purchase_date):
        """Initialize symbol, no_shares, purchase_price, current_price, and purchase_date attribues of a stock."""
        self.symbol = symbol
        self.no_shares = no_shares
        self.purchase_price = purchase_price
        self.current_price = current_price
        self.purchase_date = purchase_date
        self.purchase_ID = purchase_ID 

    # Create date object
    d1 = date.today()  # Get todays date
    today = d1.strftime("%m/%d/%Y")  # Set todays date in string object.

    def build_stock(self): 
        """Build a new dictionary item for a stock."""
        stock = {'purchase_ID':self.purchase_ID,
                 'symbol':self.symbol, 
                 'no_shares':self.no_shares, 
                 'purchase_price':self.purchase_price, 
                 'current_price':self.current_price, 
                 'purchase_date':self.purchase_date
                 }
        return stock

    def get_stock(self):
        """Return summary of stock infromation"""
        print('\n ' + self.symbol)
        print('  Shares: ' + str(self.no_shares))
        print('  Purchase Price: $' + str(self.purchase_price))
        print('  Current Price: $' + str(self.current_price))
        print('  Purchase Date: ' + self.purchase_date)

    def investment_returns(self):
        """Calculates the earnings or losses for a stock"""
        investmentRet = (holding['current_price'] - holding['purchase_price']) * holding['no_shares']  # Calculate earnings/loss for each stock.
        return investmentRet  # Return the return on invesement.

    def percentage_yield(self):
        """Calculates the percentage yield for a stock"""
        percentYield = ((holding['current_price'] - holding['purchase_price'])/holding['purchase_price'])  # Calculate percentage yield for each stock
        return percentYield  # Return percentage yield.

    def yearly_return(self):
        """Calculate the yearly percentage of earnings or losses for a stock"""
        current_date = datetime.strptime(Stock.today,"%m/%d/%Y") # Create datetime object from string of current date
        purchase_date = datetime.strptime(holding['purchase_date'],"%m/%d/%Y") # Create datetime object from string of sotck purchase data.
        no_days = (current_date-purchase_date).days  #  Calc number of days between two datetime objects. 
        yearlyVal = 365.2425  # Constant year value
        yearlyReturn = (Stock.percentage_yield(self)/(no_days/yearlyVal))*100  # Calc the yearly return on investment
        return yearlyReturn  # Return yearly return on investment.

class Bond(Stock):
    """Simple representation of a bond that inherits from a stock."""

    def __init__(self, purchase_ID, symbol, no_shares, purchase_price, current_price, purchase_date, coupon, bond_yield):
        """Initialize symbol, no_shares, purchase_price, current_price, purchase_date, coupon, and bond_yield attributes of a bond."""
        super().__init__(purchase_ID, symbol, no_shares, purchase_price, current_price, purchase_date)
        self.coupon = coupon
        self.bond_yield = bond_yield
    
    def build_stock(self):
        """Builds a new dictionary item for a bond."""
        bond = {'purchase_ID':self.purchase_ID,
            'symbol':self.symbol, 
            'no_shares':self.no_shares, 
            'purchase_price':self.purchase_price, 
            'current_price':self.current_price, 
            'purchase_date':self.purchase_date,
            'coupon':self.coupon,
            'bond_yield':self.bond_yield
            }
        return bond

    def get_stock(self):
        """Return summary of stock infromation"""
        print('\n ' + self.symbol)
        print('  Shares: ' + str(self.no_shares))
        print('  Purchase Price: $' + str(self.purchase_price))
        print('  Current Price: $' + str(self.current_price))
        print('  Purchase Date: ' + self.purchase_date)
        print('  Coupon: ' + str(self.coupon))
        print('  Bond Yield: ' + str(self.bond_yield) + '%')

class Investor:
    """Simple representation of an investor."""

    def __init__(self, investor_ID, name, address, city, state, zip_code, phone):
        """Initialize name, address, and phone attributes."""
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.investor_ID = investor_ID

    def get_name(self):
        """Returns the investors name"""
        fullName = self.name.title()
        return fullName
    
    def get_investor(self):
        """Returns summary of investor's infomation."""
        print("\n" + self.name)
        print("  Address: " + self.address)
        print("  City: " + self.city)
        print("  State: " + self.state)
        print("  Zip Code: " + self.zip_code)
        print("  Phone: " + self.phone)


# Create list to put the newly created stocks or bonds.
stock_holdings = []
bond_holdings = []

# Instantiate all the stocks and one bond class, build stock & bond dictionaries, and append dictionaries to stock or bond list.
stock_holdings.append(Stock(0,'GOOGL', 125, 772.88, 941.53, '8/1/2019').build_stock())
stock_holdings.append(Stock(1,'MSFT', 85, 56.60, 73.04, '8/1/2015').build_stock())
stock_holdings.append(Stock(2,'RDS-A', 400, 49.58, 55.74, '8/1/2015').build_stock())
stock_holdings.append(Stock(3,'AIG', 235, 54.21, 65.27, '8/1/2015').build_stock())
stock_holdings.append(Stock(4,'FB', 150, 124.31, 172.45, '8/1/2015').build_stock())
stock_holdings.append(Stock(5,'M', 425, 30.30, 23.98, '1/10/2017').build_stock())
stock_holdings.append(Stock(6,'F', 85, 12.58, 10.95, '2/17/2017').build_stock())
stock_holdings.append(Stock(7,'IBM', 80, 150.37, 145.30, '5/12/2017').build_stock())
bond_holdings.append(Bond(0,'GT2:GOV', 200, 100.02, 100.05, '8/1/2017', 1.38, 1.35).build_stock())

new_investor = Investor(0,'bob smith', '123 Main St', 'Portland', 'OR', '97210', '123-456-7890')  # Instantiate Investor class

print(f"\nStock ownership for " + new_investor.get_name())  # Call Investor class function to get investor name.
print('\nSTOCK            SHARE#         EARNINGS/LOSS        YEARLY% EARNINGS/LOSS')
print('----------------------------------------------------------------------------')
for holding in stock_holdings:  # Iterate through investor holdings list. 
    returns = Stock.investment_returns(holding)  # Call Stock class function to get investment returns.
    yearly = Stock.yearly_return(holding)  # Call Stock class function to get yearly return percentage.
    print('{symbol}            {shares}            ${returns:.2f}            {yearly:.2f}%'.format(symbol=holding['symbol'], 
                                                                                                   shares=holding['no_shares'], 
                                                                                                   returns=returns, 
                                                                                                   yearly=yearly))
print('\n----------------------------------------------------------------------------\n')
print(f"\nBond ownership for " + new_investor.get_name())  # Call Investor class function to get investor name.
print('\nBOND            SHARE#         EARNINGS/LOSS        YEARLY% EARNINGS/LOSS')
print('----------------------------------------------------------------------------')
for holding in bond_holdings:  # Iterate through investor holdings list. 
    bond_returns = Bond.investment_returns(holding)  # Call Bond class function inherited from Stock class to get investment returns.
    bond_yearly = Bond.yearly_return(holding)  # Call Bond class function inherited from Stock class to get yearly return percentage.
    print('{symbol}            {shares}            ${returns:.2f}            {yearly:.2f}%'.format(symbol=holding['symbol'], 
                                                                                                   shares=holding['no_shares'], 
                                                                                                   returns=bond_returns, 
                                                                                                   yearly=bond_yearly))
