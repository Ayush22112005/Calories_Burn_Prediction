import streamlit as st
import pickle
import pandas as pd

model = pickle.load(
    open("calories_model.pkl", "rb")
)

st.title("Calories Burn Prediction App")

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100
)

height = st.number_input("Height (cm)")
weight = st.number_input("Weight (kg)")
duration = st.number_input("Workout Duration (min)")
heart_rate = st.number_input("Heart Rate (bpm)", min_value=60, max_value=150, value=95)
body_temp = st.number_input("Body Temperature (°C)", min_value=35.0, max_value=42.0, value=40.0)


gender = 0 if gender == "Male" else 1

if st.button("Predict Calories"):

    input_data = pd.DataFrame(
        [[
            gender,
            age,
            height,
            weight,
            duration,
            heart_rate,
            body_temp
        ]],
        columns=[
            "Gender",
            "Age",
            "Height",
            "Weight",
            "Duration",
            "Heart_Rate",
            "Body_Temp"
        ]
    )

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Calories Burned: {prediction[0]:.2f}"
    )