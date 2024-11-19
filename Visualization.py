## Section 7: Visualization
### Introduction:

#This exercise is based on the titanic Disaster dataset avaiable at [Kaggle](https://www.kaggle.com/c/titanic).
#To know more about the variables check [here](https://www.kaggle.com/c/titanic/data)


### Step 1. Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

### Step 2. Import the dataset from this [address](https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv)
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/07_Visualization/Titanic_Desaster/train.csv"
titanic = pd.read_csv(url)

### Step 3. Assign it to a variable titanic
titanic.head()

### Step 4. Set PassengerId as the index
titanic.set_index('PassengerId', inplace=True)

### Step 5. Create a pie chart presenting the male/female proportion
gender_counts = titanic['Sex'].value_counts()
gender_counts.plot.pie(autopct='%1.1f%%')
plt.title('Male/Female Proportion')
plt.ylabel('')
plt.show()

### Step 6. Create a scatterplot with the Fare payed and the Age, differ the plot color by gender
plt.scatter(titanic['Fare'], titanic['Age'], c=titanic['Sex'].map({'male': 'blue', 'female': 'red'}))
plt.xlabel('Fare')
plt.ylabel('Age')
plt.title('Fare vs Age colored by Gender')
plt.show()

### Step 7. How many people survived?
survival_count = titanic['Survived'].sum()
print(f"Number of survivors: {survival_count}")

### Step 8. Create a histogram with the Fare payed
titanic['Fare'].hist(bins=20)
plt.title('Histogram of Fare')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

### BONUS: Create your own question and answer it.

## Section 8: Creating Series and DataFrames
# Example: What is the average age of survivors?
average_age_survived = titanic[titanic['Survived'] == 1]['Age'].mean()
print(f"Average age of survivors: {average_age_survived}")
