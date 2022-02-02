import streamlit as st
import requests

st.set_page_config(page_title='Streamlit Weather', page_icon="⛅")
st.title("🌞Streamlit Weather☁️️")

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqhImnN1KCxe8k8DDt0pCl01uqmq6yZDPm3w&usqp=CAU")
    }
   .sidebar .sidebar-content {
        background: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqhImnN1KCxe8k8DDt0pCl01uqmq6yZDPm3w&usqp=CAU")
    }
    </style>
    """,
    unsafe_allow_html=True
)




url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"xml"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "4a5237600amsh2d283547f53b90ap12f53djsn09b9149d542d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

q = ['Sydney', 'Colombo', 'Los Angeles', 'London', 'Rome', 'Paris']

st.sidebar.selectbox('Pick a country', q )


with st.sidebar.expander("About"):
         st.write( "Developed by Dinuja de Silva ")

with st.sidebar.expander("Version"):
    st.write("1.0.0")

print(response.text)
