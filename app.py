import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("GDP at Current Prices (2011-12 Series) - India")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("GDP_QE_Current_Prices_2011-12_Series.csv")
    return df

df = load_data()

# Preview data
st.subheader("Raw Data")
st.dataframe(df)

# Dropdowns for interaction
columns = df.columns.tolist()

# Assuming the data has a column for sectors/industries and year-wise data
sector_column = st.selectbox("Select Sector/Industry Column", options=columns)
value_columns = st.multiselect("Select Year Columns to Plot", options=columns, default=columns[-4:])

# Display selected sector's data over the years
if sector_column and value_columns:
    st.subheader("GDP Trend for Selected Sectors")
    selected_sectors = st.multiselect("Select Sector(s) to Display", df[sector_column].unique())
    if selected_sectors:
        filtered_df = df[df[sector_column].isin(selected_sectors)]
        filtered_df = filtered_df[[sector_column] + value_columns].set_index(sector_column).T

        st.line_chart(filtered_df)

# Footer
st.markdown("Data Source: Ministry of Statistics and Programme Implementation (MoSPI)")
