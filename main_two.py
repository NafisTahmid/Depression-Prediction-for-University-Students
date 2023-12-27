import numpy as np
import pickle
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

#Loading the saved model
loaded_model = pickle.load(open("Depression-Prediction-for-University-Students
/depression_dataset_trained_model_updated.sav", "rb"))

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

    #Getting the input data from user
    gender_subheader = st.subheader("What is your Gender?")
    gender_markdown = st.markdown('''
                                Press:
                                
                                  '0' if you're a male

                                  '1' if you're a female
                                ''')
    gender = st.text_input("Your Gender")

    
    age_subheader = st.subheader("What is your age?")
    age_markdown = st.markdown('''
                                Press:
                               
                               '0' if you're '18 years old'

                               '1' if your're '19 years old'

                               '2' if you're '20 years old'

                               '3' if your're '21 years old'

                               '4' if you're '22 years old'

                               '5' if you're '23 years old'

                               '6' if you're '24 years old'

                               '7' if you're '25 years old'

                               '8' if you're '26 years old'

                               '9' if you're '30 years old'

                               '10' if you're 'more than 30 years old' 

                            ''')
    age = st.text_input("Please enter your age")

    university_year_subheader = st.subheader("Which year of university are you in?")
    st.markdown('''
                    Press:
                
                    '0' for First Year
                
                    '1' for Second Year
                
                    '2' for Third Year
                
                    '3' for 4th Year
                
                    '4' for Final Year(Medical)
                
                    '5' for Post-Graduation
                ''')
    university_year = st.text_input("Please Enter University Year")

    family_members_sub_header = st.subheader("How many members are there in your family?")
    st.markdown('''
                    Press:
                
                    '0' for 1 member
                
                    '1' for 2 members
                
                    '2' for 3 members
                
                    '3' for 6 members
                
                    '4' for 5 members
                
                    '5' for 4 members
                
                    '6' for more than 6  members

                ''')
    family_members = st.text_input("Please Enter number of Family Members")

    
    educational_background_sub_header = st.subheader("What is your educational background?")
    educational_background_markdown = st.markdown('''
                                                 Press:
                                                  
                                                 '0' for 'Bangla Medium',
                                                
                                                 '1' for 'English Medium', 
                                                  
                                                 '2' for 'Madrasah'
                                                 ''')
    educational_background = st.text_input(label = "Please enter your educational background", placeholder = "")

    relationship_status_sub_header= st.subheader("What is your relationship status?")
    relationship_status_markdown = st.markdown('''
                                              Press:
                                               
                                              '0' for 'In a Relationship',
                                               
                                              '1' for 'Married',
                                               
                                              '2' for 'Single'
                                                ''')
    relationship_status = st.text_input(label="Please enter your relationship status", placeholder="")
    

    number_of_children_sub_header = st.subheader(" If you have any children, how many do you have? ")

    number_of_children_markdown = st.markdown('''
                                            Press:
                                            
                                            '0' for 'No Children'
                                              
                                            '1' for '1 child'
                                            
                                            '2' for '2 children'
                                            
                                            '3' for '3 children'
                                              
                                            '4' for '4 children'
                                              
                                            '5' for 'more than 4 children'  
                                              
                                              ''')
    number_of_children = st.text_input("Please enter your Number of children")

    home_town_sub_header = st.subheader("Were you brought up in the capital city of Bangladesh?")
    home_town_markdown = st.markdown('''
                                    Press:
                                     
                                    '1' for 'Yes',
                                     
                                    '0' for 'No'
                                    ''')
    home_town = st.text_input("Please enter answer here")

    income_source_sub_header = st.subheader("Do you have any part time job or income source?")
    income_source_markdown = st.markdown('''
                                        Press:
                                         
                                        '1' for 'Yes',
                                         
                                        '0' for 'No'
                                        ''')
    income_source = st.text_input("Please enter an input")

    
    monthly_income_subheader = st.subheader("What is your monthly income?")
    monthly_income_markdown = st.markdown('''
                                         Press:
                                        
                                          '0' for 'Nearly 10K'

                                           '1' for 'Nearly 20K'
                                          
                                           '3' for 'Nearly 5k'
                                          
                                           '4' for 'Not earning as of now'
                                        ''')
    monthly_income_encoded = st.text_input(label="Please enter your answer.")

    expense_sub_header = st.subheader("What is your monthly living expense?")
    expense_markdown=st.markdown('''
                                Press:
                                 
                                '0' for 'More Than 100K',
                                 
                                '1' for 'Nearly 100K',
                                 
                                '2' for 'Nearly 10K',

                                '3' for 'Nearly 20K',

                                '4' for 'Nearly 40K',
                                 
                                '5' for 'Nearly 5K',
                                 
                                '6' for 'Nearly 60K',
                                 
                                '7' for 'Nearly 80K'
                                ''')
    monthly_living_expense = st.text_input(label="Please enter your monthly living expense")

    academic_performance_satisfaction_sub_header = st.subheader("Are you currently satisfied with your academic performance?")
    academic_performance_satisfaction_markdown = st.markdown('''
                                                            Press:
                                                             

                                                            '1' for 'Yes',
                                                             
                                                            '0' for 'No'
                                                            ''')
    academic_performance_satisfaction = st.text_input("12. Are you satisfied with your result?")
    
    physical_disabilities_sub_header = st.subheader("Do you have any physical disabilities?")
    physical_disabilities_markdown = st.markdown('''
                                                Press:
                                                 
                                                '1' for 'Yes',
                                                 
                                                 '0' for 'No'
                                                ''')
    physical_disabilities = st.text_input("Please answer 'Yes or no'")

    road_accident_issue_sub_header = st.subheader("Have you ever been in a road accident? ")
    road_accident_issue_markdown = st.markdown('''
                                              Press:

                                              '1' for 'Yes',
                                               
                                              '0' for 'No'                                        
                                                ''')
    road_accident_issue = st.text_input("What's the answer?")

    childhood_trauma_sub_header = st.subheader("Do you have any childhood trauma?")
    childhood_trauma_markdown = st.markdown('''
                                            Press:

                                            '1' for 'Yes',
                                            
                                             '0' for 'No'
                                            ''')
    childhood_trauma = st.text_input("Please enter a number")

    taking_medication_sub_header = st.subheader("Are you currently taking any doctor prescribed medication regularly?")
    taking_medication_markdown = st.markdown('''
                                            Press:
                                             
                                            '1' for 'Yes',
                                             
                                             '0' for 'No'
                                            ''')
    taking_medication = st.text_input("Do you take prescribed medication regularly?")

    is_a_religious_person_sub_header = st.subheader("Do you consider yourself as a religious person? ")
    is_a_religious_person_markdown = st.markdown('''
                                                 Press:

                                                '1' for 'Yes'
                                                 
                                                '0' for 'No'
                                                ''')
    is_a_religious_person = st.text_input("Are you a religious person?")

    social_gathering_time_sub_header = st.subheader("How often do you find yourself going out to social gatherings every Week?")
    social_time_markdown=st.markdown('''
                                    Press:
                                     
                                    '0' for 'I go out on weekends and also weekdays',
                                    
                                    '1' for 'Rarely go to social gatherings',
                                     
                                    '2' for 'Weekends only'
                                    ''')
    social_gathering_time = st.text_input(label="Please enter social gatherings time") 

    participant_in_indoor_fun_activity_sub_header = st.subheader("Are you a regular participant in novels/movies/series/Ludo/chess or any indoor fun activity?")
    participant_in_indoor_fun_activity_markdown = st.markdown('''
                                                             Press:
                                                            
                                                             '1' for 'Yes'
                                                              
                                                              '0' for 'No'
                                                             ''') 
    participant_in_indoor_fun_activity = st.text_input("What is your answer?")

    sports_or_gym_sub_header = st.subheader("Do you do sports or gym regularly?")
    sports_or_gym_markdown = st.markdown('''
                                        Press:
                                         
                                        '1' for 'Yes',
                                         
                                         '0' for 'No'
                                        ''')
    sports_or_gym_regularly = st.text_input("Please enter an answer")

    social_media_markdown= st.subheader("How much time do you spend on social media on a daily basis?")

    st.markdown('''
                Press:
                
                '0' for 'One hour',

                '1' for 'Two hours',
                
                '2' for 'Three hours',
                
                '3'  for 'Four hours',
                
                '4' for 'Five hours',
                
                '5' for 'Less than thirty minutes',
                
                '6' for 'More than 5 hours'
                ''')
    social_media_time = st.text_input("Please Enter Social Media Usage Time")

    social_satisafction = st.subheader("How satisfied are you with your social life?")
    st.markdown('''
                    Press:

                    '0' for 'Disappointed',
                
                    '1' for 'Not Satisfied',
                
                    '2' for 'Satisfied',
                
                     '3' for 'Very Satisfied'
                
                ''')
    social_life_satisfaction = st.text_input("Please Enter Social Life Satisfaction")


    coffee_person_subheader = st.subheader("Do you consider yourself a coffee person?")
    coffee_person_markdown = st.markdown('''
                                        Press:
                                         
                                        '1' for 'Yes',
                                        
                                         '0' for 'No'
                                        ''')
    coffee_person = st.text_input(label="", placeholder= "")

    substance_addiction_subheader = st.subheader("Are you addicted to any kind of addictive substances?")
    substance_addiction_markdown = st.markdown('''
                                 Press:

                                 '1' for 'Yes',

                                 '0' for 'No'
                                ''')
    substance_addiction = st.text_input(label="Please enter a value",  placeholder= "")

    

    sleep_duration_sub_header = st.subheader("How long do you sleep every night?")
    st.markdown('''
                
                Press:
                
                
                '0' for 3 hours
                
                '1' for 4 hours

                '2' for 5 hours
                
                '3' for 6 hours

                '4' for 7 hours
                
                '5' for 8 hours

                '7' for More than 9 hours

                ''')
    sleep_duration = st.text_input("Please enter Sleep Duration")

    #Code for prediction
    depression = ''

    #Creating a button for prediction
    if st.button('Depression Test Result'):
        depression = depression_prediction([gender, number_of_children, home_town, income_source, academic_performance_satisfaction, physical_disabilities, road_accident_issue, childhood_trauma, taking_medication, is_a_religious_person, participant_in_indoor_fun_activity, sports_or_gym_regularly, coffee_person, substance_addiction, educational_background, relationship_status, monthly_income_encoded, monthly_living_expense, social_gathering_time, social_media_time, social_life_satisfaction, age, university_year, family_members, sleep_duration])

    st.success(depression)

if __name__ == '__main__':
    main()
