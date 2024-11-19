                                        #Grouping
## Section 2: Filtering and Sorting
### Step 1. Import the necessary libraries
pip install panda as pd

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv).
url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv'
euro12 = pd.read_csv(url)

### Step 3. Assign it to a variable called euro12.
### Step 4. Select only the Goal column.
goals_column = euro12['Goals']
print("Goals column:\n", goals_column)

### Step 5. How many team participated in the Euro2012?
num_teams = euro12['Team'].nunique()
print("Number of teams:", num_teams)

### Step 6. What is the number of columns in the dataset?
num_columns = euro12.shape[1]
print("Number of columns:", num_columns)
### Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro12[['Team', 'Yellow Cards', 'Red Cards']]
print("Discipline data:\n", discipline)

### Step 8. Sort the teams by Red Cards, then to Yellow Cards
sorted_teams = euro12.sort_values(by=['Red Cards', 'Yellow Cards'], ascending=[False, False])
print("Teams sorted by Red and Yellow Cards:\n", sorted_teams)

### Step 9. Calculate the mean Yellow Cards given per Team
mean_yellow_cards = euro12['Yellow Cards'].mean()
print("Mean Yellow Cards per team:", mean_yellow_cards)

### Step 10. Filter teams that scored more than 6 goals
teams_with_more_than_6_goals = euro12[euro12['Goals'] > 6]
print("Teams with more than 6 goals:\n", teams_with_more_than_6_goals)

### Step 11. Select the teams that start with G
teams_starting_with_G = euro12[euro12['Team'].str.startswith('G')]
print("Teams starting with G:\n", teams_starting_with_G)

### Step 12. Select the first 7 columns
first_7_columns = euro12.iloc[:, :7]
print("First 7 columns:\n", first_7_columns)

### Step 13. Select all columns except the last 3.
all_except_last_3 = euro12.iloc[:, :-3]
print("All columns except the last 3:\n", all_except_last_3)

### Step 14. Present only the Shooting Accuracy from England, Italy and Russia
shooting_accuracy = euro12[euro12['Team'].isin(['England', 'Italy', 'Russia'])]['Shooting Accuracy']
print("Shooting accuracy for England, Italy, and Russia:\n", shooting_accuracy)
