import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Consumer Shopping Behavior Dashboard", layout="wide")

st.title("🛒 Consumer Shopping Behavior Interactive Dashboard")

# --- Load Data ---
DATA_PATH = "dataset/Consumer_Shopping_Behavior_dataset.csv"
df = pd.read_csv(DATA_PATH)
df.columns = df.columns.str.strip()

# --- Sidebar Filters ---
st.sidebar.header("Filter Data")
if 'Gender' in df.columns:
    genders = st.sidebar.multiselect("Gender", options=df['Gender'].unique(), default=df['Gender'].unique())
    df = df[df['Gender'].isin(genders)]

if 'Location' in df.columns:
    locations = st.sidebar.multiselect("Location", options=df['Location'].unique(), default=df['Location'].unique())
    df = df[df['Location'].isin(locations)]

if 'Category' in df.columns:
    categories = st.sidebar.multiselect("Category", options=df['Category'].unique(), default=df['Category'].unique())
    df = df[df['Category'].isin(categories)]

# --- KPIs ---
st.header("📈 Key Performance Indicators")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

purchase_col = 'Purchase Amount (USD)'
if purchase_col in df.columns:
    with kpi1:
        st.metric("Total Revenue", f"$ {df[purchase_col].sum():,.0f}")
    with kpi3:
        st.metric("Avg. Purchase Size", f"$ {df[purchase_col].mean():.2f}")
else:
    with kpi1:
        st.metric("Total Revenue", "N/A")
    with kpi3:
        st.metric("Avg. Purchase Size", "N/A")

if 'Customer ID' in df.columns:
    with kpi2:
        st.metric("Total Customers", df['Customer ID'].nunique())
else:
    with kpi2:
        st.metric("Total Customers", "N/A")

with kpi4:
    st.metric("Transactions", f"{len(df):,}")

st.markdown("---")

# --- Visualizations ---

# Sales by Category
st.subheader("Sales by Category")
if 'Category' in df.columns and purchase_col in df.columns:
    cat_sales = df.groupby('Category')[purchase_col].sum().reset_index()
    fig_cat = px.bar(
        cat_sales,
        x='Category',
        y=purchase_col,
        title="Total Revenue by Category",
        color=purchase_col,
        text_auto='.2s'
    )
    st.plotly_chart(fig_cat, use_container_width=True)

# Customer Demographics
st.subheader("Customer Demographics")
demo_cols = st.columns(2)
with demo_cols[0]:
    if 'Gender' in df.columns:
        fig_gender = px.pie(df, names='Gender', title="Gender Distribution", hole=0.4)
        st.plotly_chart(fig_gender, use_container_width=True)

with demo_cols[1]:
    if 'Age' in df.columns:
        fig_age = px.histogram(df, x='Age', nbins=10, title="Customer Age Distribution", color='Gender' if 'Gender' in df.columns else None)
        st.plotly_chart(fig_age, use_container_width=True)

# Top Locations by Revenue
st.subheader("Top Locations by Revenue")
if 'Location' in df.columns and purchase_col in df.columns:
    loc_sales = df.groupby('Location')[purchase_col].sum().reset_index().sort_values(by=purchase_col, ascending=False).head(10)
    fig_loc = px.bar(loc_sales, x='Location', y=purchase_col, title="Top 10 Locations by Revenue", color=purchase_col)
    st.plotly_chart(fig_loc, use_container_width=True)

# Review Rating Distribution
st.subheader("Review Rating Distribution")
if 'Review Rating' in df.columns:
    fig_rating = px.histogram(df, x='Review Rating', nbins=5, title="Review Rating Distribution", color='Review Rating')
    st.plotly_chart(fig_rating, use_container_width=True)

# Sales Trend Over Time
st.subheader("Sales Trend Over Time")
if 'Previous Purchase' in df.columns and purchase_col in df.columns:
    try:
        df['Previous Purchase'] = pd.to_datetime(df['Previous Purchase'], errors='coerce')
        trend = df.dropna(subset=['Previous Purchase']).copy()
        trend['Month'] = trend['Previous Purchase'].dt.to_period('M').dt.to_timestamp()
        time_sales = trend.groupby('Month')[purchase_col].sum().reset_index()
        fig_time = px.line(time_sales, x='Month', y=purchase_col, title="Monthly Sales Trend")
        st.plotly_chart(fig_time, use_container_width=True)
    except Exception as e:
        st.warning("Could not parse 'Previous Purchase' as dates.")

# Payment Method Preferences
st.subheader("Payment Method Preferences")
if 'Payment Method' in df.columns:
    fig_payment = px.pie(df, names='Payment Method', title="Payment Method Preferences")
    st.plotly_chart(fig_payment, use_container_width=True)

# Subscription Status
st.subheader("Subscription Status Distribution")
if 'Subscription Status' in df.columns:
    fig_sub = px.pie(df, names='Subscription Status', title="Subscription Status Distribution")
    st.plotly_chart(fig_sub, use_container_width=True)

# Frequency of Purchase
st.subheader("Purchase Frequency Distribution")
if 'Frequency of Purchase' in df.columns:
    freq_counts = df['Frequency of Purchase'].value_counts().reset_index()
    freq_counts.columns = ['Frequency', 'Count']
    fig_freq = px.bar(freq_counts, x='Frequency', y='Count', title="Purchase Frequency Distribution", color='Count')
    st.plotly_chart(fig_freq, use_container_width=True)

# Discount Applied
st.subheader("Discount Applied Distribution")
if 'Discount Applied' in df.columns:
    fig_discount = px.pie(df, names='Discount Applied', title="Discount Applied Distribution")
    st.plotly_chart(fig_discount, use_container_width=True)

st.markdown("---")

# --- Data Explorer ---
st.subheader("🔍 Data Preview")
st.dataframe(df.head(100), use_container_width=True)

# --- Screenshots Section ---
st.subheader("📸 Dashboard Screenshots")
img_cols = st.columns(3)
screenshot_dir = "screenshots"
screenshots = ["dashboard_overview.png", "kpi_section.png", "visuals_analysis.png"]
captions = ["Dashboard Overview", "KPI Section", "Visuals Analysis"]
for idx, img_name in enumerate(screenshots):
    img_path = os.path.join(screenshot_dir, img_name)
    if os.path.exists(img_path):
        with img_cols[idx]:
            st.image(img_path, caption=captions[idx], use_container_width=True)
