import streamlit as st
import requests

st.set_page_config(page_title='Streamlit Weather', page_icon="⛅")
st.title("🌞Streamlit Weather☁️️")

page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)









with st.sidebar.expander("About"):
         st.write( "Developed by Dinuja de Silva ")

with st.sidebar.expander("Version"):
    st.write("1.0.0")

print(response.text)
