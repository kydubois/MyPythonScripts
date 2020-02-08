'''Programming Assignment 5: Stock Earnings Summary Using Classes


Developed by Kyle DuBois. Version 1. Written 2/7/2020'''

from datetime import datetime
from datetime import date

# Generate dictionaries for stock details.
stock_0 = {'symbol':'GOOGL', 'no_shares':125, 'purchase_price':772.88, 'current_price': 941.53, 'purchase_date':'8/1/2019'}
stock_1 = {'symbol':'MSFT', 'no_shares':85, 'purchase_price':56.60, 'current_price':73.04, 'purchase_date':'8/1/2015'}
stock_2 = {'symbol':'RDS-A', 'no_shares':400, 'purchase_price':49.58, 'current_price':55.74, 'purchase_date':'8/1/2015'}
stock_3 = {'symbol':'AIG', 'no_shares':235, 'purchase_price':54.21, 'current_price':65.27, 'purchase_date':'8/1/2015'}
stock_4 = {'symbol':'FB', 'no_shares':150, 'purchase_price':124.31, 'current_price':172.45, 'purchase_date':'8/1/2015'}
stock_5 = {'symbol':'M', 'no_shares':425, 'purchase_price':30.30, 'current_price':23.98, 'purchase_date':'1/10/2017'}
stock_6 = {'symbol':'F', 'no_shares':85, 'purchase_price':12.58, 'current_price':10.95, 'purchase_date':'2/17/2017'}
stock_7 = {'symbol':'IBM', 'no_shares':80, 'purchase_price':150.37, 'current_price':145.30, 'purchase_date':'5/12/2017'}

myStocks = [stock_0, stock_1, stock_2, stock_3, stock_4, stock_5, stock_6, stock_7] 

class Stock:

    def __init__(self, symbol, no_shares, purchase_price, current_price, purchase_date):
        """Represents aspects of a stock."""
        self.symbol = symbol
        self.no_shares = no_shares
        self.purchase_price = purchase_price
        self.current_price = current_price
        self.purchase_date = purchase_date
        self.stock_list = []

    # Create date object
    d1 = date.today()  # Get todays date
    today = d1.strftime("%m/%d/%Y")  # Set todays date in string object. 

    def build_stock(self, symbol, no_shares, purchase_price, current_price, purchase_date): 
        """Build a new deictionary item for a stock and append it to myList of stocks."""
        stock = {'symbol':self.symbol, 
                 'no_shares':self.no_shares, 
                 'purchase_price':self.purchase_price, 
                 'current_price':self.current_price, 
                 'purchase_date':self.purchase_date
                 }
        return stock
    
    def set_stock_list(self, stock)
        self.stock_list.append(stock)

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

    def __init__(self, symbol, no_shares, purchase_price, current_price, purchase_date, coupon, bond_yield):
        """Represents aspects of a stock, specif to a bond."""
        super().__init__(symbol, no_shares, purchase_price, current_price, purchase_date)
        self.coupon = coupon
        self.bond_yield = bond_yield
    
    def build_stock(self, symbol, no_shares, purchase_price, current_price, purchase_date, coupon, bond_yield):
        stock = {'symbol':self.symbol, 
            'no_shares':self.no_shares, 
            'purchase_price':self.purchase_price, 
            'current_price':self.current_price, 
            'purchase_date':self.purchase_date,
            'coupon':self.coupon,
            'bond_yield':self.bond_yield
            }
        self.stock_list.append(stock)

    

class Investor:

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.investor_ID = 1

    def get_investor(self):
        print(f"\nStock ownership for {self.name}")
        print('----------------------------------\n')


new_investor = Investor('Bob Smith', '123 Main St', '123-456-7890')
new_investor.get_investor()
print('\nSTOCK            SHARE#         EARNINGS/LOSS        YEARLY% EARNINGS/LOSS')
print('-----------------------------------------------------------------------------------')
# iterate through myStocks list. 
# refernce dictionary keys for stock symbol, number of shares, and total value.
for stock in myStocks:
    returns = Stock.investment_returns(stock)
    yearly = Stock.yearly_return(stock)
    print('{symbol}            {shares}            ${returns:.2f}            {yearly:.2f}%'.format(symbol=stock['symbol'], shares=stock['no_shares'], returns=returns, yearly=yearly))

# print('\nBOND           SHARE#         EARNINGS/LOSS        YEARLY% EARNINGS/LOSS')
# print('-----------------------------------------------------------------------------------')
# for bond in myBond;

my_bond = Bond('GT2:GOV', 200, 100.02, 100.05, '8/1/2017', 1.38, 1.35)
my_bond.build_stock()

for stock in myStocks:
    print(stock['symbol'])
