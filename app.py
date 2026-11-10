"""A small, interactive dashboard for tracking greywater use."""

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Greywater Management",  
    page_icon="💧",
    layout="wide",
)

# Keep the input controls together so the dashboard is easy to update.
with st.sidebar:
    st.title("Water data")
    st.caption("Enter the greywater readings you want to review.")

    collected = st.number_input(
        "Greywater collected (litres)",
        min_value=0,
        value=12_000,
        step=500,
        help="The total amount of greywater collected.",
    )
    treated =st.number_input(
        "Greywater treated (litres)",
        min_value=0,
        value=10_000,
        step=500,
        help="The amount of collected greywater that has been treated.",
    )
    reused = st.number_input(
        "Greywater reused (litres)",
        min_value=0,
        value=8_500,
        step=500,
        help="The amount of treated greywater that has been reused.",
    )

st.title("Greywater Management")
st.caption("A clear view of collected, treated, and reused water.")
st.divider()

if reused > collected:
    st.warning(
        "Reused water is greater than collected water. "
        "Please check the readings in the sidebar."
    )

reuse_percentage = (reused / collected * 100) if collected else 0

metric_columns = st.columns(3)
metric_columns[0].metric("Water collected", f"{collected:,.0f} L")
metric_columns[1].metric("Water reused", f"{reused:,.0f} L")
metric_columns[2].metric("Reuse percentage", f"{reuse_percentage:.1f}%")

st.subheader("Water by stage")
st.caption("Compare the volume recorded at each step of the greywater process.")

chart_data = pd.DataFrame(
    {
        "Stage": ["Collected", "Treated", "Reused"],
        "Litres": [collected, treated, reused],
    }
).set_index("Stage")

st.bar_chart(
    chart_data,
    color="#0F9D9A",
    y_label="Litres",
    height=340,
)

if collected == 0:
    st.info("Enter a collected-water value greater than zero to calculate a reuse percentage.")
