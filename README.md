# 🧠 Customer Risk Prediction Dashboard

A Machine Learning web application that predicts a **customer's financial risk behavior** based on demographic and spending data.
The project uses a **Random Forest model** and is deployed through an interactive **Streamlit dashboard**.

---

# 🚀 Project Overview

Businesses often need to understand **customer risk behavior** to make better financial decisions.

This project analyzes:

* Customer demographics
* Income
* Spending behavior across categories

Using these features, the machine learning model predicts a **Risk Taking Score (1–5)** and categorizes customers into:

* Low Risk
* Medium Risk
* High Risk

---

# 📊 Features

✔ Interactive Streamlit dashboard
✔ Machine learning risk prediction
✔ Automatic feature engineering
✔ Real-time prediction using user input
✔ Risk visualization using a gauge meter
✔ Model confidence score display

---

# 🧾 Dataset

The dataset contains customer information such as:

* Age
* Annual Income
* Number of Children
* Fashion Spending
* Electronics Spending
* Grocery Spending
* Gender
* Marital Status
* Education

Additional engineered features include:

* Spending ratios
* Income per household member

---

# 🤖 Machine Learning Model

The model pipeline includes:

1. Data preprocessing
2. Feature engineering
3. One-hot encoding of categorical features
4. Feature scaling using StandardScaler
5. Model training using RandomForestClassifier

The trained pipeline is saved using **joblib** and loaded into the Streamlit app for prediction.

---

# 📁 Project Structure

```id="qex32h"
Customer Personality ML
│
├── data/
│   └── customer_personality.csv
│
├── model/
│   ├── pipeline.pkl
│   └── feature_columns.pkl
│
├── notebook/
│   └── MLproject.ipynb
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

# 🖥️ Running the Application

### 1 Install dependencies

```id="qz9m0n"
pip install -r requirements.txt
```

### 2 Run the Streamlit app

```id="0ur3pj"
python -m streamlit run streamlit_app.py
```

The app will open at:

```id="rppxqk"
http://localhost:8501
```

---

# 📈 Risk Score Interpretation

| Risk Score | Category    |
| ---------- | ----------- |
| 1 – 2      | Low Risk    |
| 3          | Medium Risk |
| 4 – 5      | High Risk   |

---

# 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Plotly
* Joblib

---

# 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud** for free hosting.

---

# 👨‍💻 Author

Developed as a **Machine Learning deployment project** demonstrating how predictive models can be integrated into interactive web applications.
