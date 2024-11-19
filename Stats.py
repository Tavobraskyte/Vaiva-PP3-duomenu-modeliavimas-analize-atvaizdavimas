### Section 6: Stats
### Introduction:
# The data has been modified to contain some missing values, identified by NaN.
# Using pandas should make this exercise easier, in particular for the bonus question.
# You should be able to perform all of these operations without using a for loop or other looping construct.

# Step 1. Import the necessary libraries
import pandas as pd

# Step 2. Import the dataset from this address
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data"
data = pd.read_csv(url, sep=r'\s+', header=None)

# Step 3. Assign it to a variable called data and replace the first 3 columns by a proper datetime index.
data.columns = ['Yr', 'Mo', 'Dy', 'RPT', 'VAL', 'ROS', 'KIL', 'SHA', 'BIR', 'DUB', 'CLA', 'MUL', 'CLO', 'BEL', 'MAL']

# Ensure the Yr column is read as integers
data['Yr'] = data['Yr'].astype(dict)

# Fix the year if needed, e.g., converting 61 to 1961
data['Yr'] = data['Yr'].apply(lambda x: x + 1900 if x < 100 else x)

# Create a datetime index
data['Date'] = pd.to_datetime({'year': data['Yr'], 'month': data['Mo'], 'day': data['Dy']})
data.set_index('Date', inplace=True)

# Step 4. Compute how many values are missing for each location over the entire record.
missing_values = data.isna().sum()

# Step 5. Compute how many non-missing values there are in total.
non_missing_values = data.count()

# Step 6. Calculate the mean windspeed over all the locations and all the times.
# A single number for the entire dataset.
mean_windspeed = data.drop(['Yr', 'Mo', 'Dy'], axis=1).mean().mean()

# Step 7. Create a DataFrame called loc_stats to calculate min, max, mean windspeeds, and standard deviations
loc_stats = data.drop(['Yr', 'Mo', 'Dy'], axis=1).agg(['min', 'max', 'mean', 'std'])

# Step 8. Create a DataFrame called day_stats to calculate min, max, mean, and std for each day across all locations.
day_stats = data.drop(['Yr', 'Mo', 'Dy'], axis=1).agg(['min', 'max', 'mean', 'std'], axis=1)

# Step 9. Find the average windspeed in January for each location.
# Treat January 1961 and January 1962 both as January.
january_data = data[data.index.month == 1]
january_avg_wind = january_data.drop(['Yr', 'Mo', 'Dy'], axis=1).mean()

# Step 10. Downsample the record to a yearly frequency for each location.
yearly_data = data.drop(['Yr', 'Mo', 'Dy'], axis=1).resample('Y').mean()

# Step 11. Downsample the record to a monthly frequency for each location.
monthly_data = data.drop(['Yr', 'Mo', 'Dy'], axis=1).resample('M').mean()

# Step 12. Downsample the record to a weekly frequency for each location.
weekly_data = data.drop(['Yr', 'Mo', 'Dy'], axis=1).resample('W').mean()

# Step 13. Calculate the min, max, mean, and standard deviations of the windspeeds across all locations for each week.
# Assume that the first week starts on January 2, 1961.
weekly_stats = weekly_data.agg(['min', 'max', 'mean', 'std'])

# Step 14. Display results to verify correctness
print("Missing values per location:\n", missing_values)
print("\nNon-missing values per location:\n", non_missing_values)
print("\nOverall mean windspeed:\n", mean_windspeed)
print("\nLocation statistics:\n", loc_stats)
print("\nDaily statistics:\n", day_stats)
print("\nJanuary average windspeed per location:\n", january_avg_wind)
print("\nYearly data:\n", yearly_data.head())
print("\nMonthly data:\n", monthly_data.head())
print("\nWeekly data:\n", weekly_data.head())
print("\nWeekly statistics:\n", weekly_stats.head())

