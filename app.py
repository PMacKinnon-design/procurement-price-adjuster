import streamlit as st
import pandas as pd
from inflation_utils import adjust_prices

st.set_page_config(page_title="Procurement Price Adjuster", layout="wide")

st.title("📈 Procurement Price Adjuster")
st.markdown("Upload a CSV or manually enter your historical procurement data.")

# Input method selection
input_mode = st.radio("Choose Input Method:", ["Upload CSV", "Manual Entry"])

# CSV Upload Mode
if input_mode == "Upload CSV":
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

# Manual Entry Mode
elif input_mode == "Manual Entry":
    st.write("Enter your data below:")
    default_data = pd.DataFrame({
        "Item": [""],
        "Purchase Date": [""],
        "Price": [0.0],
        "Category": [""]
    })
    df = st.data_editor(default_data, num_rows="dynamic", use_container_width=True)

    if st.button("Submit Manual Data"):
        try:
            df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
            df['Purchase Date'] = pd.to_datetime(df['Purchase Date'], errors='coerce')
            adjusted_df = adjust_prices(df.dropna())
            st.success("Prices adjusted to current levels.")
            st.write("### Adjusted Data", adjusted_df)

            csv = adjusted_df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download Adjusted CSV", data=csv, file_name="adjusted_prices.csv")

        except Exception as e:
            st.error(f"Error processing manual data: {e}")