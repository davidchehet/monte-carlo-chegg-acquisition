"""
A collection of financial helper functions.
"""

def calculate_default_probability(company_yield, treasury_yield, ticker, time_frame):
    """
    Calculate the probability of a public company defaulting
    based on the US treasury yield over the same time period.

    Parameters:
      company_yield: The bond yield of the company over time_frame
      treasury_yield: The bond yield of US Treasury over time_frame(+/- 3 months)
      ticker: The company in question
      time_frame: Time until bond maturity in months

    Returns:
      The probability that the company will default, or go bankrupt
    """
    yield_spread = company_yield - treasury_yield
    # Calculate the recovery rate
    if company_yield <= 0.06:
        recovery_rate = 0.55
    elif company_yield > 0.06 and company_yield <= 0.10:
        recovery_rate = 0.40
    elif company_yield > 0.10 and company_yield <= 0.15:
        recovery_rate = 0.30
    elif company_yield > 0.15 and company_yield <= 0.20:
        recovery_rate = 0.25
    else:
        # Very distressed business
        recovery_rate = 0.20

    # Calculate default probability
    default_probability = yield_spread / (1 - recovery_rate)
    #print(f"Stock ticker {ticker} has a {default_probability * 100}% chance of going bankrupt over the next {time_frame} months.")
    return default_probability

def calculate_percent_roi(entry_price, exit_price):
    """
    Given an average entry cost and exit price of an equity,
    calculate the percentage return.

    Parameters: 
      entry_price: Average cost per share
      exit_price: Price per share at exit
    
    Returns:
      Percentage return of the investment
    """
    return round((exit_price - entry_price) / entry_price, 2)

def calculate_dollar_profit(share_count, entry_price, exit_price):
    """
    Given an average entry cost, exit price of an equity, and total shares
    owned, return the profit or loss, in dollars, of the investment.

    Parameters: 
      share_count: total shares owned
      entry_price: Average cost per share
      exit_price: Price per share at exit

    Returns:
      Profit or loss in dollars of the investment      
    """
    profit_per_share = exit_price - entry_price
    
    return round(profit_per_share * share_count, 2)
