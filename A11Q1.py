import pandas as pd

date_time_obj_1 = pd.to_datetime('2012-01-15')
print(f"Date time object for Jan 15 2012: {date_time_obj_1}")

date_time_obj_2 = pd.to_datetime('2012-01-15 21:20')
print(f"Specific date and time of 9:20 pm: {date_time_obj_2}")

local_date_time = pd.to_datetime('now')
print(f"Local date and time: {local_date_time}")

date_without_time = pd.to_datetime('2012-01-15').date()
print(f"A date without time: {date_without_time}")

current_date = pd.to_datetime('now').date()
print(f"Current date: {current_date}")

time_from_date_time = pd.to_datetime('2012-01-15 21:20').time()
print(f"Time from a date time: {time_from_date_time}")

current_local_time = pd.to_datetime('now').time()
print(f"Current local time: {current_local_time}")
