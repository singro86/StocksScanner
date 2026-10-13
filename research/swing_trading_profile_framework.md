# Automated Catalyst & Trend Swing Trading Strategy

This document outlines the end-to-end framework for a short-term swing trading profile. It combines real-time news tracking, technical trend filters, and automated mathematical exit boundaries to buy and hold momentum stocks for 2 to 5 days.

---

## 🔎 Profile Architecture: Tools & Live Data Links

To build an actionable trading profile, your environment must integrate zero-lag data aggregators, screening infrastructure, and programmatic brokers.

### 1. High-Speed News & Sentiment Feeds
*   **Institutional Catalyst Tracking**: Use [Benzinga Pro](https://www.benzinga.com/go/benzinga-pro) for lightning-fast news squawks, corporate breaking headlines, and immediate sentiment indicators.
*   **Real-Time Macro Audio**: Monitor global economic indicators and geopolitical alerts via [Newsquawk Audio Commentary](https://newsquawk.com/).
*   **Retail Sentiment Monitoring**: Track breaking viral trends, high-volume retail stock discussion, and retail momentum pools using [Stocktwits Rooms](https://stocktwits.com/).

### 2. Charting & Trend Scanners
*   **Technical Scanning Infrastructure**: Set up multi-interval trend analysis (1D and 4H charts) using [TradingView Scanners](https://www.tradingview.com/).
*   **Real-Time Volatility Tracking**: Monitor sudden price disruptions and immediate catalyst price action over baseline averages using [StockAlarm Alerts](https://stockalarm.io/).

### 3. Execution & Bracket Order Brokers
*   **Advanced Order Routing**: Execute multi-legged bracket orders seamlessly via [Interactive Brokers (IBKR)](https://www.interactivebrokers.com/).

---

## 📈 Stock Selection Strategy: Screening for Today's Growth

To identify, evaluate, and suggest viable ticker targets based on today's explosive market movements, you must apply a strict, rule-based quantitative filter.

```
[Pre-Market Scanner] ➡️ [Catalyst Verification] ➡️ [Volume Filter] ➡️ [Trend Alignment]
```

### Step 1: Configure the Daily Momentum Scanner
Every morning before or exactly at the market open, run a scanner on [TradingView](https://www.tradingview.com/) filtered with the following constraints:
*   **Pre-Market / Today's Change**: Greater than **+3.0%** (Identifies early alpha relative to the index).
*   **Relative Volume (RVOL)**: Greater than **2.5** (Ensures the stock is trading at 2.5x its normal volume, indicating massive institutional participation).
*   **Market Capitalization**: Between **$1 Billion and $50 Billion** (Avoids highly illiquid micro-caps while retaining high volatility potential).
*   **Average True Range (ATR)**: Greater than **$1.50** (Guarantees sufficient daily price movement to hit short-term targets).

### Step 2: Cross-Reference with the News Catalyst
A stock showing high growth without a reason is dangerous. Ensure the ticker's daily gain is backed by one of these specific events on [Benzinga Pro](https://www.benzinga.com/go/benzinga-pro):
1.  **Forward Guidance Hikes**: Executive outlook exceeding consensus Wall Street estimates.
2.  **Regulatory Clearance**: Landmark FDA approvals, patent grants, or major cross-border commercial licensing.
3.  **Large-Scale Contract Awards**: Corporate or government contract announcements valued over 10% of the company's total annual revenue.

### Step 3: Validate Trend Continuity
Never buy a stock that has extended too far from its baseline. Check the 4-Hour (4H) technical chart for these specific parameters:
*   **Exponential Moving Average (EMA)**: The current price must sit firmly above a rising 9-period EMA.
*   **Relative Strength Index (RSI)**: The RSI must be between **55 and 68**. An RSI over 70 indicates an overbought stock likely to experience an immediate multi-day pullback.

---

## 💡 Automated Trade Execution Blueprint

Once a stock is suggested and selected, the trade profile must automate the exit boundaries immediately upon execution to mitigate human emotional bias.

### The Mathematics of a Bracket Order
Every trade must maintain a strict risk-to-reward architecture, aiming for a **1:2 or 1:3 ratio**. If you target a specific percentage gain, your stop-loss must be proportionally tighter to guarantee capital survival.

| Strategy Layer | Parameter Type | Execution Metric | Operational Rule |
| :--- | :--- | :--- | :--- |
| **Entry Point** | Limit Order | Post-Consolidation High | Enter only when the stock breaks above its initial 15-minute high. |
| **Profit Ceiling** | Take-Profit Limit | **+6.0% to +8.0%** | Automatically triggers a sale when your targeted return threshold is hit. |
| **Risk Floor** | Stop-Loss Order | **-2.0% to -3.0%** | Hard structural stop located exactly below the daily chart's 9-EMA line. |

---

## ⚠️ Tactical Guardrails & Risk Management

1.  **The Overnight Gap Risk**: Keeping concentrated stock positions active over multiple days introduces severe overnight volatility. Limit your exposure so that no individual trade accounts for more than **5% to 10% of your total liquid capital**.
2.  **The "Sell the News" Trap**: When an event is highly anticipated (e.g., a planned product launch date), the stock typically rallies *before* the event. The day the news officially breaks, early investors liquidate positions to secure profits, driving prices down. Trade the news **after** an unpredicted structural surprise hits.
3.  **Strict Strategy Discipline**: If a stock breaks down below its 20-day Simple Moving Average (SMA) on the daily chart, the upward momentum has completely failed. Liquidate the trade instantly; never convert a broken 3-day swing trade into a multi-month forced investment out of hope.