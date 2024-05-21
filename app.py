import streamlit as st
import pandas as pd
import joblib
import base64

# Load the trained XGBoost model
model = joblib.load("D:/Jerushaa/AML/xgb_model.pkl")

# Function to preprocess input data
def preprocess_input(data):
    # Remove outliers
    data.drop(data[(data['height'] > data['height'].quantile(0.975)) | (data['height'] < data['height'].quantile(0.025))].index, inplace=True)
    data.drop(data[(data['weight'] > data['weight'].quantile(0.975)) | (data['weight'] < data['weight'].quantile(0.025))].index, inplace=True)
    data.drop(data[(data['ap_hi'] > data['ap_hi'].quantile(0.975)) | (data['ap_hi'] < data['ap_hi'].quantile(0.025))].index, inplace=True)
    data.drop(data[(data['ap_lo'] > data['ap_lo'].quantile(0.975)) | (data['ap_lo'] < data['ap_lo'].quantile(0.025))].index, inplace=True)

    return data

# Function to make predictions
def predict(data):
    # Preprocess the input data
    processed_data = preprocess_input(data)
    # Make predictions
    predictions = model.predict(processed_data)
    return predictions

# Function to set background image
def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: black;  /* Font color */
        }}
        .stTextInput > div > div > input[type="text"], 
        .stNumberInput > div > div > input[type="number"], 
        .stSelectbox > div > div > div > div > div > div > div > div > div {{
            color: black !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Streamlit app
def main():
    set_background("D:/Jerushaa/AML/bg.jpg")

    st.title("Cardiovascular Disease Prediction")
    st.write(
        "This app predicts the presence or absence of cardiovascular disease based on input features."
    )

    # Add input fields for user to enter data
    with st.form("user_input_form"):
        st.write("Please fill out the following information:")
        age = st.slider("Age (in years)", 10, 100)
        height = st.slider("Height (in cm)", 100, 250)
        weight = st.slider("Weight (in kg)", 30, 200)
        ap_hi = st.slider("Systolic blood pressure (mmHg)", 60, 250)
        ap_lo = st.slider("Diastolic blood pressure (mmHg)", 40, 150)
        cholesterol = st.selectbox("Cholesterol level", ["Normal", "Above Normal", "Well Above Normal"])
        gluc = st.selectbox("Glucose level", ["Normal", "Above Normal", "Well Above Normal"])
        smoke = st.selectbox("Smoking status", ["Non-smoker", "Smoker"])
        alco = st.selectbox("Alcohol consumption status", ["Non-drinker", "Drinker"])
        active = st.selectbox("Physical activity level", ["Inactive", "Active"])

        submit_button = st.form_submit_button("Predict")

    # Convert categorical inputs to numerical values
    cholesterol_map = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}
    gluc_map = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}
    smoke = 1 if smoke == "Smoker" else 0
    alco = 1 if alco == "Drinker" else 0
    active = 1 if active == "Active" else 0

    # Create a dictionary with user input
    user_data = {
        "age": age,
        "height": height,
        "weight": weight,
        "ap_hi": ap_hi,
        "ap_lo": ap_lo,
        "cholesterol": cholesterol_map[cholesterol],
        "gluc": gluc_map[gluc],
        "smoke": smoke,
        "alco": alco,
        "active": active
    }

    # Convert the dictionary to a DataFrame
    input_df = pd.DataFrame([user_data])

    # Make predictions
    if submit_button:
        prediction = predict(input_df)
        if prediction[0] == 0:
            st.write("Prediction: No cardiovascular disease")
        else:
            st.write("Prediction: Cardiovascular disease present")

if __name__ == "__main__":
    main()
