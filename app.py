import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

# Page layout optimization
st.set_page_config(layout="wide", page_title="Amazon Sales Dashboard")

# Load cleaned dataset
sales_data = pd.read_csv("data/Amazonsales_cleaned.csv")

# Fix date format issue
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'], dayfirst=True, errors='coerce')
sales_data = sales_data.dropna(subset=['Order Date'])
sales_data['Year'] = sales_data['Order Date'].dt.year

# Sidebar navigation
st.sidebar.title("📊 Amazon Sales Dashboard")
option = st.sidebar.radio("Select Analysis:",
                          ["Yearly Sales by Product", "Probability of Sales", "Top 5 Most Profitable Products",
                           "Sales Forecasting"])

# Option 1: Yearly Sales by Product
if option == "Yearly Sales by Product":
    st.header("📈 Yearly Sales by Product")

    category_selected = st.sidebar.selectbox("Select Category:", sales_data["Category"].unique())
    category_data = sales_data[sales_data["Category"] == category_selected]

    product_selected = st.sidebar.selectbox("Select Product:", category_data["Product Name"].unique())
    product_data = category_data[category_data["Product Name"] == product_selected]

    yearly_sales = product_data.groupby("Year")["Sales"].sum().reset_index()

    # Color coding for sales
    def get_color(sales):
        if sales < yearly_sales["Sales"].quantile(0.33):
            return "red"
        elif sales < yearly_sales["Sales"].quantile(0.66):
            return "blue"
        else:
            return "green"

    yearly_sales["Color"] = yearly_sales["Sales"].apply(get_color)

    fig = px.bar(yearly_sales, x="Year", y="Sales", title=f"Yearly Sales for {product_selected}",
                 color=yearly_sales["Color"], color_discrete_map={"red": "red", "blue": "blue", "green": "green"})

    fig.update_xaxes(type='category')
    st.plotly_chart(fig, use_container_width=True)

# ✅ Fixed Option 2: Probability of Sales
elif option == "Probability of Sales":
    st.header("📦 Probability of Sales for 2016")

    # Step 1: Select Category
    category_selected = st.sidebar.selectbox("Select Category:", sales_data["Category"].unique())

    # Filter data for the selected category
    category_data = sales_data[sales_data["Category"] == category_selected]

    # Find valid products (having sales data for 2014 & 2015)
    valid_products = []
    for product in category_data["Product Name"].unique():
        product_sales = category_data[category_data["Product Name"] == product]
        sales_2014 = product_sales[product_sales['Year'] == 2014]['Sales'].sum()
        sales_2015 = product_sales[product_sales['Year'] == 2015]['Sales'].sum()

        if sales_2014 > 0 or sales_2015 > 0:
            valid_products.append(product)

    # If no valid products, show a message
    if not valid_products:
        st.write("❌ No products found with sales data for 2014 & 2015 in this category.")
    else:
        # Step 2: Select Product from filtered list
        product_selected = st.sidebar.selectbox("Select Product:", valid_products)

        # Step 3: Compute Probability
        product_sales = category_data[category_data['Product Name'] == product_selected]
        sales_2014 = product_sales[product_sales['Year'] == 2014]['Sales'].sum()
        sales_2015 = product_sales[product_sales['Year'] == 2015]['Sales'].sum()

        # Handle missing values
        if sales_2014 == 0:
            sales_2014 = product_sales['Sales'].mean()  # Use the average sales
        if sales_2015 == 0:
            sales_2015 = sales_2014 * 1.1  # Assume a 10% increase if missing

        # Compute estimated sales for 2016
        estimated_sales_2016 = (0.4 * sales_2014) + (0.6 * sales_2015)

        # Compute probability
        total_sales_2014_2015 = sales_2014 + sales_2015
        probability_2016 = estimated_sales_2016 / total_sales_2014_2015 if total_sales_2014_2015 > 0 else 0

        # Display results
        st.write(f"### Estimated Sales for {product_selected} in 2016: **{estimated_sales_2016:.2f}**")
        st.write(f"### Probability of 2016 sales based on 2014-2015: **{probability_2016:.2f}**")

# Option 3: Top 5 Most Profitable Products
elif option == "Top 5 Most Profitable Products":
    st.header("📌 Top 5 Most Profitable Products")

    top_products = sales_data.groupby("Product Name")["Profit"].sum().reset_index()
    top_products = top_products.sort_values(by="Profit", ascending=False).head(5)

    fig_top5 = px.bar(top_products, x="Product Name", y="Profit", title="Top 5 Most Profitable Products",
                      color="Profit", color_continuous_scale=["red", "orange", "green"])

    fig_top5.update_xaxes(tickangle=45)
    st.plotly_chart(fig_top5, use_container_width=True)

# Option 4: Sales Forecasting
elif option == "Sales Forecasting":
    st.header("📊 Sales Forecasting")

    sales_by_year = sales_data.groupby("Year")["Sales"].sum().reset_index()

    X = sales_by_year["Year"].values.reshape(-1, 1)
    y = sales_by_year["Sales"].values
    model = LinearRegression()
    model.fit(X, y)

    future_years = np.array(range(sales_by_year["Year"].min(), sales_by_year["Year"].max() + 6)).reshape(-1, 1)
    predicted_sales = model.predict(future_years)

    fig_forecast = go.Figure()
    fig_forecast.add_trace(go.Scatter(x=sales_by_year["Year"], y=sales_by_year["Sales"],
                                      mode='lines+markers', name='Actual Sales', marker=dict(size=8, color='blue'),
                                      hoverinfo='x+y'))
    fig_forecast.add_trace(go.Scatter(x=future_years.flatten(), y=predicted_sales,
                                      mode='lines+markers', name='Predicted Sales',
                                      line=dict(dash='dash', color='green'), hoverinfo='x+y'))

    selected_year = st.selectbox("Select a Year to View Details:", sales_by_year["Year"].unique())
    selected_data = sales_by_year[sales_by_year["Year"] == selected_year]

    fig_forecast.add_trace(go.Scatter(x=[selected_year], y=selected_data['Sales'].values,
                                      mode='markers', name=f"Sales for {selected_year}",
                                      marker=dict(size=12, color='red')))

    fig_forecast.update_layout(title="Sales Forecasting", xaxis_title="Year", yaxis_title="Sales",
                               legend_title="Legend")
    st.plotly_chart(fig_forecast, use_container_width=True)

    if not selected_data.empty:
        st.write(f"### Details for Year {selected_year}")
        st.write(f"Total Sales: {selected_data['Sales'].values[0]}")
