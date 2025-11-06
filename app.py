import streamlit as st
import pickle
import numpy as np

# Load your trained model
model = pickle.load(open("loan_model.pkl", "rb"))

st.title("🏦 Loan Default Prediction App")

# Collect all required features (11 total)
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_emp = st.selectbox("Self Employed", ["Yes", "No"])
app_income = st.number_input("Applicant Income")
coapp_income = st.number_input("Coapplicant Income")
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Term (in days)")
credit_history = st.selectbox("Credit History", ["1 - Has Credit History", "0 - No Credit History"])
prop_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Encode inputs just like you did in preprocessing
input_data = np.array([[1 if gender == "Male" else 0,
                        1 if married == "Yes" else 0,
                        {"0": 0, "1": 1, "2": 2, "3+": 3}[dependents],
                        1 if education == "Graduate" else 0,
                        1 if self_emp == "Yes" else 0,
                        app_income,
                        coapp_income,
                        loan_amount,
                        loan_term,
                        1 if "Has" in credit_history else 0,
                        {"Urban": 2, "Semiurban": 1, "Rural": 0}[prop_area]]])

# Make prediction
if st.button("Predict"):
    result = model.predict(input_data)
    st.success("Loan Approved" if result[0] == 1 else "Loan Default Risk")
