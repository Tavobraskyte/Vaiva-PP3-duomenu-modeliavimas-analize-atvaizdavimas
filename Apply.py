## Section 4: Apply
### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv).
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv'
crime = pd.read_csv(url)

### Step 3. Assign it to a variable called crime.
crime.head()
### Step 4. What is the type of the columns?
print(crime.dtypes)
##### Have you noticed that the type of Year is int64. But pandas has a different type to work with Time Series. Let's see it now.
crime['Year'] = pd.to_datetime(crime['Year'], format='%Y')

### Step 5. Convert the type of the column Year to datetime64
crime.set_index('Year', inplace=True)

### Step 6. Set the Year column as the index of the dataframe
crime.set_index('Year', inplace=True)

### Step 7. Delete the Total column
crime.drop('Total', axis=1, inplace=True)

### Step 8. Group the year by decades and sum the values
crime['Decade'] = (crime.index.year // 10) * 10
crime_by_decade = crime.groupby('Decade').sum()
crime_by_decade

#### Pay attention to the Population column number, summing this column is a mistake
### Step 9. What is the most dangerous decade to live in the US?
dangerous_decade = crime_by_decade.sum(axis=1).idxmax()
print(f"The most dangerous decade to live in the US is the {dangerous_decade}s.")
