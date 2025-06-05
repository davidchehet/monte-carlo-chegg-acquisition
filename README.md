# Monte Carlo Distressed Investing Framework

This project models the potential future outcomes of an investment in **Chegg Inc.** using a robust, scenario-based **Monte Carlo simulation**. It evaluates downside and upside probabilities such as bankruptcy, buyout, turnaround, and stagnation — generating thousands of simulations to quantify risk and return using real-world data like corporate bond yields and business segments.

As someone who enjoys value investing and picking stocks, I came across Chegg as a potential investment. However, this business is in distress and is going through turbulence, which is a type of company I usually want to avoid. I wanted to use Monte Carlo to project what might happen to the company and as a result how much money there is to be made or lost. I made the project in a way so that you can clone it, change the constants in `config.py`, and run this for any distressed business stock.

---

## Why This Project Matters

In a volatile investing environment, probabilistic thinking can offer superior insight to static valuation models. This simulation combines:

- **Market-driven financial signals** (bond yield spreads)
- **Scenario-weighted distributions** (triangular forecasting)
- **Investor-centered metrics** (ROI %, dollar gain, cumulative return)
- **High-quality visualizations** worthy of financial dashboards

The goal of this is to get the odds on your side, and use Math to see how likely you are to profit from investing in a distressed, riskier stock.

---

## Using Poetry to Run The Code

### Step 1: Clone the project

```bash
git clone https://github.com/davidchehet/monte-carlo-chegg-acquisition.git
cd monte-carlo-chegg 
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

---

## How It Works

### 1. Scenario Modeling

User assigns probabilities to future states of the company:
`['bankruptcy', 'buyout', 'turnaround', 'stagnation']`

Valuation ranges (`low`, `mode`, `high`) are defined for each in `config.py`. This is where you map out what you think the stock price would be if the scenario occurred, inputting low, mid, and high estimates.

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

**ROI distribution histogram, color-coded by profitability and scenario**  
![ROI Distribution](https://github.com/user-attachments/assets/d5d6ee0a-5723-4777-a46a-cad8201f139a)

**Scenario frequency vs average dollar gain**  
![Scenario Frequency](https://github.com/user-attachments/assets/8f335aaa-2eb4-4140-b621-ef455a87f2a0)

**CDF plot showing cumulative return probabilities**  
![CDF Plot](https://github.com/user-attachments/assets/382aa205-a9d8-45b2-89d5-61d2df78b93f)

---

## How to Customize This for Your Investment

This is a reusable framework.

1. Update `config.py` with new valuations, shares, entry price, etc.
2. Adjust your scenario probabilities in `config.py`.
3. For the `"bankruptcy"` key in `SCENARIO_PROBABILITIES`, adjust parameters for your business inside the `calculate_default_probability` function.
4. Run `main.py` to simulate and visualize.

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
