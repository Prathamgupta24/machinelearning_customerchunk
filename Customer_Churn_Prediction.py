import streamlit as st
import pickle
import numpy as np

# Load the ANN model
with open('ann_model.pkl', 'rb') as model_file:
   model = pickle.load(model_file)

# Define a function for making predictions
def predict(input_data):
    prediction = model.predict(input_data)
    return prediction

# Streamlit UI elements for user input
credit_score = st.number_input('Credit Score')
age = st.number_input('Age', min_value=18, max_value=100 )
tenure = st.slider('Tenure', min_value=0, max_value=10, step=1, value=5)
balance = st.number_input('Balance', value=0.0)
num_of_products = st.slider('Number of Products', min_value=1, max_value=4, step=1, value=1)
has_cr_card = st.checkbox('Has Credit Card')
is_active_member = st.checkbox('Is Active Member')
estimated_salary = st.number_input('Estimated Salary', value=0.0)
st.write("Select Your Geography")
geography_germany = st.checkbox('Germany')
geography_spain = st.checkbox('Spain')
geography_spain = st.checkbox('France')
st.write("Select Your Gender")
gender_male = st.checkbox('Male')
gender_female = st.checkbox('Female')

# Combine user inputs into an array for prediction
input_data = np.array([credit_score, age, tenure, balance, num_of_products, has_cr_card, is_active_member, estimated_salary,
                       geography_germany, geography_spain, gender_male])

if st.button('Predict'):
   prediction = predict(input_data.reshape(1, -1))  # Reshape input_data to match model's input shape
   st.write('Prediction:')
   if(prediction>=0.5):
      st.write('The Customer is leaving the Bank.')
   else: 
      st.write('The Customer is not leaving the Bank.')
         
