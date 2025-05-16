# ikea_app.py (This is the code we finalized earlier)

import streamlit as st

# --- Product Catalog ---
products = {
    "BILLY Bookcase": 4000,
    "POANG Chair": 6000,
    "LACK Table": 800,
    "FABLER Bjorn Toy": 500
}

# --- Calculation Functions ---
def calculate_initial_total(qty_bookcase, qty_chair, qty_table, qty_toy):
    total = (products["BILLY Bookcase"] * qty_bookcase) + \
            (products["POANG Chair"] * qty_chair) + \
            (products["LACK Table"] * qty_table) + \
            (products["FABLER Bjorn Toy"] * qty_toy)
    return total

def calculate_final_details(initial_total):
    discount_percent = 0
    discount_amount = 0.0
    if initial_total >= 10000:
        discount_percent = 10
    elif initial_total >= 5000:
        discount_percent = 5
    if discount_percent > 0:
        discount_amount = (initial_total * discount_percent) / 100
    final_price = initial_total - discount_amount
    return final_price, discount_percent, discount_amount

# --- Streamlit App Interface ---
st.set_page_config(page_title="IKEA Quick Calculator", layout="centered")
st.title("IKEA Simple Order Calculator 🛒")
st.header("Enter Quantities Purchased:")
col1, col2 = st.columns(2)
with col1:
    qty_b = st.number_input(f"BILLY Bookcase ({products['BILLY Bookcase']} INR)", min_value=0, step=1, key='b')
    qty_t = st.number_input(f"LACK Table ({products['LACK Table']} INR)", min_value=0, step=1, key='t')
with col2:
    qty_c = st.number_input(f"POANG Chair ({products['POANG Chair']} INR)", min_value=0, step=1, key='c')
    qty_toy = st.number_input(f"FABLER Bjorn Toy ({products['FABLER Bjorn Toy']} INR)", min_value=0, step=1, key='toy')
st.markdown("---")
if st.button("Calculate Final Price 🧮", type="primary"):
    order_total = calculate_initial_total(qty_b, qty_c, qty_t, qty_toy)
    if order_total > 0:
        st.subheader("🧾 Order Summary")
        st.metric(label="Initial Total", value=f"{order_total:.2f} INR")
        final_amount, discount_applied, discount_value = calculate_final_details(order_total)
        if discount_applied > 0:
             st.metric(label="Discount Applied", value=f"{discount_applied}%", delta=f"-{discount_value:.2f} INR", delta_color="inverse")
             st.success(f"**Final Amount Payable: {final_amount:.2f} INR**")
        else:
             st.info("No discount applied on this order.")
             st.success(f"**Final Amount Payable: {order_total:.2f} INR**")
    else:
        st.warning("Please enter a quantity for at least one item to calculate the price.")
st.sidebar.header("About")
st.sidebar.info("Demo for Python Workshop!")
st.sidebar.markdown("Built with ❤️ using [Streamlit](https://streamlit.io)")