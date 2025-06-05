"""
In this file we run the Monte Carlo simulation 
and plot visualizations to determine the potential
profit of our investment.
"""

from simulation import simulate_investment_return
from config import SCENARIO_PROBABILITIES, VALUATIONS, ENTRY_PRICE, SIMULATION_COUNT
from visualize import plot_percent_roi_histogram, plot_scenario_distribution, plot_cdf_of_roi

data = simulate_investment_return(ENTRY_PRICE, SIMULATION_COUNT, SCENARIO_PROBABILITIES, VALUATIONS)

plot_percent_roi_histogram(data)
plot_scenario_distribution(data)
plot_cdf_of_roi(data)
