import pandas as pd

data = {
    'artist': ['Artist A', 'Artist B', 'Artist A', 'Artist A', 'Artist B', 'Artist C', 'Artist A', 'Artist B'],
    'venue': ['Venue 1', 'Venue 1', 'Venue 2', 'Venue 1', 'Venue 2', 'Venue 1', 'Venue 1', 'Venue 1'],
    'concert_date': ['2023-01-15', '2023-01-20', '2023-02-15', '2023-03-05', '2023-03-20', '2023-03-25', '2023-04-01', '2023-04-10']
}

df = pd.DataFrame(data)
df['concert_date'] = pd.to_datetime(df['concert_date'])

df['year_month'] = df['concert_date'].dt.to_period('M')

concert_counts = df.groupby(['year_month', 'artist', 'venue']).size().reset_index(name='concert_count')

artists = df['artist'].unique()
venues = df['venue'].unique()

pairs = pd.MultiIndex.from_product([artists, venues], names=['artist', 'venue'])

pivot_df = concert_counts.pivot_table(index='year_month', columns=['artist', 'venue'], values='concert_count', fill_value=0)

pivot_df.columns = [f'{artist} - {venue}' for artist, venue in pivot_df.columns]

print(pivot_df)
