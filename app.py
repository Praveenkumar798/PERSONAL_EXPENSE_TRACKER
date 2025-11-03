import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from utils import load_data, save_data

# ---- Page Settings ----
st.set_page_config(page_title="Personal Expense Tracker", page_icon="💰", layout="wide")

# ---- App Title ----
st.title("💰 PERSONAL EXPENSE TRACKER")
st.write("Track your daily expenses and visualize your spending easily!")

# ---- Load existing data ----
data = load_data()
if not data.empty:
    data['Date'] = pd.to_datetime(data['Date'])

# ---- Sidebar Filters ----
st.sidebar.header("📊 Filter Options")

# Date range filter
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(datetime.now().date() - timedelta(days=30), datetime.now().date()),
    max_value=datetime.now().date()
)

# Category filter
all_categories = ["All"] + sorted(data['Category'].unique().tolist() if not data.empty else [])
selected_category = st.sidebar.selectbox("Select Category", all_categories)

# Note search
search_note = st.sidebar.text_input("Search in Notes", "")

# Apply filters
if not data.empty:
    mask = (data['Date'].dt.date >= date_range[0]) & (data['Date'].dt.date <= date_range[1])
    if selected_category != "All":
        mask &= data['Category'] == selected_category
    if search_note:
        mask &= data['Note'].str.contains(search_note, case=False, na=False)
    filtered_data = data[mask]
else:
    filtered_data = data

# ---- Expense Input Form ----
st.subheader("➕ Add New Expense")

with st.form("expense_form"):
    date = st.date_input("Date")
    category = st.selectbox(
        "Category",
        ["Food", "Travel", "Shopping", "Bills", "Entertainment", "Other"]
    )
    amount = st.number_input("Amount (₹)", min_value=0.0, step=0.1)
    note = st.text_input("Note (optional)")
    submitted = st.form_submit_button("Add Expense")

    if submitted:
        new_entry = {"Date": date, "Category": category, "Amount": amount, "Note": note}
        data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)
        save_data(data)
        st.success("✅ Expense added successfully!")

# ---- Summary Statistics ----
if not filtered_data.empty:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Expenses", f"₹{filtered_data['Amount'].sum():,.2f}")
    with col2:
        st.metric("Average Expense", f"₹{filtered_data['Amount'].mean():,.2f}")
    with col3:
        st.metric("Number of Transactions", len(filtered_data))

# ---- Show Table ----
st.subheader("📋 Your Expenses")
if not filtered_data.empty:
    st.dataframe(
        filtered_data.sort_values('Date', ascending=False),
        column_config={
            "Date": "Date",
            "Category": "Category",
            "Amount": st.column_config.NumberColumn("Amount", format="₹%.2f"),
            "Note": "Note"
        },
        hide_index=True
    )
    
    # Export button
    csv = filtered_data.to_csv(index=False)
    st.download_button(
        "⬇️ Download Filtered Data",
        csv,
        "expenses_export.csv",
        "text/csv",
        key='download-csv'
    )
else:
    st.info("No expenses found for the selected filters.")

# ---- Display Charts ----
if not filtered_data.empty:
    # Create two columns for charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Spending by Category")
        category_totals = filtered_data.groupby("Category")["Amount"].sum()
        
        # Bar chart
        fig1, ax1 = plt.subplots()
        category_totals.plot(kind="bar", ax=ax1, color="skyblue")
        plt.xticks(rotation=45)
        plt.xlabel("Category")
        plt.ylabel("Total Spent (₹)")
        st.pyplot(fig1)
        
    with col2:
        st.subheader("🥧 Category Distribution")
        # Pie chart
        fig2, ax2 = plt.subplots()
        category_totals.plot(kind="pie", autopct='%1.1f%%', ax=ax2)
        plt.axis('equal')
        st.pyplot(fig2)
    
    # Monthly trend
    st.subheader("📈 Monthly Spending Trend")
    monthly_data = filtered_data.set_index('Date').resample('M')['Amount'].sum().reset_index()
    
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    ax3.plot(monthly_data['Date'], monthly_data['Amount'], marker='o')
    plt.xticks(rotation=45)
    plt.xlabel("Month")
    plt.ylabel("Total Spent (₹)")
    st.pyplot(fig3)
else:
    st.info("No data yet! Add your first expense above 👆")