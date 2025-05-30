"""
This file contains methods for all visualiations of our data.
Data will be created in simulation.py, however all the data will
be displayed with the methods found here.
"""

import matplotlib.pyplot as plt
from matplotlib import colors

def plot_percent_roi_histogram(sim_results):
    """
    Plot a histogram that shows all outcomes of
    percentage gain of our investment based on the outcomes
    calculated in the Monte-Cristo simulation.

    Parameters:
      sim_results: A list of dictionaries of structure ->
      {
        "scenario": the outcome("buyout", "bankruptcy", etc)
        "price": exit price after simulation
        "percent_gain": roi in terms of percent
        "dollar_gain": roi in terms of dollars
      }

    Returns:
      Histogram plot
    """
    roi_values = [result["percent_gain"] for result in sim_results]

    plt.hist(roi_values)
    plt.xlabel("Percent Gain/Loss")
    plt.ylabel("Frequency")
    plt.axvline(x=0)
    plt.show()
