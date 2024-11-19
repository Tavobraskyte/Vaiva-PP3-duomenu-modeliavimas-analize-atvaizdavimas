## Section 8: Creating Series and DataFrames
### Introduction:

                           #This time you will create the data.

### Step 1. Import the necessary libraries
import pandas as pd

### Step 2. Create a data dictionary that looks like the DataFrame below
data = {
    'name': ['Pikachu', 'Charmander', 'Bulbasaur'],
    'type': ['Electric', 'Fire', 'Grass'],
    'hp': [35, 39, 45],
    'evolution': ['Raichu', 'Charizard', 'Ivysaur'],
    'pokedex': [25, 4, 1]
}
pokemon = pd.DataFrame(data)

### Step 3. Assign it to a variable called pokemon
pokemon.head()

### Step 4. Ops...it seems the DataFrame columns are in alphabetical order. Place  the order of the columns as name, type, hp, evolution, pokedex
pokemon = pokemon[['name', 'type', 'hp', 'evolution', 'pokedex']]

### Step 5. Add another column called place, and insert what you have in mind.
pokemon['place'] = ['Kanto', 'Kanto', 'Kanto']

### Step 6. Present the type of each column
pokemon.dtypes

### BONUS: Create your own question and answer it.
## Section: 9 Time Series
# Example: What is the most common type of Pokemon?
most_common_type = pokemon['type'].value_counts().idxmax()
print(f"The most common Pokemon type is: {most_common_type}")


