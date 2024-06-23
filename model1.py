import pickle
import streamlit as st

# Load your model
model1 = pickle.load(open("index.pkl", "rb"))

def myf1():
    st.title("Cancer Prediction")

    # Input fields
    age = st.slider("Age", 20, 80, step=1)  # Slider for age from 20 to 80

    # Dropdown for Gender
    gender_options = ["Male", "Female"]
    gender = st.selectbox("Gender", gender_options)
    gender_value = 1 if gender == "Female" else 0  # Convert gender to binary (0 for Male, 1 for Female)

    bmi = st.number_input("BMI (Body Mass Index)", 15.0, 40.0, step=0.1)  # BMI input ranging from 15.0 to 40.0

    # Dropdown for Smoking
    smoking_options = ["No", "Yes"]
    smoking = st.selectbox("Smoking Status", smoking_options)
    smoking_value = 1 if smoking == "Yes" else 0  # Convert smoking status to binary (0 for No, 1 for Yes)

    # Dropdown for Genetic Risk
    genetic_risk_options = ["Low", "Medium", "High"]
    genetic_risk = st.selectbox("Genetic Risk", genetic_risk_options)
    genetic_risk_value = genetic_risk_options.index(genetic_risk)  # Convert to categorical values (0, 1, 2)

    physical_activity = st.slider("Physical Activity (hours/week)", 0, 10, step=1)  # Slider for physical activity from 0 to 10 hours/week
    alcohol_intake = st.slider("Alcohol Intake (units/week)", 0, 5, step=1)  # Slider for alcohol intake from 0 to 5 units/week

    # Dropdown for Cancer History
    cancer_history_options = ["No", "Yes"]
    cancer_history = st.selectbox("Cancer History", cancer_history_options)
    cancer_history_value = 1 if cancer_history == "Yes" else 0  # Convert cancer history to binary (0 for No, 1 for Yes)

    # Button to predict
    pred = st.button("Predict Diagnosis")

    if pred:
        # Make prediction using the model
        prediction = model1.predict([[age, gender_value, bmi, smoking_value, genetic_risk_value, physical_activity, alcohol_intake, cancer_history_value]])

        # Display prediction result
        diagnosis = "Cancer" if prediction[0] == 1 else "No Cancer"
        st.write(f"Diagnosis: {diagnosis}")

# Run the app
if __name__ == "__main__":
    myf1()