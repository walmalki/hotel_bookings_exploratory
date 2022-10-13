import pandas as pd
from pandas_profiling import ProfileReport

df = pd.read_csv('hotel_bookings.csv')
profile = ProfileReport(df, title='Hotel Bookings | Data Analysis')
profile.to_file('index.html')