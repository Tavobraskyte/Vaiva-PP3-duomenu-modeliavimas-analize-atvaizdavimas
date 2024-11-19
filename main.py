import pandas as pd

# Step 2 and 3
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users = pd.read_csv(url, sep='|', index_col='user_id')
# Step 4
users.head(25)

# Step 5
users.tail(10)

# Step 6
num_observations = users.shape[0]

# Step 7
num_columns = users.shape[1]

# Step 8
column_names = users.columns.tolist()

# Step 9
index_info = users.index

# Step 10
data_types = users.dtypes

# Step 11
occupation_column = users['occupation']

# Step 12
num_unique_occupations = users['occupation'].nunique()

# Step 13
most_frequent_occupation = users['occupation'].value_counts().idxmax()

# Step 14
summary = users.describe(include='all')

# Step 15
summary_all_columns = users.describe()

# Step 16
occupation_summary = users['occupation'].describe()

# Step 17
mean_age = users['age'].mean()

# Step 18
least_occurrence_age = users['age'].value_counts().idxmin()
