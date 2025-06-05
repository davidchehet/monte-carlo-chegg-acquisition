"""
This file contains methods for all visualiations of our data.
Data will be created in simulation.py, however all the data will
be displayed with the methods found here.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
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
    df = pd.DataFrame(sim_results)

    # Map each scenario to get an idea of what happened and our return
    scenario_order = ['bankruptcy', 'buyout', 'turnaround', 'stagnation']
    scenario_colors = {
        "bankruptcy": "#d9534f",   # red
        "buyout": "#5cb85c",       # green
        "turnaround": "#f0ad4e",   # orange
        "stagnation": "#5bc0de"    # blue
    }

    # Prepare data: list of percent_gain Series per scenario
    scenario_gains = [df[df["scenario"] == s]["percent_gain"] for s in scenario_order]
    color_list = [scenario_colors[s] for s in scenario_order]

    # Create plot
    plt.figure(figsize=(14, 7))

    plt.hist(
        scenario_gains,
        bins=60,
        stacked=True,
        color=color_list,
        edgecolor='black', 
        linewidth=0.6,
        label=[s.capitalize() for s in scenario_order]
    )

    # Breakeven on my investment
    plt.axvline(x=0, color='black', linestyle='--', linewidth=1.5, label='Breakeven (0%)')

    plt.title("Simulated ROI Distribution by Scenario", fontsize=18, weight='bold')
    plt.xlabel("Percent Gain (%)", fontsize=14)
    plt.ylabel("Number of Simulations", fontsize=14)
    plt.legend(title="Scenario", fontsize=12, title_fontsize=13)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.tight_layout()
    plt.show()

def plot_scenario_distribution(sim_results):
    """
    Plot a bar chart that displays the percentage of
    simulations that resulted in a given scenario of
    the company, with an overlapping line graph showing
    the average dollar gain for each scenario.

    Parameters:
      sim_results: A list of dictionaries of structure ->
      {
        "scenario": the outcome("buyout", "bankruptcy", etc)
        "price": exit price after simulation
        "percent_gain": roi in terms of percent
        "dollar_gain": roi in terms of dollars
      }

    Returns:
      Bar plot with overlapping line graph
    """

    df = pd.DataFrame(sim_results)

    scenario_order = ['bankruptcy', 'stagnation', 'turnaround', 'buyout']
    scenario_colors = {
        "bankruptcy": "#d9534f",
        "stagnation": "#5bc0de",
        "turnaround": "#f0ad4e",
        "buyout": "#5cb85c"
    }

    # Group data
    counts = df["scenario"].value_counts().reindex(scenario_order)
    percentages = (counts / counts.sum() * 100).round(2)
    avg_dollar_gain = df.groupby("scenario")["dollar_gain"].mean().reindex(scenario_order).round(2)

    bar_colors = [scenario_colors[s] for s in scenario_order]

    # Start plot
    sns.set_theme(style="whitegrid", context="talk")
    fig, ax1 = plt.subplots(figsize=(12, 7))

    # Bar chart for scenario frequencies
    bars = ax1.bar(
        scenario_order,
        percentages,
        color=bar_colors,
        edgecolor='black'
    )
    ax1.set_ylabel("Percentage of Simulations (%)", fontsize=13)
    ax1.set_ylim(0, max(percentages) * 1.2)

    # Add percentage labels
    for bar, pct in zip(bars, percentages):
        ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                 f'{pct:.1f}%', ha='center', va='bottom', fontsize=12)

    # Secondary axis for average dollar gain
    ax2 = ax1.twinx()
    ax2.plot(
        scenario_order,
        avg_dollar_gain,
        color='black',
        marker='o',
        linewidth=2,
        label='Average $ Gain'
    )
    ax2.set_ylabel("Average Dollar Gain", fontsize=13)
    ax2.set_ylim(min(avg_dollar_gain) * 1.2, max(avg_dollar_gain) * 1.2)

    # Clean up secondary axis
    ax2.grid(False)
    ax2.spines["right"].set_visible(False)
    ax2.tick_params(axis='y', which='both', length=0, labelsize=12)

    # Add dollar value annotations
    for x, y in zip(scenario_order, avg_dollar_gain):
      ax2.text(x, y + (max(avg_dollar_gain) * 0.10),
              f"${y:.2f}", ha='center', va='bottom', fontsize=11)


    plt.title("Scenario Frequency vs. Average Dollar Gain", fontsize=18, weight="bold")
    ax1.tick_params(axis='x', labelsize=12)
    ax1.tick_params(axis='y', labelsize=12)

    fig.tight_layout()
    plt.show()

def plot_cdf_of_roi(sim_results):
    """
    Create a sophisticated graph that models our
    return on investment in percent form with a CDF.

    How to read the graph:
    At any x-axis value(ROI %), the y-axis says:
    "What % of simulations delivered this ROI or worse?"

    Parameters:
    sim_results: A list of dictionaries of structure ->
    {
      "scenario": the outcome("buyout", "bankruptcy", etc)
      "price": exit price after simulation
      "percent_gain": roi in terms of percent
      "dollar_gain": roi in terms of dollars
    }

    Returns:
      CDF chart with annotations explaining different key values
    """
     # Convert and sort ROI
    df = pd.DataFrame(sim_results)
    roi_sorted = np.sort(df["percent_gain"].values)
    cdf = np.linspace(0, 1, len(roi_sorted))

    # Key percentiles
    p10 = np.percentile(roi_sorted, 10)
    p50 = np.percentile(roi_sorted, 50)
    p90 = np.percentile(roi_sorted, 90)

    i10 = np.searchsorted(roi_sorted, p10)
    i50 = np.searchsorted(roi_sorted, p50)
    i90 = np.searchsorted(roi_sorted, p90)

    # Simulations that doubled money
    num_doubled = np.sum(roi_sorted >= 100)
    pct_doubled = round((num_doubled / len(roi_sorted)) * 100, 2)

    # Plot setup
    sns.set_theme(style="whitegrid", context="talk")
    fig, ax = plt.subplots(figsize=(13, 7))

    # Plot CDF
    ax.plot(roi_sorted, cdf, color="black", linewidth=2, drawstyle='steps-post')

    # Breakeven line
    ax.axvline(x=0, color='red', linestyle='--', linewidth=1.5, label="Breakeven (0%)")

    # Dots for percentiles
    ax.plot(p10, cdf[i10], 'o', color='gray', markersize=8)
    ax.plot(p50, cdf[i50], 'o', color='blue', markersize=8, label="Median ROI")
    ax.plot(p90, cdf[i90], 'o', color='gray', markersize=8)

    # Text box: 10th percentile
    ax.text(0.02, 0.30,
            f"10th percentile ROI: {p10:.1f}%\n90% of simulations performed better",
            transform=ax.transAxes,
            fontsize=11, ha='left', va='bottom',
            bbox=dict(boxstyle="round,pad=0.4", facecolor='whitesmoke', edgecolor='gray'))

    # Text box: Median
    ax.text(0.50, 0.38,
            f"Median ROI: {p50:.1f}%\n50% of simulations returned less",
            transform=ax.transAxes,
            fontsize=11, ha='center', va='bottom',
            bbox=dict(boxstyle="round,pad=0.4", facecolor='lightblue', edgecolor='blue'))

    # Text box: 90th percentile
    ax.text(0.81, 0.83,
            f"90th percentile ROI: {p90:.1f}%\nOnly 10% did better than this",
            transform=ax.transAxes,
            fontsize=11, ha='right', va='bottom',
            bbox=dict(boxstyle="round,pad=0.4", facecolor='whitesmoke', edgecolor='gray'))

    # How often did I breakeven?
    breakeven_idx = np.searchsorted(roi_sorted, 0)
    breakeven_cdf = round(cdf[breakeven_idx] * 100, 1)
    ax.text(0.98, 0.05,
            f"At ROI = 0% (breakeven):\nCDF = {breakeven_cdf}%\n→ {breakeven_cdf}% of simulations\nreturned ≤ 0%",
            transform=ax.transAxes,
            fontsize=11, va='bottom', ha='right',
            bbox=dict(boxstyle="round,pad=0.4", facecolor='whitesmoke', edgecolor='gray'))

    # How often did I double my money?
    ax.text(0.98, 0.22,
            f"{num_doubled} simulations (≈{pct_doubled}%)\nreturned ≥ 100%",
            transform=ax.transAxes,
            fontsize=11, va='bottom', ha='right',
            bbox=dict(boxstyle="round,pad=0.4", facecolor='honeydew', edgecolor='green'))

    # Labels and ticks
    ax.set_title("Cumulative Distribution of Simulated ROI", fontsize=18, weight='bold')
    ax.set_xlabel("Percent Gain (%)", fontsize=14)
    ax.set_ylabel("Cumulative Probability", fontsize=14)
    ax.set_yticks(np.linspace(0, 1, 11))
    ax.set_yticklabels([f"{int(x*100)}%" for x in np.linspace(0, 1, 11)], fontsize=12)
    ax.tick_params(axis='x', labelsize=12)
    ax.grid(True)
    ax.legend(fontsize=12, loc='upper left')
    plt.tight_layout()
    plt.show()
