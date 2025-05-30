"""
This file is for configuring the code that runs
on each Monte Carlo simulation, and store the results
for further analysis in the future.
"""

from scenarios import choose_scenario, forecast_stock_price, run_scenario_once
from financials import calculate_dollar_profit, calculate_percent_roi
from config import SHARE_COUNT

def simulate_investment_return(entry_price, num_trials, scenario_probs, valuation_ranges):
    """
    For each iteration of the Monte-Carlo simulation,
    predict a outcome for the company, a share price, return
    on investment in percent form, and return in dollars. Append
    that JSON to a list for analysis later on.

    Parameters:
      entry_price: Average cost of ownership of the stock
      num_trials: Number of iterations of Monte Carlo
      scenario_probs: Dictionary of ("scenario", probability)
      valuation_ranges: Dictionary of ("scenario", stock_prediction)

    Returns:
      List of JSON elements, where each JSON stores a run of Monte Carlo
    """

    output_list = []
    shares_owned = SHARE_COUNT
    
    for simulation in range(num_trials):
        prediction = run_scenario_once(choose_scenario, forecast_stock_price, scenario_probs, valuation_ranges)
        # Capture exit price from run_scenario_once method
        exit_price = prediction["price"]
        percent_gain = calculate_percent_roi(entry_price, exit_price)
        dollar_gain = calculate_dollar_profit(shares_owned, entry_price, exit_price)
        json_output = {
            "scenario": prediction["scenario"],
            "price": exit_price,
            "percent_gain": round(percent_gain * 100, 2),
            "dollar_gain": round(dollar_gain, 2)
        }

        output_list.append(json_output)
    
    return output_list
