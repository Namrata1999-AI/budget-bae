import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="💰 Budget Bae", layout="wide")

st.markdown("<h1 style='text-align: center; color: #FF6F61;'>💁‍♀️ Budget Bae: Your Sassy Saving Sidekick!</h1>", unsafe_allow_html=True)
st.markdown("#### 💡 Enter your income & expenses, and let Budget Bae help you save like a queen!")

# Layout: Two columns for input
col1, col2 = st.columns(2)

with col1:
    income = st.number_input("💸 Monthly Income", min_value=0, step=100)

with col2:
    rent = st.number_input("🏠 Rent", min_value=0, step=100)
    groceries = st.number_input("🛒 Groceries", min_value=0, step=100)
    entertainment = st.number_input("🎉 Entertainment", min_value=0, step=100)
    other = st.number_input("📦 Other Expenses", min_value=0, step=100)

if st.button("✨ Show Budget Summary"):
    total_expenses = rent + groceries + entertainment + other
    savings = income - total_expenses
    percent_saved = (savings / income) * 100 if income > 0 else 0

    st.markdown("---")
    st.subheader("📊 Budget Summary")

    col3, col4 = st.columns([2, 1])
    with col3:
        data = {
            "Category": ["Rent", "Groceries", "Entertainment", "Other"],
            "Amount": [rent, groceries, entertainment, other]
        }
        df = pd.DataFrame(data)
        fig = px.pie(df, names="Category", values="Amount", title="Expense Breakdown")
        st.plotly_chart(fig, use_container_width=True)

    with col4:
        st.success(f"💰 **Total Savings**: ₹{savings:,.2f}")
        st.info(f"📈 **Savings Rate**: {percent_saved:.2f}%")

        if percent_saved < 20:
            st.warning("🚨 Try to save at least 20% of your income!")
        else:
            st.balloons()
            st.success("🎉 Great job saving! Budget Bae approves! 💅")