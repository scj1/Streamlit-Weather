import streamlit as st
import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"xml"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "4a5237600amsh2d283547f53b90ap12f53djsn09b9149d542d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)




st.title("Streamlit Weather")
