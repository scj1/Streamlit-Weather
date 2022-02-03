import streamlit as st


st.set_page_config(page_title='Streamlit Weather', page_icon="⛅")
st.title("🌞Streamlit Weather☁️️")

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://images.pexels.com/photos/1431822/pexels-photo-1431822.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260")
    }
   .sidebar .sidebar-content {
        background: url("https://images.pexels.com/photos/1431822/pexels-photo-1431822.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260")
    }
    </style>
    """,
    unsafe_allow_html=True
)









with st.sidebar.expander("About"):
         st.write( "Developed by Dinuja de Silva ")

with st.sidebar.expander("Version"):
    st.write("1.0.0")
