# Monte Carlo Investing Framework

## Description

This project is a framework for using Monte Carlo simulations to analyze how often you will make money investing in a near-bankrupt public business. Investors/coders need to take into account how likely they think the business goes broke, turnsaround, is acquired, or stagnates. However, after that user input, the software runs 100,000 simulations and outputs potential returns on investment and how often those returns occur.

## Motivation for this project

I am basically obsessed with the financial markets, specifically buying stock in indvidual companies I believe have the ability to outperform. Thus far I have achieved above average performance, however most of my success came from intuition and I wish to systematize parts of my approach. I invested 1 year ago into a highly distressed business known as **Chegg Inc($CHGG)**. Given the distessed nature of the business, I decided I needed more than just my intuition to be comfortable allocating capital. I wanted to use Monte Carlo simulations to project what might happen to the company and as a result how much money there is to be made or lost. I made the project in a way so that you can clone it, change the constants in `config.py`, and run this for any distressed business stock.

---

## Setup and Installation

### Step 1: Clone the project

```bash
git clone https://github.com/davidchehet/monte-carlo-chegg-acquisition.git
cd monte-carlo-chegg-acquisition
```

### Step 2: Install Poetry (if not installed)

```bash
pip install poetry
```

### Step 3: Create virtual environment and install dependencies

```bash
poetry install
```

### Step 4: Activate the shell

```bash
poetry shell
```

### Step 5: Run the simulation

```bash
python src/main.py
```

Or run it without entering a shell:

```bash
poetry run python src/main.py
```

## Contributing

### Clone the repo
```bash
git clone https://github.com/davidchehet/monte-carlo-chegg-acquisition
cd monte-carlo-chegg-acquisition
```

### Install Dependencies
 ```bash
 poetry install
 ```

### Submit a pull request
If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.

## How to Customize This for Your Investment

This is a reusable framework.

1. Update `config.py` with new valuations, shares, entry price, etc.
2. Adjust your scenario probabilities in `config.py`.
3. For the `"bankruptcy"` key in `SCENARIO_PROBABILITIES`, adjust parameters for your business inside the `calculate_default_probability` function stored in `financials.py`. Look at the function documentation for details on how to implement it for your business.
4. Run `main.py` to simulate and visualize.

---

## Table of Contents

- [Why This Project Matters](#why-this-project-matters)
- [Using Poetry to Run The Code](#using-poetry-to-run-the-code)
- [How It Works](#how-it-works)
  - [1. Scenario Modeling](#1-scenario-modeling)
  - [2. Simulation Engine](#2-simulation-engine)
  - [3. Visualization](#3-visualization)
- [How to Customize This for Your Investment](#how-to-customize-this-for-your-investment)
- [Potential Enhancements](#potential-enhancements)
- [Author Notes](#author-notes)

---

## Why This Project Matters

In a volatile investing environment, probabilistic thinking can offer superior insight to static valuation models. This simulation combines:

- **Market-driven financial signals** (bond yield spreads)
- **Scenario-weighted distributions** (triangular forecasting)
- **Investor-centered metrics** (ROI %, dollar gain, cumulative return)
- **High-quality visualizations** worthy of financial dashboards

The goal of this is to get the odds on your side, and use Math to see how likely you are to profit from investing in a distressed, riskier stock.

---


## How It Works

### 1. Scenario Modeling

User assigns probabilities to future states of the company:
`['bankruptcy', 'buyout', 'turnaround', 'stagnation']`

Valuation ranges (`low`, `mid`, `high`) are defined for each in `config.py`. This is where you map out what you think the stock price would be if the scenario occurred, inputting low, mid, and high estimates.

---

### 2. Simulation Engine

For each iteration:

- A scenario is sampled based on weights
- A stock price is drawn from a triangular distribution
- ROI and dollar return are calculated

Each iteration creates and appends a dictionary to a list that we then query for our visualizations.

---

### 3. Visualization

The results are visualized using **Seaborn** and **Matplotlib**:
## Key Points:
Graphs reflect the following constant values:
- ENTRY_PRICE: 1.30
- SHARE_COUNT: 3050

**ROI distribution histogram, color-coded by profitability and scenario**  
![ROI Distribution](https://github.com/user-attachments/assets/d5d6ee0a-5723-4777-a46a-cad8201f139a)

**Scenario frequency vs average dollar gain**  
![Scenario Frequency](https://github.com/user-attachments/assets/8f335aaa-2eb4-4140-b621-ef455a87f2a0)

**CDF plot showing cumulative return probabilities**  
![CDF Plot](https://github.com/user-attachments/assets/382aa205-a9d8-45b2-89d5-61d2df78b93f)

---

## Potential Enhancements

- Add GUI dashboard with Streamlit or Plotly Dash  
- Model multiple time horizons (1-year, 3-year, 5-year exit)  
- Include boxplots or violin plots for deeper distribution insight  
- Save simulation output to CSV or a local database  
- Integrate LLMs for real-time earnings sentiment classification  
- Add CLI interface for parameter overrides

---

## Author Notes

I hope you find this project useful — whether you're investing, modeling, or just learning how to bring probabilities into decision-making.  
Happy investing!





