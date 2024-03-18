import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import TimeSeriesSplit
from sklearn.preprocessing import StandardScaler
import shap

df = pd.read_csv(
    r"C:\Users\Tycia\Desktop\GitHub\Python prywatny\e-commerce_data\data.csv",
    encoding="ISO-8859-1")
# print(df.shape)
# print(df.head())
print(df.info())
print(df["UnitPrice"])
df["CustomerID"] = df["CustomerID"].astype(str)
df['UnitPrice'] = df['UnitPrice'].astype('float32')
print(df.info())

print(df["UnitPrice"])
# missing_percentage = data.isnull().sum() / data.shape[0] * 100
# print(missing_percentage)
#
# print(data[data.Description.isnull()].head())
# print(data[data.Description.isnull()].CustomerID.isnull().value_counts())
# print(data[data.Description.isnull()].UnitPrice.value_counts())
# print(data[data.CustomerID.isnull()].head())



