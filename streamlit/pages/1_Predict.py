import streamlit as st
import pickle
import pandas as pd
from datetime import datetime
import sys


st.title('Predict AQI')


# if "city" not in st.session_state:
#     st.session_state.num1 = ""

# if "co" not in st.session_state:
#     st.session_state.co = 0.0
# if "o3" not in st.session_state:
#     st.session_state.o3 = 0.0

# if "so2" not in st.session_state:
#     st.session_state.so2 = 0.0
# if "no2" not in st.session_state:
#     st.session_state.no2 = 0.0

# if "pm25" not in st.session_state:
#     st.session_state.pm25 = 0.0
# if "pm10" not in st.session_state:
#     st.session_state.pm10 = 0.0



# def reset_form():
#     st.session_state.city = ""

#     st.session_state.co = 0.0
#     st.session_state.o3 = 0.0

#     st.session_state.so2 = 0.0
#     st.session_state.no2 = 0.0

#     st.session_state.pm25 = 0.0
#     st.session_state.pm10 = 0.0



with st.form(key="my_form"):
    col1,col2 = st.columns(2)
    city = col1.selectbox("Location",options=["Ahmedabad","Bengaluru","Chennai","Delhi","Hyderabad","Kolkata","Mumbai","Pune"])
    hour = col2.number_input("Hour : ",min_value=0,max_value=23,value=None)

    col1,col2 = st.columns(2)
    co = col1.number_input("Conc. of Carbon monoxide (μg/m3):",min_value=0.0, step=0.1, format="%.2f",placeholder=0,value=None)
    o3 = col2.number_input("Conc. of surafce O3 (μg/m3):",min_value=0.0, step=0.1, format="%.2f",value=None)

    col1,col2 = st.columns(2)
    so2 = col1.number_input("Conc. of surface SO2 (μg/m3):",min_value=0.0, step=0.1, format="%.2f",value=None)
    no2 = col2.number_input('Conc. of surface NO2 (μg/m3):',min_value=0.0, step=0.1, format="%.2f",value=None)

    
    pm25 = st.number_input("Conc. of particulate matter < 2.5 microns (μg/m3):",min_value=0.0, step=0.1, format="%.2f",value=None)
    pm10 = st.number_input("Conc. of particulate matter < 10 microns (μg/m3):",min_value=0.0, step=0.1, format="%.2f",value=None)


    # Submit button
    submit_button = st.form_submit_button("Predict")


# co,no2,o3,pm10,pm25,so2,hour
if submit_button:

    if hour == None or co == None or o3 == None or so2 == None or no2==None or pm25 == None or pm10 == None:
        st.warning("All fields are required, some fileds are missing!")
        sys.exit(0)
    
    # encoder
    with open("files/encoder.pkl", "rb") as file:
        encoder = pickle.load(file)
    
    # ensembled stacked model
    with open("files/stacked_ensembled.pkl",'rb') as file:
        model = pickle.load(file)
    
    # standard scaler
    with open("files/standard_scaler.pkl",'rb') as file:
        standard_scaler = pickle.load(file)
    
    # polynomial Features
    with open("files/polynomialFeatures.pkl",'rb') as file:
        polynomial_features = pickle.load(file)
    
    input = pd.DataFrame({
        'co' : [co],
        'no2': [no2],
        'o3' : [o3],
        'pm10':[pm10],
        'pm25':[pm25],
        'so2':[so2],
        'hour':[hour]
    })
    
    # categorical encoding
    encoded_cities = encoder.get_feature_names_out(['city_name'])
    input[encoded_cities] = encoder.transform(pd.DataFrame([city]))

    # polynomial features_names
    input = polynomial_features.transform(input)
    feature_names = [name.replace(' ', '_') for name in polynomial_features.get_feature_names_out()]

    input = standard_scaler.transform(input)
    

    input = pd.DataFrame(input, columns=polynomial_features.get_feature_names_out())


    prediction = model.predict(input)
    
    

    current_datetime = datetime.now()
    date = current_datetime.date()
    time = current_datetime.time()

    # prediction date,prediction time,city_name,hour,co,o3,so2,no2,pm10,pm25,aqi
    with open('results/recent_estimates.csv','a') as file:
        file.write(f"{date},{time},{city},{hour},{co},{o3},{so2},{no2},{pm10},{pm25},{prediction[0]}\n")

    st.write(f"The Air Quality Index : {prediction[0]}")

    
