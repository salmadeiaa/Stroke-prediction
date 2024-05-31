import streamlit as st 
import pickle
import pandas as pd


st.title('Stroke Prediction app')
st.info('Application for Stroke Predection')
st.sidebar.header('Feature Selection')

age=st.text_input('age')
hypertension=st.text_input('hypertension')
heart_disease=st.text_input('heart_disease')
avg_glucose_level=st.text_input('avg_glucose_level')
bmi=st.text_input('bmi')
gender_Male=st.text_input('gender_Male')
gender_Other=st.text_input('gender_Other')
ever_married_Yes=st.text_input('ever_married_Yes')
work_type_Never_worked=st.text_input('work_type_Never_worked')
work_type_Private=st.text_input('work_type_Private')
work_type_Selfemployed=st.text_input('work_type_Self-employed')
work_type_children=st.text_input('work_type_children')
Residence_type_Urban=st.text_input('Residence_type_Urban')
smoking_status_formerlysmoked=st.text_input('smoking_status_formerly smoked')
smoking_status_neversmoked=st.text_input('smoking_status_never smoked')
smoking_status_smokes=st.text_input('smoking_status_smokes')



df=pd.DataFrame({'age':[age],
'hypertension':[hypertension], 'heart_disease':[heart_disease],'avg_glucose_level':[avg_glucose_level],'bmi':[bmi],
'gender_Male':[gender_Male],'gender_Other':[gender_Other],'ever_married_Yes':[ever_married_Yes],'work_type_Never_worked':[work_type_Never_worked],
'work_type_Private':[work_type_Private],'work_type_Self-employed':[work_type_Selfemployed],
'work_type_children':[work_type_children],'Residence_type_Urban':[Residence_type_Urban],'smoking_status_formerly smoked':[smoking_status_formerlysmoked],
'smoking_status_never smoked':[smoking_status_neversmoked], 'smoking_status_smokes':[smoking_status_smokes]
},index=[0])

model=pickle.load(open(r'D:\Education\university\6 term\machine learning\healthcare-dataset-stroke-data.sav','rb'))
Con=st.sidebar.button('confirm')
if Con:
    result=model.predict(df)
    st.write(result)
