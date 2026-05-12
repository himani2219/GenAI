import streamlit as st

st.title("Product form")
st.sidebar.header("Product details")
product_name = st.sidebar.text_input("Product name:")
category = st.sidebar.selectbox("Category:", ["Electronics", "Clothing", "Books"])
price = st.sidebar.number_input("Price:")
button_clicked = st.sidebar.button("Add product")
if "products" not in st.session_state:
    st.session_state.products = []
if button_clicked:
    st.session_state.products.append((product_name, category, price))
    st.success(f"Product added successfully")
if st.session_state.products:
    st.subheader("Product List")
    st.table(st.session_state.products)

