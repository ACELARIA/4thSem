import pandas as pd

asking_prices = pd.Series([1000, 2200, 1600, 500, 1700, 2900, 2600])
fair_prices = pd.Series([1300, 2100, 1700, 700, 2000, 2600, 2800])

good_deals = asking_prices[asking_prices < fair_prices]

good_deal_indices = good_deals.index.tolist()

print("Indices of good deals:", good_deal_indices)
