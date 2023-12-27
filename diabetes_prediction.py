import numpy as np
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler 

# Loading the saved model and scaler
loaded_model = pickle.load(open('C:/Users/nafis/Downloads/trained_model (1).sav', "rb"))

# Creating a function for prediction
def diabetes_prediction(input_data):
    # Changing the input data to a numpy array and converting to float
    input_data_as_numpy_array = np.asarray(input_data)
    
    # Reshape the array as we're predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    # Standardize the input data using the loaded scaler
    # input_data_standardized = scaler.transform(input_data_reshaped)
    
    # Make predictions using the loaded model
    prediction = loaded_model.predict(input_data_reshaped)
    
    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

def main():
    # Giving a title
    st.title('Diabetes Prediction Web App')
    
    # Getting the input data from the user
    # Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness Level')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Level')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    Age = st.text_input('Age of the Person')
    
    # Code for Prediction
    diagnosis = ''
    
    # Creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
    
    st.success(diagnosis)

if __name__ == '__main__':
    main()
