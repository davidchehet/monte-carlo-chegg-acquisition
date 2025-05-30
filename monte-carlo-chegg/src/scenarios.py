"""
This file includes functions that calculate different
outcomes for the business, and then calculate a potential
end stock price using triangular distribution.
"""
import random
import numpy as np

def choose_scenario(dict):
    """
    Given a dictionary of weighted probabilities for a company's fate,
    randomly choose a scenario(e.g "buyout", "bankruptcy", etc.)

    Parameters:
      dict: Dictionary of ("scenario", probability)

    Returns:
      Key from dictionary as a string
    """
    keys = list(dict.keys())
    values = list(dict.values())

    return random.choices(keys, weights=values)[0]


def forecast_stock_price(scenario, valuation_dict):
    """
    Given a scenario of the fate of the company(e.g "buyout", "bankruptcy")
    forecast a potential stock price based on valuation predictions. Uses a 
    triangular distribution.

    Parameters:
      scenario: Acts as the key for the valuation_dict
      valuation_dict: Dictionary of ("scenario", stock_prediction)

    Returns:
      Forecasted stock price
    """
    potential_prices = valuation_dict[scenario]
    left = potential_prices[0]
    mode = potential_prices[1]
    right = potential_prices[2]

    return round(np.random.triangular(left, mode, right), 2)

 
def run_scenario_once(choose_scenario, forecast_stock_price, scenario_prob, valuation_dict):
    """
    The central function for the Monte Carlo simulation. We call choose_scenario to get
    a weighted random choice for the fate of the company. We then pass that value into the
    forecast_stock_price function to get a predicted stock price using a triangular distribution. Lastly we return a JSON that stores what happened and the exit price.

    Parameters:
      choose_scenario: func to generate scenario
      forecast_stock_price: func to generate stock price based on scenario
      scenario_prob: Dictionary of ("scenario", probability)
      valuation_dict: Dictionary of ("scenario", stock_prediction)

    Returns:
      JSON format of the scenario and the stock price
    """

    scenario = choose_scenario(scenario_prob)
    price = forecast_stock_price(scenario, valuation_dict)

    return {
        "scenario": scenario,
        "price": price
    }

