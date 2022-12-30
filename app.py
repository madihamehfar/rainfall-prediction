import streamlit as st
from xgboost import XGBClassifier
import pickle
model = pickle.load(open('rain.pkl', 'rb'))

st.title('Rain Predictor')
st.text(model.predict([[0.0,14.8,13.0,37.0,8,10,10,2009,1,2,4,10.5,0.8,6.7,0.0,22.0,0.0]]))
rainfall = st.number_input("Rainfall")
evaporation=st.number_input("Evaporation")
sunshine = st.number_input("Sunshine")
windgustspeed = st.number_input("Windgustspeed")
wgd = st.number_input("wgd")
wdir9am = st.number_input("wdir9")
wdir3pm = st.number_input("wdir3")
year=st.number_input("year")
month=st.number_input("month")
day=st.number_input("day")
week=st.number_input("week")
temp=st.number_input("temp")
pressure=st.number_input("pressure")
temprature=st.number_input("temperature")
wind=st.number_input("wind")
humidity=st.number_input("humidity")
cloud=st.number_input("cloud")

if st.button('Predict'):
    
    y=model.predict([[rainfall,evaporation,sunshine,windgustspeed,wgd,wdir9am,wdir3pm,year,month,day,week,temp,pressure,temprature,wind,humidity,cloud]])[0]
    if y == 1:
        st.success('rain')
    else: st.success('no rain')