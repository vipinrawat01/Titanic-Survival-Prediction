import streamlit as st
import pickle
import pandas as pd
from joblib import load

# Load the model from the file
model =load("titanic_survival_prediction_model.pkl")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)
# Function to make predictions
def predict_survival(pclass, sex):
    # Convert sex to binary
    sex = 1 if sex == 'male' else 0
    # Prepare the feature array
    features = pd.DataFrame({
    'Pclass': [pclass],
    'Sex': [sex]
})

    # Make prediction
    prediction = model.predict(features)
    return 'Survived' if prediction == 1 else 'Did not survive'

# Streamlit app
st.title("Titanic Survival Prediction")

st.write("Enter the details to predict whether the person survived or not:")

# User inputs
pclass = st.selectbox("Passenger Class (Pclass)", [1, 2, 3])
sex = st.selectbox("Sex", ['male', 'female'])

if st.button("Predict"):
    result = predict_survival(pclass, sex)
    st.write(f"The person {result}")
