import numpy as np
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from faker import Faker
import random


df = pd.read_csv("datasets/food_coded.csv")
df_og = df.copy()

#NAME GENERATOR
seed_value = 69
faker_seed = 69
random.seed(seed_value)

fake = Faker()
Faker.seed(faker_seed)

def generate_gender_names(row):
    if row['Gender'] == 1:
        return fake.first_name_male()
    elif row['Gender'] == 2:
        return fake.first_name_female()
    else:
        return None

def split_and_clean(value):
    value = value.replace('.', '')  # Remove full stops
    values = [v.strip() for v in re.split(r'[,/]', value)]  # Split by comma or slash and remove leading/trailing whitespace
    return values


def remove_non_numeric(cell):
    if isinstance(cell, str):
        # Remove non-numeric characters and retain decimal points
        numeric_chars = ''.join(filter(lambda x: x.isdigit() or x == '.', cell))

        # Check if the resulting string is empty, and return NaN if it is
        return float(numeric_chars) if numeric_chars else np.nan
    return cell


# Set pandas display options to show all columns and rows
pd.set_option('display.max_columns', None)  # Show all columns

df = df[['GPA', 'Gender', 'calories_day', 'coffee', 'cook', 'cuisine', 'diet_current_coded', 'eating_out', 'employment', 'ethnic_food', 'exercise', 'fav_food', 'fruit_day', 'income', 'marital_status', 'pay_meal_out', 'sports', 'vitamins']]

df = df.applymap(remove_non_numeric)


df.fillna(0, inplace=True)

columns_to_compare = ['GPA', 'calories_day', 'coffee', 'cook', 'cuisine', 'diet_current_coded', 'eating_out', 'employment', 'ethnic_food', 'exercise', 'fav_food', 'fruit_day', 'income', 'marital_status', 'pay_meal_out', 'sports', 'vitamins']

df['names'] = df.apply(generate_gender_names, axis=1)


df_final = df

columns_to_convert= []

for col in df_final:
    if df_final[col].dtype == 'float64':
        non_integer_values = df_final[~df_final[col].apply(lambda x: x.is_integer())][col]
        if non_integer_values.empty:
            columns_to_convert.append(col)
        else:
            print(f"Column '{col}' contains non-integer values: {non_integer_values}")

df_final[columns_to_convert] = df_final[columns_to_convert].astype(int)

df_final['comfort_food'] = df_og['comfort_food']

print(columns_to_convert)
print(df_final.info())