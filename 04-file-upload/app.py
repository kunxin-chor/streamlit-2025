import streamlit as st
import pandas as pd
import plotly.express as px


@st.cache_data()
def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    # Try to convert any date-like columns to datetime
    for col in df.columns:
        if any(keyword in col.lower() for keyword in ['date', 'time', 'datetime']):
            df[col] = pd.to_datetime(df[col], errors='ignore')
        else:
            # Try to parse columns with object type and at least one value that looks like a date
            sample = df[col].astype(str).head(10)
            try:
                parsed = pd.to_datetime(sample, errors='raise')
                df[col] = pd.to_datetime(df[col], errors='ignore')
            except Exception:
                pass
    return df


# File uploader
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Load data from the uploaded file
    df = load_data(uploaded_file)

    st.title("Interactive Data Dashboard")

    # Select column to filter by
    filter_column = st.sidebar.selectbox('Select column to filter by', df.columns)
    unique_values = df[filter_column].unique().tolist()
    selected_values = st.sidebar.multiselect(f'Select values for {filter_column}', unique_values)

    if selected_values:
        df_filtered = df[df[filter_column].isin(selected_values)]
    else:
        df_filtered = df

    st.dataframe(df_filtered)

    # Visualization Section
    st.subheader('Data Visualizations')

    if len(selected_values) == 0:
        st.write(f"Select one or more {filter_column} values to see visualizations")

    # Bar Chart
    if selected_values:
        st.subheader(f'Bar Chart')
        bar_x = st.selectbox('Bar Chart - X axis', options=df_filtered.columns, key='bar_x')
        bar_y = st.selectbox('Bar Chart - Y axis', options=df_filtered.columns, key='bar_y')
        if bar_x and bar_y:
            fig = px.bar(df_filtered, x=bar_x, y=bar_y,
                         labels={bar_y: bar_y.title(), bar_x: bar_x.title()},
                         color=bar_x,
                         barmode='group')
            st.plotly_chart(fig)

    # Line Chart
    if selected_values:
        st.subheader('Line Chart')
        line_x = st.selectbox('Line Chart - X axis', options=df_filtered.columns, key='line_x')
        line_y = st.selectbox('Line Chart - Y axis', options=df_filtered.columns, key='line_y')
        if line_x and line_y:
            fig = px.line(df_filtered, x=line_x, y=line_y, color=filter_column,
                          labels={line_y: line_y.title(), line_x: line_x.title(), filter_column: filter_column.title()},
                          title=f'Line Chart: {line_y.title()} vs {line_x.title()} by {filter_column}')
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig)

    # Box Plot
    if selected_values:
        st.subheader('Box Plot')
        box_x = st.selectbox('Box Plot - X axis', options=df_filtered.columns, key='box_x')
        box_y = st.selectbox('Box Plot - Y axis', options=df_filtered.columns, key='box_y')
        if box_x and box_y:
            fig = px.box(df_filtered, x=box_x, y=box_y, 
                         labels={box_y: box_y.title(), box_x: box_x.title()},
                         title=f'Box Plot: {box_y.title()} by {box_x.title()}')
            st.plotly_chart(fig)
else:
    st.title("Interactive Data Dashboard")
    st.write("Please upload a CSV file to proceed.")