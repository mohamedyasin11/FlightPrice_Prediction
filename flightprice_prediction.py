# importing the libraries for this project 
import streamlit as st
from datetime import datetime,timedelta
import pickle

st.title('Flight Price Prediction')

airline = st.sidebar.selectbox('Airlines', [None,'SpiceJet', 'AirAsia', 'Vistara', 'GO_FIRST', 'Indigo', 'Air_India'])
airline_dict = {'AirAsia':0,'Indigo':1,'GO_FIRST':2,'SpiceJet':3,'Air_India':4,'Vistara':5}

source_city = st.sidebar.selectbox('source_city',[None,'Delhi','Hyderabad','Bangalore','Mumbai','Kolkata','Chennai'])
source_city_dict = {'Delhi':0,'Hyderabad':1,'Bangalore':2,'Mumbai':3,'Kolkata':4,'Chennai':5}

departure_time = st.sidebar.selectbox('departure_time',[None,'Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night', 'Late_Night'])

arrival_time = st.sidebar.selectbox('arrival_time',[None,'Evening', 'Early_Morning', 'Morning', 'Afternoon', 'Night','Late_Night'])

time_dict = {'Early_Morning':0,'Morning':1,'Afternoon':2,'Evening':3,'Night':4,'Late_Night':5}

stops = st.sidebar.selectbox('stops',[None,'zero', 'one', 'two_or_more'])
stops_dict = {'zero':0,'one':1,'two_or_more':2}



destination_city = st.sidebar.selectbox('destination_city',[None,'Delhi','Hyderabad','Bangalore','Mumbai','Kolkata','Chennai'])
destination_city_dict = {'Delhi':0,'Hyderabad':1,'Mumbai':2,'Bangalore':3,'Chennai':4,'Kolkata':5} 

Class =  st.sidebar.selectbox('Class',[None,'Economy', 'Business'])
Class_dict = {'Economy':0,'Business':1}

departure_date = st.sidebar.date_input('select the departure date',min_value= datetime.today(),max_value= datetime.today()+timedelta(50))
date_diff = datetime.strptime(str(departure_date),'%Y-%m-%d')-datetime.today()
days_left = int(date_diff.days + 1)

data = [airline, source_city, departure_time, arrival_time, stops , destination_city, Class]
if None not in data and st.button('predict'):
    features = [airline_dict[airline], source_city_dict[source_city], time_dict[departure_time], stops_dict[stops], time_dict[arrival_time], destination_city_dict[destination_city], Class_dict[Class], days_left]
    model = pickle.load(open('flightprice.pkl','rb'))
    predict = model.predict([features])[0]
    st.title(f"your Flight Price is : Rs{round(predict)}")
