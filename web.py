import os # For file handling
import pickle # For loading the trained model
import streamlit as st # For creating the web application
from streamlit_option_menu import option_menu # For creating the option menu

st.set_page_config(page_title="Prediction of Disease Outbreaks", 
                   layout="wide",
                   page_icon=":rocket:")
diabetes_model = pickle.load(open('D:\AICTE Internship\Prediction of Disease Outbreaks\Training_Models\diabetes-prediction-model.sav', 'rb'))
heart_model = pickle.load(open('D:\AICTE Internship\Prediction of Disease Outbreaks\Training_Models\heart-prediction-model.sav', 'rb'))
parkinson_model = pickle.load(open('D:\AICTE Internship\Prediction of Disease Outbreaks\Training_Models\parkinsons-prediction-model.sav', 'rb'))

with st.sidebar:
    selected_option = option_menu("Prediction of disease outbreaks system", ["Diabetes Prediction", "Heart Prediction", "Parkinson Prediction"],
                                  menu_icon="hospital-fill", icons=[":syringe:", ":heart:", ":brain:"], default_index=0)
    
if selected_option == "Diabetes Prediction":
    st.title("Diabetes Prediction")
    col1, col2, = st.columns([3, 3])
    with col1:
        pregnancies = st.number_input("Pregnancies", 0, 20, 0)
        glucose = st.number_input("Glucose", 0, 200, 0)
        blood_pressure = st.number_input("Blood Pressure", 0, 200, 0)
        skin_thickness = st.number_input("Skin Thickness", 0, 100, 0)
    with col2:
        insulin = st.number_input("Insulin", 0, 1000, 0)
        bmi = st.number_input("BMI", 0.0, 100.0, 0.0)
        diabetes_pedigree_function = st.number_input("Diabetes Pedigree Function", 0.0, 2.0, 0.0)
        age = st.number_input("Age", 0, 100, 0)

if st.button("Predict"):
            prediction = diabetes_model.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])
            if prediction[0] == 1:
                st.error("You have diabetes")
            else:
                st.success("You don't have diabetes")

if selected_option == "Heart Prediction":
    st.title("Heart Prediction")
    col1, col2, = st.columns([3, 3])
    with col1:
        age = st.number_input("Age", 0, 100, 0)
        sex = st.number
        sex = st.selectbox("Sex", [0, 1])
        cp = st.number_input("Chest Pain types", 0, 3, 0)
        trestbps = st.number_input("Resting Blood Pressure", 0, 200, 0)
        chol = st.number_input("Serum Cholestoral in mg/dl", 0, 600, 0)
    with col2:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
        restecg = st.number_input("Resting Electrocardiographic results", 0, 2, 0)
        thalach = st.number_input("Maximum Heart Rate achieved", 0, 220, 0)
        exang = st.selectbox("Exercise Induced Angina", [0, 1])
        oldpeak = st.number_input("ST depression induced by exercise", 0.0, 10.0, 0.0)
        slope = st.number_input("Slope of the peak exercise ST segment", 0, 2, 0)
        ca = st.number_input("Major vessels colored by flourosopy", 0, 4, 0)
        thal = st.number_input("thal: 0 = normal; 1 = fixed defect; 2 = reversable defect", 0, 2, 0)

if st.button("Predict"):
    prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    if prediction[0] == 1:
        st.error("You have heart disease")
    else:
        st.success("You don't have heart disease")

if selected_option == "Parkinson Prediction":
    st.title("Parkinson Prediction")
    col1, col2, = st.columns([3, 3])
    with col1:
        fo = st.number_input("MDVP:Fo(Hz)", 0.0, 300.0, 0.0)
        fhi = st.number_input("MDVP:Fhi(Hz)", 0.0, 300.0, 0.0)
        flo = st.number_input("MDVP:Flo(Hz)", 0.0, 300.0, 0.0)
        jitter_percent = st.number_input("MDVP:Jitter(%)", 0.0, 1.0, 0.0)
        jitter_abs = st.number_input("MDVP:Jitter(Abs)", 0.0, 0.1, 0.0)
    with col2:
        rap = st.number_input("MDVP:RAP", 0.0, 1.0, 0.0)
        ppq = st.number_input("MDVP:PPQ", 0.0, 1.0, 0.0)
        ddp = st.number_input("Jitter:DDP", 0.0, 1.0, 0.0)
        shimmer = st.number_input("MDVP:Shimmer", 0.0, 1.0, 0.0)
        shimmer_db = st.number_input("MDVP:Shimmer(dB)", 0.0, 1.0, 0.0)
        nhr = st.number_input("NHR", 0.0, 1.0, 0.0)
        hnr = st.number_input("HNR", 0.0, 50.0, 0.0)

if st.button("Predict"):
    prediction = parkinson_model.predict([[fo, fhi, flo, jitter_percent, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, nhr, hnr]])
    if prediction[0] == 1:
        st.error("You have Parkinson's disease")
    else:
        st.success("You don't have Parkinson's disease")