
import streamlit as st
import pandas as pd
from inflation_utils import adjust_prices

st.set_page_config(page_title="Procurement Price Adjuster", layout="wide")

st.title("📈 Procurement Price Adjuster")
st.markdown("Upload your historical price data and adjust it to today's values using CPI.")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Original Data", df.head())

    try:
        adjusted_df = adjust_prices(df)
        st.success("Prices adjusted to current levels.")
        st.write("### Adjusted Data", adjusted_df)

        csv = adjusted_df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Adjusted CSV", data=csv, file_name="adjusted_prices.csv")

    except Exception as e:
        st.error(f"Error adjusting prices: {e}")
