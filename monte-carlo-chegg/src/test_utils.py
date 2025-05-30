# Test our utility functions
from financials import calculate_default_probability, calculate_dollar_profit, calculate_percent_roi
from scenarios import choose_scenario, forecast_stock_price, run_scenario_once
from config import SCENARIO_PROBABILITIES, VALUATIONS, ENTRY_PRICE, SHARE_COUNT, SIMULATION_COUNT
from simulation import simulate_investment_return

calculate_default_probability(0.2251, 0.0412, "$CHGG", 15)
choose_scenario(SCENARIO_PROBABILITIES)
forecast_stock_price("buyout", VALUATIONS)
run_scenario_once(choose_scenario=choose_scenario, forecast_stock_price=forecast_stock_price, scenario_prob=SCENARIO_PROBABILITIES, valuation_dict=VALUATIONS)
calculate_percent_roi(ENTRY_PRICE, 3.00)
calculate_dollar_profit(SHARE_COUNT, ENTRY_PRICE, 3.00)
print(simulate_investment_return(ENTRY_PRICE, SIMULATION_COUNT, SCENARIO_PROBABILITIES, VALUATIONS))