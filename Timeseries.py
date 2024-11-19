                              #We are going to use Apple's stock price.

### Step 1. Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv)
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/09_Time_Series/Apple_Stock/appl_1980_2014.csv"
apple = pd.read_csv(url)

### Step 3. Assign it to a variable apple
apple.head()

### Step 4.  Check out the type of the columns
apple.dtypes

### Step 5. Transform the Date column as a datetime type
apple['Date'] = pd.to_datetime(apple['Date'])

### Step 6.  Set the date as the index
apple.set_index('Date', inplace=True)

### Step 7.  Is there any duplicate dates?
duplicate_dates = apple.index.duplicated().sum()

### Step 8.  Ops...it seems the index is from the most recent date. Make the first entry the oldest date.
apple.sort_index(inplace=True)
duplicate_dates = apple.index.duplicated().sum()

### Step 9. Get the last business day of each month
monthly_last_day = apple.resample('ME').last()

### Step 10.  What is the difference in days between the first day and the oldest
first_day = apple.index[0]
oldest_day = apple.index[-1]
date_diff = (first_day - oldest_day).days

### Step 11.  How many months in the data we have?
months_count = apple.resample('ME').count()
months_count.shape[0]

### Step 12. Plot the 'Adj Close' value. Set the size of the figure to 13.5 x 9 inches
apple['Adj Close'].plot(figsize=(13.5, 9))
plt.title('Apple Adjusted Close Price')
plt.show()
