import streamlit as st

def calculate_simple_interest(principal, rate, rate_unit, time, time_unit):
    # Adjust rate if it's in rupees
    if rate_unit == "r":
        rate *= 12

    # Convert time to years
    if time_unit == "m":
        time_in_years = time / 12
        period = "month"
    elif time_unit == "w":
        time_in_years = time / 48
        period = "week"
    else:
        time_in_years = time
        period = "year"
    
    # Calculate interest and total amount
    interest = (principal * time_in_years * rate) / 100
    total_amount = interest + principal
    payment_per_period = total_amount / time if time != 0 else 0
    
    return rate / 12, interest, total_amount, payment_per_period, period

st.set_page_config(page_title="Simple Interest Calculator", layout="centered")
st.title("📊 Simple Interest Calculator")

st.markdown("""
<style>
    @media (max-width: 768px) {
        .block-container {
            padding: 10px;
        }
    }
</style>
""", unsafe_allow_html=True)

principal = st.number_input("Enter Principal Amount (₹):", min_value=0.0, step=100.0)
rate_unit = st.selectbox("Select Interest Rate Unit:", ["Percentage (p)", "Rupees (r)"])
rate = st.number_input("Enter Interest Rate:", min_value=0.0, step=0.1)
time_unit = st.selectbox("Select Time Unit:", ["Weeks (w)", "Months (m)", "Years (y)"])
time = st.number_input("Enter Time Period:", min_value=0.0, step=1.0)

if st.button("Calculate"):
    # Convert units to code logic format
    rate_unit_code = "p" if "Percentage" in rate_unit else "r"
    time_unit_code = "w" if "Weeks" in time_unit else ("m" if "Months" in time_unit else "y")
    
    # Perform calculation
    monthly_rate, interest, total_amount, payment_per_period, period = calculate_simple_interest(
        principal, rate, rate_unit_code, time, time_unit_code
    )
    
    # Display results
    st.success(f"Your monthly interest rate is: {monthly_rate:.2f}%")
    st.info(f"Interest amount is: ₹{interest:,.0f}")
    st.info(f"Total amount to be paid: ₹{total_amount:,.0f}")
    st.info(f"Amount to pay per {period}: ₹{payment_per_period:,.0f}")
