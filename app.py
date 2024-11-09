import streamlit as st

# Set up session state variables
if "audio_bytes" not in st.session_state:
    st.session_state["audio_bytes"] = None
if "selected_categories" not in st.session_state:
    st.session_state["selected_categories"] = []
if "transcript" not in st.session_state:
    st.session_state["transcript"] = ""
if "analysis_results" not in st.session_state:
    st.session_state["analysis_results"] = {}

# Navigation
PAGES = {
    "Record Feedback": "audio_recorder",
    "Select Categories": "category_selection",
    "View Results": "results",
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Dynamically import the selected page module
page = __import__(PAGES[selection])

# Run the selected page
page.main()
