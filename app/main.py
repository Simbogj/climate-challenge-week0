import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import glob
import os

# Page configuration
st.set_page_config(
    page_title="African Climate Trend Analysis",
    page_icon="🌍",
    layout="wide"
)

# Title and Description
st.title("🌍 African Climate Trend Analysis Dashboard")
st.markdown("""
This dashboard explores historical climate trends (2015–2026) for Ethiopia, Kenya, Sudan, Tanzania, and Nigeria.
Data source: NASA POWER Database.
""")

# Sidebar for filters
st.sidebar.header("Filters")

# Load data helper
@st.cache_data
def load_data():
    clean_files = glob.glob("data/*_clean.csv")
    if not clean_files:
        return None
    dfs = [pd.read_csv(f) for f in clean_files]
    df = pd.concat(dfs, ignore_index=True)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df_all = load_data()

if df_all is not None:
    # Country multi-select
    countries = st.sidebar.multiselect(
        "Select Countries",
        options=sorted(df_all['Country'].unique()),
        default=df_all['Country'].unique()
    )

    # Year range slider
    min_year = int(df_all['Date'].dt.year.min())
    max_year = int(df_all['Date'].dt.year.max())
    year_range = st.sidebar.slider(
        "Year Range",
        min_value=min_year,
        max_value=max_year,
        value=(min_year, max_year)
    )

    # Variable selector
    variable = st.sidebar.selectbox(
        "Climate Variable",
        options=['T2M', 'T2M_MAX', 'T2M_MIN', 'PRECTOTCORR', 'RH2M', 'WS2M'],
        index=0
    )

    # Filter data
    mask = (df_all['Country'].isin(countries)) & \
           (df_all['Date'].dt.year >= year_range[0]) & \
           (df_all['Date'].dt.year <= year_range[1])
    df_filtered = df_all.loc[mask]

    # Dashboard layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"Average {variable} Over Time")
        fig_line = px.line(
            df_filtered.groupby(['Country', pd.Grouper(key='Date', freq='M')])[variable].mean().reset_index(),
            x='Date', y=variable, color='Country',
            template="plotly_white"
        )
        st.plotly_chart(fig_line, use_container_width=True)

    with col2:
        st.subheader(f"{variable} Distribution")
        fig_box = px.box(
            df_filtered,
            x='Country', y=variable, color='Country',
            template="plotly_white"
        )
        if variable == 'PRECTOTCORR':
            fig_box.update_yaxes(type="log")
        st.plotly_chart(fig_box, use_container_width=True)

    # Metrics
    st.subheader("Key Statistics")
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    avg_val = df_filtered[variable].mean()
    max_val = df_filtered[variable].max()
    min_val = df_filtered[variable].min()
    std_val = df_filtered[variable].std()

    m_col1.metric(f"Mean {variable}", f"{avg_val:.2f}")
    m_col2.metric(f"Max {variable}", f"{max_val:.2f}")
    m_col3.metric(f"Min {variable}", f"{min_val:.2f}")
    m_col4.metric(f"Std Dev", f"{std_val:.2f}")

else:
    st.warning("No cleaned datasets found in the `data/` directory. Please run the EDA notebooks first.")
    st.info("Ensure files like `ethiopia_clean.csv` are present in `climate-challenge-week0/data/`.")
