import pandas as pd

data = {
    'day': ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7', 'Day 8', 'Day 9', 'Day 10'],
    'john': [1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    'judy': [1, 0, 0, 1, 0, 0, 0, 1, 0, 0]
}

df = pd.DataFrame(data)

def calculate_days_til_party(df):
    df['days_til_party'] = None

    next_party_day = None

    for i in range(len(df) - 1, -1, -1):
        if df.at[i, 'john'] == 1 and df.at[i, 'judy'] == 1:
            df.at[i, 'days_til_party'] = 0
            next_party_day = i  
        elif next_party_day is not None:
            df.at[i, 'days_til_party'] = next_party_day - i
    
    return df

df = calculate_days_til_party(df)

print(df[['day', 'john', 'judy', 'days_til_party']])
