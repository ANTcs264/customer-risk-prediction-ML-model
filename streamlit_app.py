import streamlit as st
import pandas as pd
import joblib

pipeline = joblib.load("model/pipeline.pkl")
feature_cols = joblib.load("model/feature_columns.pkl")

st.set_page_config(
    page_title="Customer Risk Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------- Header ----------
st.markdown("""
# 🧠 Customer Risk Prediction Dashboard
Predict customer risk behaviour using demographic and spending data.
""")

st.caption("💰 All monetary values are in Indian Rupees (₹)")

st.divider()

# ---------- Sidebar ----------
st.sidebar.title("⚙ Customer Inputs")

age = st.sidebar.slider("Age", 18, 70, 30)
income = st.sidebar.number_input("Annual Income (₹)", 10000, 2000000, 500000)
children = st.sidebar.slider("Children", 0, 5, 1)

gender = st.sidebar.selectbox("Gender", ["Male","Female"])
marital = st.sidebar.selectbox("Marital Status", ["Single","Married","Divorced"])
education = st.sidebar.selectbox("Education", ["Basic","Bachelor","Master","PhD"])

st.sidebar.divider()
st.sidebar.subheader("Shopping Behaviour")

fashion = st.sidebar.slider("Fashion Spend (₹)", 0, 100000, 5000)
electronics = st.sidebar.slider("Electronics Spend (₹)", 0, 100000, 5000)
grocery = st.sidebar.slider("Grocery Spend (₹)", 0, 100000, 5000)

total = fashion + electronics + grocery

# ---------- Dashboard Metrics ----------
st.subheader("Customer Summary")

col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Spending", f"₹{total:,.0f}")
col2.metric("💵 Annual Income", f"₹{income:,.0f}")
col3.metric("👨‍👩‍👧 Children", children)

st.divider()

# ---------- Tabs ----------
tab1, tab2 = st.tabs(["Prediction", "Input Summary"])

# ---------- Prediction ----------
with tab1:

   if st.button("🚀 Predict Customer Risk"):

    with st.spinner("Analyzing customer profile..."):

        row = {col:0 for col in feature_cols}

        row["Age"] = age
        row["Annual_Income"] = income
        row["Children"] = children

        row["Category_Fashion_Spend"] = fashion
        row["Category_Electronics_Spend"] = electronics
        row["Category_Grocery_Spend"] = grocery
        row["Total_Spend"] = total

        if total > 0:
            row["Fashion_to_Total"] = fashion/total
            row["Electronics_to_Total"] = electronics/total
            row["Grocery_to_Total"] = grocery/total

        row["Income_per_Person"] = income/(children+1)

        if f"Gender_{gender}" in row:
            row[f"Gender_{gender}"] = 1

        if f"Marital_Status_{marital}" in row:
            row[f"Marital_Status_{marital}"] = 1

        if f"Education_{education}" in row:
            row[f"Education_{education}"] = 1

        df = pd.DataFrame([row])

        prediction = pipeline.predict(df)[0]

    st.success("Prediction Complete")
    st.metric("Customer Risk Score", prediction)

    if prediction > 70:
        st.error("⚠ High Risk Customer")

    elif prediction > 40:
        st.warning("⚡ Medium Risk Customer")

    else:
        st.success("✅ Low Risk Customer")

# ---------- Input Summary ----------
with tab2:

    data = {
        "Age": age,
        "Income": income,
        "Children": children,
        "Fashion Spend": fashion,
        "Electronics Spend": electronics,
        "Grocery Spend": grocery
    }

    st.table(pd.DataFrame(data.items(), columns=["Feature","Value"]))