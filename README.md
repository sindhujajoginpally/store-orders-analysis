# Store Orders Analysis (multi-table merge)

A pandas project analyzing order data split across two related tables — orders and customers — joined together for full analysis.

## What it does
- Cleans two separate messy datasets (orders, customers) independently
- Merges them on a shared `CustomerID` key to build a complete view of each order
- Calculates revenue by customer segment, by city, and identifies top customers by spend
- Cross-checks findings using both totals AND averages, to avoid misleading conclusions (e.g. one segment having higher total revenue simply because it has more customers, not higher spend per customer)

## Why I built it
Real business data is almost always split across multiple tables. This project practices the merge/join workflow that's central to most real analyst work, plus the analytical discipline of validating a finding before presenting it.

## How to run it
```bash
pip install pandas
python orders_analysis.py
```

## Key skills demonstrated
- `pd.merge()` for combining relational data
- `.groupby()` with both `.sum()` and `.mean()` to validate findings from multiple angles
- Structuring a multi-step analysis pipeline: clean → merge → calculate → analyze

## Sample insight
While Retail generated nearly double the total revenue of Wholesale, average order value was actually comparable between segments (~$394 vs ~$360) — showing the revenue gap was driven by customer count, not higher individual spend.
