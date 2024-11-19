import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set up logging to write to a file
logging.basicConfig(filename='intermediate_results.log', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(message)s')

def log_print(message):
    """Function to log intermediate results to a file."""
    logging.info(message)
    print(message)  # Also print to console for real-time viewing

# Section 4: Apply

# Step 1. Import the necessary libraries
log_print("Importing pandas...")
import pandas as pd

# Step 2. Import the dataset
log_print("Importing the dataset...")
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"
crime = pd.read_csv(url)
log_print(f"Dataset loaded. Here are the first few rows:\n{crime.head()}")

# Step 3. Assign it to a variable called crime
log_print(f"Dataset info: {crime.info()}")

# Step 4. What is the type of the columns?
log_print(f"Column types: {crime.dtypes}")

# Step 5. Convert the type of the column Year to datetime64
crime['Year'] = pd.to_datetime(crime['Year'], format='%Y')
log_print(f"Data types after conversion: {crime.dtypes}")

# Step 6. Set the Year column as the index of the dataframe
crime.set_index('Year', inplace=True)
log_print(f"Dataset with Year as index:\n{crime.head()}")

# Step 7. Delete the Total column
crime.drop('Total', axis=1, inplace=True)
log_print(f"Dataset after dropping 'Total' column:\n{crime.head()}")

# Step 8. Group the year by decades and sum the values
crime['Decade'] = (crime.index.year // 10) * 10
crime_by_decade = crime.groupby('Decade').sum()
log_print(f"Grouped by decade:\n{crime_by_decade}")

# Step 9. What is the most dangerous decade to live in the US?
dangerous_decade = crime_by_decade.sum(axis=1).idxmax()
log_print(f"The most dangerous decade to live in the US is the {dangerous_decade}s.")

# Section 5: Merge

# Step 1. Import the necessary libraries
log_print("Importing pandas for merging...")
import pandas as pd

# Step 2. Create the 3 DataFrames based on the following raw data
raw_data_1 = {
    'subject_id': ['1', '2', '3', '4', '5'],
    'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
    'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']
}
raw_data_2 = {
    'subject_id': ['4', '5', '6', '7', '8'],
    'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
    'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']
}
raw_data_3 = {
    'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
    'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]
}
data1 = pd.DataFrame(raw_data_1)
data2 = pd.DataFrame(raw_data_2)
data3 = pd.DataFrame(raw_data_3)

log_print(f"DataFrames created:\n{data1}\n{data2}\n{data3}")

# Step 3. Assign each to a variable called data1, data2, data3
log_print(f"Assigned variables: data1, data2, data3")

# Step 4. Join the two dataframes along rows and assign to all_data
all_data = pd.concat([data1, data2], ignore_index=True)
log_print(f"All data concatenated along rows:\n{all_data}")

# Step 5. Join the two dataframes along columns and assign to all_data_col
all_data_col = pd.concat([data1, data2], axis=1)
log_print(f"All data concatenated along columns:\n{all_data_col}")

# Step 6. Print data3
log_print(f"Data3:\n{data3}")

# Step 7. Merge all_data and data3 along the subject_id value
merged_data = pd.merge(all_data, data3, on='subject_id')
log_print(f"Merged all_data and data3 on 'subject_id':\n{merged_data}")

# Step 8. Merge only the data that has the same 'subject_id' on both data1 and data2
merged_data_common = pd.merge(data1, data2, on='subject_id')
log_print(f"Merged data1 and data2 on common 'subject_id':\n{merged_data_common}")

# Step 9. Merge all values in data1 and data2, with matching records from both sides where available
full_merge = pd.merge(data1, data2, on='subject_id', how='outer')
log_print(f"Full merge of data1 and data2 (outer join):\n{full_merge}")

# Section 6: Stats

# Step 1. Import the necessary libraries
log_print("Importing pandas for stats...")
import pandas as pd

# Step 2. Import the dataset
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/Wind_Stats/wind.data"
data = pd.read_csv(url, delim_whitespace=True, header=None)
log_print(f"Wind dataset loaded. Here are the first few rows:\n{data.head()}")

# Step 3. Assign it to a variable called data and replace the first 3 columns by a proper datetime index
data.columns = ['Yr', 'Mo', 'Dy', 'RPT', 'VAL', 'ROS', 'KIL', 'SHA', 'BIR', 'DUB', 'CLA', 'MUL', 'CLO', 'BEL', 'MAL']
data['Date'] = pd.to_datetime(data[['2024', '11', '18']])
data.set_index('Date', inplace=True)
log_print(f"Dataset with datetime index:\n{data.head()}")

# Step 4. Year 2061? Do we really have data from this year? Create a function to fix it and apply it.
def fix_year(row):
    if row['Yr'] == 61:
        row['Yr'] = 1961
    elif row['Yr'] == 62:
        row['Yr'] = 1962
    return row

data = data.apply(fix_year, axis=1)
log_print(f"Year data fixed:\n{data.head()}")

# Step 5. Set the right dates as the index
data.index = pd.to_datetime(data.index)
log_print(f"Corrected Date index:\n{data.head()}")

# Step 6. Compute how many values are missing for each location over the entire record
missing_values = data.isna().sum()
log_print(f"Missing values in each column:\n{missing_values}")

# Step 7. Compute how many non-missing values there are in total
non_missing_values = data.count()
log_print(f"Non-missing values in each column:\n{non_missing_values}")

# Step 8. Calculate the mean wind speeds across all locations
mean_windspeed = data.drop(['Yr', 'Mo', 'Dy'], axis=1).mean().mean()
log_print(f"Mean wind speed: {mean_windspeed}")

# Step 9. Create a DataFrame called loc_stats with min, max, mean, and std of wind speeds at each location
loc_stats = data.drop(['Yr', 'Mo', 'Dy'], axis=1).agg(['min', 'max', 'mean', 'std'])
log_print(f"Location stats:\n{loc_stats}")

# Step 10. Create a DataFrame called day_stats with min, max, mean, and std across all locations at each day
day_stats = data.agg(['min', 'max', 'mean', 'std'], axis=1)
log_print(f"Daily stats:\n{day_stats}")

# Section 7: Visualization

# Example visualizationa
titanic = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv")
titanic.set_index('PassengerId', inplace=True)

# Create a pie chart presenting the male/female proportion
gender_counts = titanic['Sex'].value_counts()
gender_counts.plot.pie(autopct='%1.1f%%')
plt.title('Male/Female Proportion')
plt.ylabel('')
plt.show()
