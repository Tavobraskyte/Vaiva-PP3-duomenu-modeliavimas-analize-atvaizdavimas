                               ## Section 10: Deleting
### Introduction: This exercise is a adaptation from the UCI Wine dataset. The only pupose is to practice deleting data with pandas.

### Step 1. Import the necessary libraries
import pandas as pd
import numpy as np

### Step 2. Import the dataset from this [address](https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data).
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine = pd.read_csv(url, header=None)

### Step 3. Assign it to a variable called wine
wine.head()

### Step 4. Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns
wine.drop([0, 3, 6, 8, 10, 12, 13], axis=1, inplace=True)

### Step 5. Assign the columns as below:
wine.columns = ['alcohol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 'flavonoids', 'proanthocyanins', 'hue']

### Step 6. Set the values of the first 3 rows from alcohol as NaN
wine.loc[0:2, 'alcohol'] = np.nan

### Step 7. Now set the value of the rows 3 and 4 of magnesium as NaN
wine['alcohol'].fillna(10, inplace=True)
wine['magnesium'].fillna(100, inplace=True)

### Step 8. Fill the value of NaN with the number 10 in alcohol and 100 in magnesium
wine['alcohol'].fillna(10, inplace=True)
wine['magnesium'].fillna(100, inplace=True)

### Step 9. Count the number of missing values
missing_values_count = wine.isna().sum()

### Step 10.  Create an array of 10 random numbers up until 10
import numpy as np
random_indices = np.random.randint(0, wine.shape[0], size=10)

### Step 11.  Use random numbers you generated as an index and assign NaN value to each of cell.
wine.loc[random_indices] = np.nan

### Step 12.  How many missing values do we have?
missing_values_after = wine.isna().sum()

### Step 13. Delete the rows that contain missing values
wine_clean = wine.dropna()

### Step 14. Print only the non-null values in alcohol
print(wine_clean['alcohol'])

### Step 15.  Reset the index, so it starts with 0 again
wine_clean.reset_index(drop=True, inplace=True)
