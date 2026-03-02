# Options Pricer

> **Live demo :** [options-pricer2.streamlit.app](https://options-pricer2.streamlit.app/)

Streamlit application for pricing a wide range of **financial options** using multiple quantitative methods, with interactive Greeks visualisation.

---

## Supported Options

| Category | Types |
|----------|-------|
| **Vanilla** | Call, Put |
| **Exotic** | Asian, Barrier, Lookback, Digit, Quanto |
| **Structured** | Autocall |
| **Strategies** | Spread, Straddle, Strangle, and more |

---

## Pricing Methods

| Method | Description |
|--------|-------------|
| **Black-Scholes** | Closed-form analytical solution |
| **Monte Carlo** | Stochastic simulation with configurable paths |
| **Binomial Tree** | Discrete-time lattice model |

---

## Greeks

Computes and visualises **Delta, Gamma, Vega, Theta** and **Rho** for each pricing method.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/MatheoTaudon/Pricer.git
cd Pricer

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

> The app will open at `http://localhost:8501`

---

## Usage

1. Select an option type in the sidebar
2. Enter market parameters (spot, strike, rate, volatility, maturity)
3. Choose a pricing method
4. Visualise the price and Greeks interactively

---

## Project Structure

```
Pricer/
├── app.py                      # Streamlit entry point
├── requirements.txt            # Python dependencies
├── models/
│   ├── option_models/          # Option class hierarchy
│   │   ├── option.py           # Base Option class
│   │   ├── vanilla_option.py
│   │   ├── asian_option.py
│   │   ├── barrier_option.py
│   │   ├── auto_call_option.py
│   │   ├── digits_option.py
│   │   ├── lookback_option.py
│   │   ├── quanto_option.py
│   │   ├── exotic_option.py
│   │   └── strategy.py
│   ├── pricing_method/         # Pricing engines
│   │   ├── black_scholes.py
│   │   ├── monte_carlo.py
│   │   └── binomial_tree.py
│   ├── greek_method/           # Greeks calculators
│   │   ├── black_scholes_greek.py
│   │   ├── monte_carlo_greek.py
│   │   └── binomial_tree_greek.py
│   └── plot_tools/             # Visualisations
│       ├── plotter.py
│       ├── plotter_with_smoothing.py
│       ├── plot_greeks.py
│       └── plot_pricing.py
└── pages/
    ├── pricer.py               # Main pricer page
    ├── source.py               # Methodology & sources
    └── profile.py              # Author profile
```

---

## Dependencies

| Package | Role |
|---------|------|
| `streamlit` | Web app framework |
| `numpy` | Numerical computations |
| `scipy` | Statistical functions (normal distribution) |
| `pandas` | Data manipulation |
| `plotly` | Interactive charts |
| `matplotlib` | Static charts |

---

## License

MIT
