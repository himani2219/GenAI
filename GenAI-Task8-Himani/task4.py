import streamlit as st

st.title("Simple Sales Dashboard")
st.header("A platform to track sales performance")
months = st.selectbox("Select a month:", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
sales = {
    "January": 10000,
    "February": 15000,
    "March": 12000,
    "April": 18000,
    "May": 20000,
    "June": 22000,
    "July": 25000,
    "August": 30000,
    "September": 28000,
    "October": 35000,
    "November": 40000,
    "December": 45000
}
st.write(f"Sales for {months}: ${sales[months]}")
st.bar_chart(list(sales.values()))
