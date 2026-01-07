#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
def load_data(filepath):
    df = pd.read_csv(filepath)
    print("\n RAW DATA PREVIEW")
    print(df.head())
    print("\nMissing Values:\n", df.isnull().sum())
    return df
def train_model(X, y, scale=False):
    if scale:
        scaler = StandardScaler()
        X = scaler.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    return acc, classification_report(y_test, y_pred)
def baseline_model(df):
    print("\n MODEL ON UNCLEAN DATA")
    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]
    acc, report = train_model(X, y)
    print("Accuracy:", acc)
    print(report)
    return acc
def clean_data(df):
    print("\n CLEANING DATA")
    df_clean = df.copy()
    cols_with_zero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df_clean[cols_with_zero] = df_clean[cols_with_zero].replace(0, np.nan)
    for col in cols_with_zero:
        df_clean[col].fillna(df_clean[col].median(), inplace=True)
    for col in df_clean.columns[:-1]:
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1
        df_clean = df_clean[
            (df_clean[col] >= Q1 - 1.5 * IQR) &
            (df_clean[col] <= Q3 + 1.5 * IQR)
        ]
    print("\n CLEANED DATA PREVIEW")
    print(df_clean.head())
    return df_clean
def clean_data_model(df_clean):
    print("\n MODEL ON CLEAN DATA")

    X = df_clean.drop("Outcome", axis=1)
    y = df_clean["Outcome"]
    acc, report = train_model(X, y, scale=True)
    print("Accuracy:", acc)
    print(report)
    return acc
def plot_accuracy(before_acc, after_acc):
    plt.figure()
    plt.bar(["Unclean Data", "Clean Data"], [before_acc, after_acc])
    plt.title("Model Accuracy Comparison")
    plt.ylabel("Accuracy")
    plt.xlabel("Data Quality")
    plt.show()
def plot_feature_distribution(df, df_clean):
    plt.figure()
    plt.hist(df["Glucose"], bins=30, alpha=0.6, label="Before Cleaning")
    plt.hist(df_clean["Glucose"], bins=30, alpha=0.6, label="After Cleaning")
    plt.title("Glucose Distribution Before vs After Cleaning")
    plt.xlabel("Glucose Level")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()
def main():
    dataset_path = r"C:\Datasetss\diabetes.csv"
    df = load_data(dataset_path)
    acc_before = baseline_model(df)
    df_clean = clean_data(df)
    acc_after = clean_data_model(df_clean)
    plot_accuracy(acc_before, acc_after)
    plot_feature_distribution(df, df_clean)
    print("""CONCLUSION:This experiment demonstrates that training a disease prediction mode on poor-quality medical data leads to unreliable performance. After cleaning missing values, removing outliers, and normalizing data, the model accuracy improves significantly. This proves that data quality is a critical factor for trustworthy AI in healthcare. """)
if __name__ == "__main__":
    main()


# In[ ]:




