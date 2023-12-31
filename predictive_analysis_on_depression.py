import requests
import numpy as np
import pickle
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Loading new packages
from PIL import Image
import pandas as pd
from PyPDF2 import PdfReader
import pdfplumber

st.set_page_config(page_title="Depression Test for University Students", page_icon='images/5859961_depression_disorder_health_mental_psychology_icon.png')

def load_image(image_file):
    img = Image.open(image_file)
    return img

def read_pdf(file):
    pdfReader = PdfReader(file)
    count = len(pdfReader.pages)
    all_page_text=""
    for i in range(count):
        page = pdfReader.pages[i]
        all_page_text += page.extract_text()

    return all_page_text
    
github_url = 'https://github.com/NafisTahmid/Depression-Prediction-for-University-Students/raw/main/depression_dataset_trained_model_updated.sav'

response = requests.get(github_url)

#Loading the saved model
# loaded_model = pickle.load(open("https://github.com/NafisTahmid/Depression-Prediction-for-University-Students/blob/main/depression_dataset_trained_model_updated.sav", "rb"))
loaded_model = pickle.loads(response.content)

#Create a function for prediction

def depression_prediction(input_data):
    # input_data = (7,100,0,0,0,30,0.484,32)

    #Changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #Reshape the array as we're predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # Standardize the input data
    # std_data = scaler.transform(input_data_reshaped)
    # print(std_data)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return "You're not depressed"
    else:
        return "You're depressed"


def main():
    #Giving a title
    st.title("Depression Prediction Web App")

    menu = ["Test Depression", "Report", "Poster", "About Us"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Test Depression":
        st.subheader("Test Your Depression Result")
        #############################################################################################
        global gender
        gender_input = st.radio("What is your gender?", ("Female", "Male"))
        if gender_input == "Female":
            gender = 1
        elif gender_input == "Male":
            gender = 0
            
        global age,age_input
        with st.expander("What is your age? (Click to Expand)"):
            age_input = st.radio("",("18", "19", "20", "21", "22", "23", "24", "25", "26", "27 to 29", "30", "More than 30"))
            if age_input == "18":
                age = 0
            elif age_input == "19":
                age = 1
            elif age_input == "20":
                age = 2
            elif age_input == "21":
                age = 3
            elif age_input == "22":
                age = 4
            elif age_input == "23":
                age = 5
            elif age_input == "24":
                age = 6
            elif age_input == "25":
                age = 7
            elif age_input == "26":
                age = 7
            elif age_input == "27 to 29":
                age = 8
            elif age_input == "30":
                age = 9
            elif age_input == "More than 30":
                age = 10
        
                
        global university_year_input, university_year
        with st.expander("Which year of university are you in?(Click to Expand)"):
            university_year_input = st.radio("", ("First Year", "Second Year", "Third Year", "Final Year", "Final Year(Medical)", "Post-Graduation"))

            if university_year_input == "First Year":
                university_year = 0
            elif university_year_input == "Second Year":
                university_year = 1
            elif university_year_input == "Third Year":
                university_year =2
            elif university_year_input == "Final Year":
                university_year = 3
            elif university_year_input == "FInal Year(Medical)":
                university_year = 4
            elif university_year_input == "Post-Graduation":
                university_year = 5
                
        global family_members_input, family_members

        with st.expander("How many members are there in your family?(Click to Expand)"):
            family_members_input = st.radio("", ("One", "Two", "Three", "Four", "Five", "Six", "More than Six members"))

            if family_members_input == "One":
                family_members = 0
            elif family_members_input == "Two":
                family_members = 1
            elif family_members_input == "Three":
                family_members = 2
            elif family_members_input == "Four":
                family_members = 5
            elif family_members_input == "Five":
                family_members = 4
            elif family_members_input == "Six":
                family_members = 3
            elif family_members_input == "More than Six members":
                family_members = 6

        global educational_background
        educational_background_input = st.radio("What is your educational background?", ("Bangla Medium", "Madrasah", "English Medium"))
        if educational_background_input == "Bangla Medium":
            educational_background = 0
        elif educational_background_input == "Madrasah":
            educational_background = 2
        elif educational_background_input == "English Medium":
            educational_background = 1
            
        global relationship_status
        relationship_status_input = st.radio("What is your relationship status?", ("Single", "In a Relationship", "Married"))
        if relationship_status_input == "Single":
            relationship_status = 2
        elif relationship_status_input == "In a Relationship":
            relationship_status = 0
        elif relationship_status_input == "Married":
            relationship_status = 1
            
        global number_of_children, number_of_children_input

        with st.expander("If you have any children, how many do you have?(Click to Expand)"):
            number_of_children_input = st.radio("", ("No Children", "One", "Two", "Three", "Four", "More than Four"))
            if number_of_children_input == "No Children":
                number_of_children = 0
            elif number_of_children_input == "One":
                number_of_children = 1
            elif number_of_children_input == "Two":
                number_of_children = 2
            elif number_of_children_input == "Three":
                number_of_children = 3
            elif number_of_children_input == "Four":
                number_of_children = 4
            elif number_of_children_input == "More than Four":
                number_of_children = 5
                
        global home_town
        home_town_input = st.radio("Were you brought up in the capital city of Bangladesh?", ("Yes", "No"))
        if home_town_input == "Yes":
            home_town = 1
        elif home_town_input == "No":
            home_town = 0

        global income_source
        income_source_input = st.radio("Do you have any part time job or income source?", ("Yes", "No"))
        if income_source_input == "Yes":
            income_source = 1
        elif income_source_input == "No":
            income_source = 0

        global monthly_income
        with st.expander("What is your monthly income?(Click to Expand)"):
            monthly_income_input = st.radio("", ("Not earning as of now", "Nearly 5K", "Nearly 10K", "Nearly 20K"))
            if monthly_income_input == "Not earning as of now":
                monthly_income = 4
            elif monthly_income_input == "Nearly 5K":
                monthly_income = 3
            elif monthly_income_input == "Nearly 10K":
                monthly_income = 0
            elif monthly_income_input == "Nearly 20K":
                monthly_income = 1

        global monthly_living_expense, monthly_living_expense_input
        with st.expander("What is your monthly living expense?(Click to Expand)"):
            monthly_living_expense_input = st.radio("", ("Nearly 5K", "Nearly 10K", "Nearly 20K", "Nearly 30K", "Nearly 40K to 50K", "Nearly 60K", "Nearly 70K to 80K", "Nearly 100K",  "More than 100K"))

            if monthly_living_expense_input == "Nearly 5K":
                monthly_living_expense = 5
            elif monthly_living_expense_input == "Nearly 10K":
                monthly_living_expense = 2
            elif monthly_living_expense_input == "Nearly 20K":
                monthly_living_expense = 3
            elif monthly_living_expense_input == "Nearly 40K to 50K":
                monthly_living_expense = 4
            elif monthly_living_expense_input == "Nearly 60K":
                monthly_living_expense = 6
            elif monthly_living_expense_input == " Nearly 70K to 80K":
                monthly_living_expense = 7
            elif monthly_living_expense_input == "Nearly 100K":
                monthly_living_expense = 1
            elif monthly_living_expense_input == "More Than 100K":
                monthly_living_expense = 0
                
        global academic_performance_satisfaction
        academic_performance_satisfaction_input =st.radio("Are you currently satisfied with your academic performance?", ("Yes", "No"))
        if academic_performance_satisfaction_input == "Yes":
            academic_performance_satisfaction = 1
        elif academic_performance_satisfaction_input == "No":
            academic_performance_satisfaction = 0
            
        global physical_disabilities
        physical_disabilities_input = st.radio("Do you have any physical disabilities?", ("Yes", "No"))
        if physical_disabilities_input == "Yes":
            physical_disabilities = 1
        elif physical_disabilities_input == "No":
            physical_disabilities = 0
    
        global road_accident_issue
        road_accident_issue_input = st.radio("Have you ever been in a road accident?", ("Yes", "No"))
        if road_accident_issue_input == "Yes":
            road_accident_issue = 1
        elif road_accident_issue_input == "No":
            road_accident_issue = 0

        global childhood_trauma
        childhood_trauma_input = st.radio("Do you have any childhood trauma?", ("Yes", "No"))
        if childhood_trauma_input == "Yes":
            childhood_trauma = 1
        elif childhood_trauma_input == "No":
            childhood_trauma = 0
            
        global taking_medication
        taking_medication_input = st.radio("Are you currently taking any doctor prescribed medication regularly?", ("Yes", "No"))
        if taking_medication_input == "Yes":
            taking_medication = 1
        elif taking_medication_input == "No":
            taking_medication = 0
            
        global is_a_religious_person
        is_a_religious_person_input = st.radio("Are you a religious person?", ("Yes", "No"))
        if is_a_religious_person_input == "Yes":
            is_a_religious_person = 1
        elif is_a_religious_person_input == "No":
            is_a_religious_person = 0
        
        global social_gathering_time
        social_gathering_time_input = st.radio("How often do you find yourself going out to social gatherings every week?", ("I go out on weekends and also weekdays", "Rarely go to social gatherings", "Weekends only"))
        if social_gathering_time_input == "I go out on weekends and also weekdays":
            social_gathering_time = 0
        elif social_gathering_time_input == "Rarely go to social gatherings":
            social_gathering_time = 1
        elif social_gathering_time_input == "Weekends Only":
            social_gathering_time = 2
            
        global participant_in_indoor_fun_activity
        participant_in_indoor_fun_activity_input = st.radio("Are you a regular participant in novels/movies/series/Ludo/chess or any indoor fun activity?", ("Yes", "No"))
        if participant_in_indoor_fun_activity_input == "Yes":
            participant_in_indoor_fun_activity = 1
        elif participant_in_indoor_fun_activity_input == "No":
            participant_in_indoor_fun_activity = 0
            
        global sports_or_gym_regularly
        sports_or_gym_regularly_input = st.radio("Do you do sports or gym regularly?", ("Yes", "No"))
        if sports_or_gym_regularly_input == "Yes":
            sports_or_gym_regularly = 1
        elif sports_or_gym_regularly_input == "No":
            sports_or_gym_regularly = 0
            
        global social_media_time, social_media_time__input

        with st.expander("How much time do you spend on social media on a daily basis?"):
            social_media_time_input = st.radio("", ("Less than thirty minutes", "One hour", "Two hours", "Three hours", "Four hours", "Five hours", "More than Five hours"))

            if social_media_time_input == "Less than thirty minutes":
                social_media_time = 5
            elif social_media_time_input == "One hour":
                social_media_time = 0
            elif social_media_time_input == "Two hours":
                social_media_time = 1
            elif social_media_time_input == "Three hours":
                social_media_time = 2
            elif social_media_time_input == "Four hours":
                social_media_time = 3
            elif social_media_time_input == "Five hours":
                social_media_time = 4
            elif social_media_time_input == "More than Five hours":
                social_media_time = 6
                
        global social_life_satisfaction, social_life_satisfaction_input

        with st.expander("How satisfied are you with your social life?(Click to Expand)"):
            social_life_satisfaction_input = st.radio("", ("Disappointed", "Not Safisfied", "Satisfied", "Very Satisfied"))
            if social_life_satisfaction_input == "Disappointed":
                social_life_satisfaction = 0
            elif social_life_satisfaction_input == "Not Satisfied":
                social_life_satisfaction = 1
            elif social_life_satisfaction_input == "Satisfied":
                social_life_satisfaction = 2
            elif social_life_satisfaction_input == "Very Satisfied":
                social_life_satisfaction = 3

        global chai_person
        chai_person_input = st.radio("Do you consider yourseld a tea/coffee person?", ("Yes", "No"))
        if chai_person_input == "Yes":
            chai_person = 1
        elif chai_person_input == "No":
            chai_person = 0
        
        global substance_addiction
        substance_addiction_input = st.radio("Are you addicted to any kind of addictive substances?", ("Yes", "No"))
        if substance_addiction_input == "Yes":
            substance_addiction = 1
        elif substance_addiction_input == "No":
            substance_addiction = 0
            
        global sleep_duration
        with st.expander("How long do you sleep every night?(Click to Expand)"):
            sleep_duration_input = st.radio("", ("Three hours", "Four hours", "Five hours", "Six hours", "Seven hours", "Eight hours", "More than Nine hours"))
            if sleep_duration_input == "Three hours":
                sleep_duration = 0
            elif sleep_duration_input == "Four hours":
                sleep_duration = 1
            elif sleep_duration_input == "Five hours":
                sleep_duration = 2
            elif sleep_duration_input == "Six hours":
                sleep_duration = 3
            elif sleep_duration_input == "Seven hours":
                sleep_duration = 4
            elif sleep_duration_input == "Eight hours":
                sleep_duration = 5
            elif sleep_duration_input == "More than Nine hours":
                sleep_duration =7


        #Code for prediction
        depression = ''

        #Creating a button for prediction
        if st.button('Depression Test Result'):
            depression = depression_prediction([gender, number_of_children, home_town, income_source, academic_performance_satisfaction, physical_disabilities, road_accident_issue, childhood_trauma, taking_medication, is_a_religious_person, participant_in_indoor_fun_activity, sports_or_gym_regularly, chai_person, substance_addiction, educational_background, relationship_status, monthly_income, monthly_living_expense, social_gathering_time, social_media_time, social_life_satisfaction, age, university_year, family_members, sleep_duration])
        

        st.success(depression)

    elif choice == "Report":
        st.subheader("Report")
        raw_text = read_pdf("data/Predictive-Analysis-on-Depression-among-University-Students-in-Bangladesh (2).pdf")
        st.write(raw_text)

    elif choice == "Poster":
        st.subheader("Poster")
        st.image(load_image("images/Report.PNG"))

    else:
        st.subheader("About Us")
        st.markdown("#### Supervisor")
        st.text("MD. Shahriar Rahman Rana")
        st.markdown("#### Co Supervisor")
        st.text("Rafeed Rahman")
        st.markdown("#### Students")
        st.text("Syed Aref Ahmed - 19201124 - syed.aref.ahmed@g.bracu.ac.bd ")
        st.text("Khondokar Jamal E Mustafa - 19241008 - khondokar.jamal.e.mustafa@g.bracu.ac.bd")
        st.text("MD. Nafis Tahmid - 19301053 - md.nafis.tahmid@g.bracu.ac.bd")
        st.text(" Ibtesum Arif - 19201054 - ibtesum.arif@g.bracu.ac.bd")
        

    

if __name__ == '__main__':
    main()
