# 🏦 Bank Customer Churn Detection

A machine learning project to predict whether a bank customer will leave (churn) or stay, helping the bank take proactive retention actions.

---

## 📊 Overview
Customer churn refers to customers stopping the use of a company’s services.  
This project builds predictive models to **identify at-risk customers** using demographic and financial data.

---

## 📁 Dataset
**File:** `bank_customer_churn.csv`  
Each record represents a customer with the following key features:
- **CreditScore, Age, Geography, Gender, Tenure, Balance**
- **NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary**
- **Exited** → Target variable (1 = churned, 0 = retained)

---

## 🎯 Problem Statement
Develop a model to **predict customer churn** and provide insights into the factors driving attrition.  
This can help financial institutions reduce churn rates and improve customer satisfaction.

---

## ⚙️ Key Features
- **Data Preprocessing:** Cleaning, feature engineering, and handling class imbalance (SMOTE).  
- **EDA:** Visualization and pattern discovery using Pandas, Matplotlib, and Seaborn.  
- **Model Building:** Trained multiple algorithms — Logistic Regression, Decision Tree, Random Forest.  
- **Model Evaluation:** Compared accuracy, precision, recall, and ROC-AUC metrics to choose the best model.

---

## 🧠 Tech Stack
- **Languages:** Python  
- **Libraries:** NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn  
- **Tools:** Jupyter Notebook

---

## 🚀 Results
- Achieved **~85% accuracy** on test data.  
- Identified key factors influencing churn (e.g., Credit Score, Age, Activity Level).  
- Demonstrated practical use of ML for real-world customer retention strategy.

---

## 🧩 Usage
1. Clone this repository:
   ```bash
   git clone https://github.com/Prathamgupta24/machinelearning_customerchunk.git
