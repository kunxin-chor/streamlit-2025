import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


@st.cache_data()
def load_data():
  df = pd.read_csv('./sales_records.csv')
  df['date_bought'] = pd.to_datetime(df['date_bought'])
  return df


df = load_data()

st.title("Interactive Data Dashboard")

# Multiselect for Categories
categories = df['category'].unique().tolist()
selected_categories = st.sidebar.multiselect('Select Categories', categories)

if selected_categories:
  df_filtered = df[df['category'].isin(selected_categories)]
else:
  df_filtered = df

st.dataframe(df_filtered)

# Visualization Section
st.subheader('Data Visualizations')

if len(selected_categories) == 0:
    st.write("Select one or more categories to see visualizations")

# Bar Chart
if selected_categories:
  st.subheader('Bar Chart: Sales by Category') 

  # Group by category and sum the sales
  category_sales = df_filtered.groupby('category')['price'].sum().reset_index()

  fig = px.bar(df_filtered, x='category', y='price',
     labels={'price': 'Sales', 'category': 'Category'},
     color='category',
     barmode='group')

  # Display the Plotly figure in Streamlit
  st.plotly_chart(fig)

# Line Chart

if selected_categories:
  st.subheader('Line Chart: Price Trend Over Time')
 
  # Create a line chart using Plotly
  fig = px.line(df_filtered, x='date_bought', y='price', color='category',
                labels={'price': 'Average Price', 'date_bought': 'Date', 'category': 'Category'},
                title='Price Trend Over Time')

  # Update x-axis tick angle
  fig.update_layout(xaxis_tickangle=-45)

  # Display the Plotly figure in Streamlit
  st.plotly_chart(fig)

# Box Plot
if selected_categories:
  st.subheader('Box Plot: Price Distribution by Category')

  # Filter the DataFrame for the selected categories
  df_selected = df_filtered[df_filtered['category'].isin(selected_categories)]

  # Create a box plot using Plotly
  fig = px.box(df_selected, x='category', y='price', 
               labels={'price': 'Price', 'category': 'Category'},
               title='Price Distribution by Category')

  # Display the Plotly figure in Streamlit
  st.plotly_chart(fig)