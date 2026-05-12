import streamlit as st

st.title("Price calculator")
price = st.number_input("Enter the price of the item:", key="price")
discount = st.slider("Select the discount percentage:", 0, 50, key="discount")
button_clicked = st.button("Calculate final price")
if "comparison" not in st.session_state:
    st.session_state.comparison = []
if button_clicked:
    final_price = price * (1 - discount / 100)
    st.session_state.comparison.append([price, discount, final_price])
    st.success(f"Original price: {price}, Discount: {discount}%, Final price: {final_price}")

if st.session_state.comparison:
    st.subheader("Price Comparison")
    st.table(st.session_state.comparison)