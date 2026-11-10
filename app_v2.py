
import streamlit as st

st.set_page_config(
    page_title="Greywater Management System",
    page_icon="💧",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
.stApp {
    background-color: #F3F8FC;
}
h1, h2, h3 {
    color: #123B5D;
}
[data-testid="stMetric"] {
    background-color: white;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #DCE8F0;
}
div.stButton > button {
    background-color: #087F8C;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("💧 Greywater System")
st.sidebar.caption("Water Quality & Reuse Monitoring")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Water Quality Input", "Predictions", "Analytics", "About"]
)

# HOME PAGE
if page == "Home":

    st.title("💧 Greywater Management System")
    st.subheader("Smart Water Quality Monitoring & Reuse")

    st.markdown("""
    Welcome to the Greywater Management Dashboard.

    This system aims to use machine learning to analyse greywater
    quality and assess its suitability for different reuse purposes.
    """)

    st.divider()

    st.subheader("Project Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("💧 **Water Quality**\n\nAnalyse important water parameters.")

    with col2:
        st.info("🤖 **Machine Learning**\n\nPredict water quality categories.")

    with col3:
        st.info("♻️ **Reuse Assessment**\n\nEstimate suitability for reuse.")

    st.divider()

    st.subheader("Project Workflow")

    st.markdown("""
    1. Enter greywater quality measurements.
    2. Analyse the input parameters.
    3. Predict the water quality category.
    4. Assess suitability for reuse.
    """)

# WATER QUALITY INPUT PAGE
elif page == "Water Quality Input":

    st.title("Water Quality Input")
    st.write("Enter water quality measurements to analyse greywater.")

    st.info(
        "The input fields will be finalised after the machine "
        "learning team confirms the selected model features and units."
    )

    st.subheader("Input Form Preview")

    st.text_input("Sample ID", placeholder="Enter sample identification")
    st.selectbox(
        "Water Source",
        ["Select source", "Bathroom", "Laundry", "Kitchen", "Mixed greywater"]
    )

    st.warning(
        "Final water-quality parameters will be added after model integration."
    )

# PREDICTIONS PAGE
elif page == "Predictions":

    st.title("Machine Learning Predictions")

    st.write("The system will provide two prediction results.")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💧 Water Quality Category")
        st.info("Prediction will appear here after model integration.")

    with col2:
        st.subheader("♻️ Reuse Suitability")
        st.info("Reuse suitability prediction will appear here.")

    st.caption(
        "Predictions are model estimates and are not a substitute "
        "for laboratory testing or applicable reuse standards."
    )

# ANALYTICS PAGE
elif page == "Analytics":

    st.title("Water Quality Analytics")

    st.write(
        "This section will display charts and statistical summaries "
        "based on the confirmed project dataset."
    )

    st.info(
        "Dataset visualisations will be added after the final "
        "analysis columns are confirmed."
    )

# ABOUT PAGE
elif page == "About":

    st.title("About the Project")

    st.subheader("Greywater Management System")

    st.write("""
    Greywater is wastewater generated from sources such as
    bathrooms, laundry and wash basins.

    This project aims to explore how machine learning can help
    analyse greywater quality and assess its potential for reuse.
    """)

    st.subheader("Project Objectives")

    st.markdown("""
    - Monitor greywater quality.
    - Classify water quality using machine learning.
    - Assess suitability for reuse.
    - Support better water management decisions.
    """)

    st.divider()

    st.caption("Developed as an academic group project.")
