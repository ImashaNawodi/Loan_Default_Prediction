import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("loan_model.pkl", "rb"))

st.title("Loan Default Prediction")

# User inputs
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
app_income = st.number_input("Applicant Income")
coapp_income = st.number_input("Coapplicant Income")
loan_amount = st.number_input("Loan Amount")
loan_term = st.number_input("Loan Term")
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_emp = st.selectbox("Self Employed", ["Yes", "No"])
prop_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# Encode inputs
input_data = np.array([[1 if gender=="Male" else 0,
                        1 if married=="Yes" else 0,
                        app_income, coapp_income, loan_amount, loan_term,
                        1 if education=="Graduate" else 0,
                        1 if self_emp=="Yes" else 0,
                        {"Urban":2,"Semiurban":1,"Rural":0}[prop_area]]])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write("Loan Default" if prediction[0]==1 else "Loan Safe")
