from financials import calculate_default_probability

"""
This file defines assumptions we are making about
different outcomes for the publicly traded company Chegg($CHGG).

I own the stock. Position as of 5/30/2025:
3,050 Shares
$1.30 Average Cost Basis

Scenario Labels for Chegg:

1. Bankruptcy: Stock goes to $0.
2. Buyout: Acquirer pays a premium on current stock price($1.00). Buyout could be partial/total.
3. Turnaround: Company turns around revenue and valuation rebounds.
4. Stagnation: Revenue continues to flatline, strategic acquisition fails.

Now that we have labels, we need probabilities for what I think will happen.
This requires human intutiton.

1. Bankruptcy: 0.23 based on latest data(see utils.py/calculate_default_probability)

2. Buyout: 0.27 based on strategic review with Goldman, dozens of active conversations with buyers,
asset values of businesses like Busuu, Skills, Study, etc, licensing with big tech/AI training
slight subtraction due to higher rates.

3. Turnaround: 0.15 based on steep 30% declines in core business. I don't envision a turnaround in the core
business, especially with GPT, Gemini, and Cursor targetting students.

4. Stagnation: 0.30 based on Chegg's major cost cutting programs. Simply put, if the core business remains
small while costs are cut, and if no buyers want Chegg's data, they could stay at these
depressed levels.
"""

SCENARIO_PROBABILITIES = {
    "bankruptcy": round(calculate_default_probability(0.2251, 0.0412, "$CHGG", 15), 2), # 0.23 with latest data
    "buyout": 0.32,
    "turnaround": 0.15,
    "stagnation": 0.30
}
ENTRY_PRICE = 1.30
SHARE_COUNT = 3050
SIMULATION_COUNT = 100000

# Low, Medium, and High stock prices based on scenario
VALUATIONS = {
    "bankruptcy": (0.00, 0.05, 0.10), # Full $0 wipeout to maybe pennies from Chapter 11.
    "buyout": (2.20, 3.20, 3.50), # Low: Busuu sells 2x sales and low value for data, Med: 3x Busuu, strong data, High: Bidding war.
    "turnaround": (1.60, 2.40, 3.00), # Valuations would need to be less than buyout but still appreciate.
    "stagnation": (0.80, 1.20, 1.70) # Study erodes fully, cost cutting continues, licensing somewhat successful.
}
