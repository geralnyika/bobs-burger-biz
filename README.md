# Bob's Burger Biz: Restaurant Analytics
The fictional *Bob's Burgers* restaurant is treated as a real business in this data science project, which uses data analysis to provide answers to the questions that would truly determine whether Bob makes a profit.

## Why This Project
Portfolio datasets are typically generic. With three business questions, three analyses, and three practical recommendations—structured like a true consulting engagement. This project applies true analytical rigor to a creative brief.

## Analyses

### P1: Menu Performance Analysis
**Question:** Which burgers should become permanent menu fixtures?

- Cleaned and standardised raw menu data
- Analysed performance across specials and categories
- **Finding:** Burgers with witty names outperformed others by ~20% on average. Conclusion: brand personality drives sales



![Top Burgers by Units](figures/01_top_burgers_by_units_aggregated.png)




![Top Burgers by Revenue](figures/02_top_burgers_by_revenue.png)




![Pun vs Units](figures/03_pun_vs_units_aggregated.png)



### P2: Customer Behaviour Analysis
**Question:** Who are Bob's customers, and what drives their visits?

- Cleaned survey and visit data (200 entries)
- Computed descriptive statistics: mean, median, quartiles for visit frequency
- Conducted segment-level analysis across families, singles, regulars, and casuals
- **Finding:** Families and regulars form the stable core; attracting younger singles represents the clearest growth opportunity

### P3: Pricing & Profitability Analysis
**Question:** Are menu prices sustainable, and where is Bob losing money?

- Cleaned inconsistent cost, price, and margin data
- Corrected mismatched profit margin calculations
- **Finding:** Several high-popularity items are underpriced. Margin improvement is possible without customer loss


## Tech Stack
| Category | Tools |
|---|---|
| Data manipulation | Pandas, NumPy |
| Visualisation | Matplotlib / Seaborn |
| Environment | Jupyter Notebook |
