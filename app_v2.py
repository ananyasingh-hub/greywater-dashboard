
import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Greywater Management System",
    page_icon="💧",
    layout="wide"
)

# ---------------- DESIGN ----------------
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
    padding: 16px;
    border-radius: 12px;
    border: 1px solid #DCE8F0;
}
</style>
""", unsafe_allow_html=True)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    file_path = Path(__file__).parent / "greywater_ml_features.csv"

    if file_path.exists():
        return pd.read_csv(file_path)

    return None

df = load_data()

# ---------------- SIDEBAR ----------------
st.sidebar.title("💧 Greywater System")
st.sidebar.caption("Water Quality & Reuse Monitoring")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Water Quality Input", "Predictions", "Analytics", "About"]
)

# ---------------- HOME ----------------
if page == "Home":

    st.title("💧 Greywater Management System")
    st.subheader("Smart Water Quality Monitoring & Reuse")

    st.write("""
    Welcome to the Greywater Management Dashboard.

    This system aims to analyse greywater quality using machine
    learning and assess its suitability for different reuse purposes.
    """)

    st.divider()
    st.subheader("Project Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("💧 **Water Quality**\n\nAnalyse water parameters.")

    with col2:
        st.info("🤖 **Machine Learning**\n\nPredict water quality categories.")

    with col3:
        st.info("♻️ **Reuse Assessment**\n\nAssess potential reuse suitability.")

    st.divider()
    st.subheader("Project Workflow")

    st.markdown("""
    1. Enter greywater quality measurements.
    2. Analyse water-quality parameters.
    3. Predict the water quality category.
    4. Assess suitability for reuse.
    """)

# ---------------- INPUT ----------------
elif page == "Water Quality Input":

    st.title("Water Quality Input")
    st.write("Enter sample information.")

    st.info(
        "The final measurement fields will be added after "
        "the ML team confirms the selected model features and units."
    )

    st.text_input("Sample ID", placeholder="Enter sample identification")

    st.selectbox(
        "Water Source",
        ["Select source", "Bathroom", "Laundry", "Kitchen", "Mixed greywater"]
    )

    st.warning(
        "Final water-quality parameters are awaiting model confirmation."
    )

# ---------------- PREDICTIONS ----------------
elif page == "Predictions":

    st.title("Machine Learning Predictions")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("💧 Water Quality Category")
        st.info("Prediction will appear here after model integration.")

    with col2:
        st.subheader("♻️ Reuse Suitability")
        st.info("Reuse prediction will appear here after model integration.")

    st.caption(
        "ML predictions are estimates, not a guarantee of safe reuse. "
        "Applicable standards and laboratory testing must also be considered."
    )

# ---------------- ANALYTICS ----------------
elif page == "Analytics":

    st.title("📊 Water Quality Analytics")
    st.write("Explore the greywater dataset.")

    if df is None:
        st.error(
            "Dataset not found. Check that "
            "greywater_ml_features.csv is in the repository root."
        )

    else:
        st.success("Dataset loaded successfully!")

        total_rows = len(df)
        total_columns = len(df.columns)
        numeric_columns = df.select_dtypes(include="number").columns.tolist()

        col1, col2, col3 = st.columns(3)

        col1.metric("Total Records", total_rows)
        col2.metric("Total Parameters", total_columns)
        col3.metric("Numerical Parameters", len(numeric_columns))

        st.divider()

        st.subheader("Dataset Preview")
        st.dataframe(df.head(10), use_container_width=True)

        st.divider()

        st.subheader("Missing Values")
        missing = df.isnull().sum()
        missing = missing[missing > 0]

        if missing.empty:
            st.success("No missing values found.")
        else:
            st.bar_chart(missing)

        st.divider()

        st.subheader("Parameter Distribution")

        if numeric_columns:
            selected_column = st.selectbox(
                "Choose a water-quality parameter",
                numeric_columns
            )

            values = pd.to_numeric(
                df[selected_column], errors="coerce"
            ).dropna()

            if len(values) > 0:
                st.write(f"Distribution of {selected_column}")

                if values.nunique() > 1:
                    bins = pd.cut(values, bins=10)
                    distribution = bins.value_counts().sort_index()
                    distribution.index = distribution.index.astype(str)
                    st.bar_chart(distribution)
                else:
                    st.info("This parameter has only one distinct value.")

                st.subheader("Statistical Summary")
                st.dataframe(
                    values.describe().to_frame("Value"),
                    use_container_width=True
                )
            else:
                st.warning("No numerical values available for this parameter.")

        else:
            st.warning("No numerical columns were found in the dataset.")

# ---------------- ABOUT ----------------
elif page == "About":

    st.title("About the Project")

    st.subheader("Greywater Management System")

    st.write("""
    Greywater is wastewater generated from sources such as
    bathrooms, laundry and wash basins.

    This academic project explores the use of machine learning
    to analyse greywater quality and assess its potential for reuse.
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
