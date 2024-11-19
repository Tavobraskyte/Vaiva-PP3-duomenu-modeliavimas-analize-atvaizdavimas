                                 ## Section 3: Grouping
### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv).
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv'
drinks = pd.read_csv(url)

### Step 3. Assign it to a variable called drinks.
### Step 4. Which continent drinks more beer on average?
avg_beer_by_continent = drinks.groupby('continent')['beer_servings'].mean()
print("Average beer consumption by continent:\n", avg_beer_by_continent)

### Step 5. For each continent print the statistics for wine consumption.
wine_stats_by_continent = drinks.groupby('continent')['wine_servings'].describe()
print("Wine consumption statistics by continent:\n", wine_stats_by_continent)

### Step 6. Print the mean alcohol consumption per continent for every column
mean_alcohol_by_continent = drinks.groupby('continent').mean()
print("Mean alcohol consumption per continent:\n", mean_alcohol_by_continent)

### Step 7. Print the median alcohol consumption per continent for every column
median_alcohol_by_continent = drinks.groupby('continent').median()
print("Median alcohol consumption per continent:\n", median_alcohol_by_continent)

### Step 8. Print the mean, min and max values for spirit consumption.
spirit_stats = drinks.groupby('continent')['spirit_servings'].agg(['mean', 'min', 'max'])
print("Spirit consumption statistics:\n", spirit_stats)
