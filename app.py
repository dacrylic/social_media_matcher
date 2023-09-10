from main import df_final, columns_to_compare
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load your DataFrame and select columns
df = df_final[columns_to_compare]

# Streamlit UI
st.title("Find a Makan Kaki")
st.write("Fill out your profile in the sidebar, and click submit to find your new friend!")

# User input section
st.sidebar.header("Tell us more about yourself!")
query = {}


query['names'] = st.sidebar.text_input("Enter a name:", "")

#-------------------------------------------------------------
#GPA qtn
#-------------------------------------------------------------

query['GPA'] = st.sidebar.slider(f"What is your GPA?", min_value=float(df['GPA'].min()), max_value=float(df['GPA'].max())
                               )

#-------------------------------------------------------------
#calorie count qtn
#-------------------------------------------------------------
option_to_value = {
    'I do not know how many calories I should consume': 1,
    'It is not at all important': 2,
    'It is moderately important': 3,
    'It is very important': 4
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("How important is counting the amount of calories consumed a day to you?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['calories_day'] = selected_option_value

#-------------------------------------------------------------
#coffee qtn
#-------------------------------------------------------------
option_to_value = {
    'I do not drink coffee': 0,
    'Creamy Frapuccino': 1,
    'A shot of Espresso': 2,

}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("What would be your preferred coffee order?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['coffee'] = selected_option_value


#-------------------------------------------------------------
#cook qtn
#-------------------------------------------------------------
option_to_value = {
    'Every day': 1,
    'A couple of times a week ': 2,
    'Whenever I can, but that is not very often  ': 3,
    'I only help a little during holidays ': 4,
    'Never, I really do not know my way around a kitchen': 5,
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("How often do you cook?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['cook'] = selected_option_value

#-------------------------------------------------------------
#cuisine qtn
#-------------------------------------------------------------
option_to_value = {
    'American': 1,
    'Mexican/Spanish': 2,
    'Korean/Asian': 3,
    'Indian': 4,
    'American inspired international dishes': 5,
    'Other': 6
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("What type of cuisine did you eat growing up?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['cuisine'] = selected_option_value

#-------------------------------------------------------------
#diet_current_coded qtn
#-------------------------------------------------------------
option_to_value = {
    'Healthy': 1,
    'Unhealthy': 2,
    'I always eat the same thing': 3,
    'I do not know': 4,
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("How would you describe your current diet?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['diet_current_coded'] = selected_option_value

#-------------------------------------------------------------
#eating_out qtn
#-------------------------------------------------------------
option_to_value = {
    'Never': 1,
    '1-2 times': 2,
    '2-3 times': 3,
    '3-5 times': 4,
    'Every day': 5,
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("How often do you eat out?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['eating_out'] = selected_option_value

#-------------------------------------------------------------
#employment qtn
#-------------------------------------------------------------
option_to_value = {
    'Yes, full time': 1,
    'Yes, part time': 2,
    'No': 3,
    'Other': 4,
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("Are you currently employed?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['employment'] = selected_option_value

#-------------------------------------------------------------
#ethnic food qtn
#-------------------------------------------------------------
option_to_value = {
    'Very unlikely': 1,
    'Unlikely': 2,
    'Neutral': 3,
    'Likely': 4,
    'Very likely': 4,
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("How likely are you to eat ethnic food?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['ethnic_food'] = selected_option_value

#-------------------------------------------------------------
#exercise qtn
#-------------------------------------------------------------
option_to_value = {
    'Every day': 1,
    'Twice or three times a week': 2,
    'Once a week': 3,
    'Sometimes': 4,
    'Never': 5,
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("How often do you exercise in a regular week?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['exercise'] = selected_option_value

#-------------------------------------------------------------
#fav_food qtn
#-------------------------------------------------------------
option_to_value = {
    'Cooked at home': 1,
    'Store bought': 2,
    'Both': 3,
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("If given the option, would you eat out or cook at home?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['fav_food'] = selected_option_value

#-------------------------------------------------------------
#fruit_day qtn
#-------------------------------------------------------------
option_to_value = {
    'Very unlikely': 1,
    'Unlikely': 2,
    'Neutral': 3,
    'Likely': 4,
    'Very likely': 4,
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("How likely are you to eat fruit in a regular day?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['fruit_day'] = selected_option_value

#-------------------------------------------------------------
#income qtn
#-------------------------------------------------------------
option_to_value = {
    'Less than $15,000': 1,
    '\$15,001 to $30,000': 2,
    '\$30,001 to $50,000': 3,
    '\$50,001 to $70,000': 4,
    '\$70,001 to $100,000': 5,
    'Higher than $100,000': 6,
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("What is your annual income?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['income'] = selected_option_value

#-------------------------------------------------------------
#marital_status qtn
#-------------------------------------------------------------
option_to_value = {
    'Single': 1,
    'In a relationship': 2,
    'Cohabiting': 3,
    'Married': 4,
    'Divorced': 5,
    'Widowed': 6,
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("What is your marital status?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['marital_status'] = selected_option_value

#-------------------------------------------------------------
#pay_meal_out qtn
#-------------------------------------------------------------
option_to_value = {
    'Up to $5.00': 1,
    '\$5.01 to $10.00': 2,
    '\$10.01 to $20.00': 3,
    '\$20.01 to $30.00': 4,
    '\$30.01 to $40.00': 5,
    'More than $40.01': 6,
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("How much would you pay for a meal out?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['pay_meal_out'] = selected_option_value

#-------------------------------------------------------------
#sports qtn
#-------------------------------------------------------------
option_to_value = {
    'Yes': 1,
    'No': 2,
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("Do you do any sporting activity?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['sports'] = selected_option_value

#-------------------------------------------------------------
#vitamins qtn
#-------------------------------------------------------------
option_to_value = {
    'Yes': 1,
    'No': 2,
}

# Use st.sidebar.radio to display the options and capture the user's choice
selected_option_text = st.sidebar.radio("Do you do take any supplements or vitamins?", list(option_to_value.keys()))

# Map the selected text option to the corresponding numeric value
selected_option_value = option_to_value[selected_option_text]

# Store the numeric value in the query dictionary
query['vitamins'] = selected_option_value

def map_gender(gender_code):
    if gender_code == 1:
        return "M"
    elif gender_code == 2:
        return "F"
    else:
        return "Unknown"


match_index = 0

# Add "Submit" button
def reset_session_state():
    session_state.closest_match_indices = []

# Create a session state object
session_state = st.session_state

# Add "Submit" button
if st.sidebar.button("Submit"):
    # Calculate cosine similarity between query and DataFrame
    query_df = pd.DataFrame([query], index=[0])  # Specify an index for the DataFrame
    cosine_similarities_query = cosine_similarity(query_df[columns_to_compare], df)

    # Find the indices of the closest matches
    indices_sorted_by_similarity = np.argsort(cosine_similarities_query[0])[::-1]
    print(indices_sorted_by_similarity)
    # Normalize cosine similarity scores between 0 and 1 for all matches
    min_score = cosine_similarities_query[0].min()
    max_score = cosine_similarities_query[0].max()
    normalized_scores = (cosine_similarities_query[0] - min_score) / (max_score - min_score)

    # Store the indices of the top 3 matches
    session_state.closest_match_indices = indices_sorted_by_similarity[:3]

    st.subheader("Top 3 Matches:")
    for index in session_state.closest_match_indices:
        st.write(f"**{df_final['names'].iloc[index]}**")
        st.write('Gender: ' + df_final['Gender'].apply(map_gender).iloc[index])
        try:
            st.write('Comfort Foods: ' + df_final['comfort_food'].iloc[index])
        except:
            st.write('Comfort Foods: NA')
        st.write(f"Match score: {cosine_similarities_query[0][index] * 100:.2f}%")  # Print the raw cosine similarity scor

# Reset session state variables when the app starts
if 'closest_match_indices' not in session_state:
    reset_session_state()

