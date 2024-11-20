# Questions -
"""
Count of Cancellation booking in and show in graph.
Graph representing cancellation based on hotel (city hotel, resort hotel)
Reservation and cancellation by months
We dont have month columns so we need to extract the month from datetime column
Country wise cancellation of hotels
"""


# CODE -
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("hotel_bookings 2.csv")
print(df.head(10))
print(df.shape)
print(df.columns)
print(df.info()) # info() is used to check the datatype of the columns.

# Convert the reservation_status_date into datetime format
df["reservation_status_date"] = pd.to_datetime(df["reservation_status_date"])
print(df.info())

# uniques values does each column have
# print(df.describe(include = "object"))
# Showing values
for col in df.describe(include = "object").columns:
    print(col)
    print(df[col].unique())
    print("-"*50)


# Finding Missing values
#print(df.isnull().sum())

# Dropping the columns which have large amount of missing values
df.drop(["company", "agent"],axis = 1, inplace = True)
df.dropna(inplace=True)
print(df.isnull().sum())


# Count of Cancellation of bookings and show in the graph
cancelled = df["is_canceled"].value_counts(normalize = True)
print(cancelled)
plt.figure(figsize=(6, 4))
plt.title("Reservation count ")
plt.bar(["Not canceled", "Canceled"], df["is_canceled"].value_counts(), width = 0.7)
plt.show()


# Graph representing cancellation based on hotel (city hotel, resort hotel)
plt.figure(figsize=(6, 4))
ax1 = sns.countplot(x= "hotel", hue = "is_canceled", data = df, palette = "Blues")
plt.title("Reservation status in different hotels ", size = 20)
plt.xlabel("hotel")
plt.ylabel("number of reservations")
plt.legend(["Not Canceled", "Canceled"])
plt.show()


# Reservation and cancellation by months
df["month"] = df["reservation_status_date"].dt.month
plt.figure(figsize=(10, 8))
ax1 = sns.countplot(x = "month", hue = "is_canceled", data = df)
plt.title("Reservation status per month ")
plt.xlabel("month")
plt.ylabel("number of reservations")
plt.legend(["not canceled", "canceled"])
plt.show()


# Country wise cancellation of hotels
cancelled_data = df[df["is_canceled"] == 1]
top_10_country = cancelled_data["country"].value_counts()[:10]
plt.figure(figsize=(8, 8))
plt.title("Top 10 country wise reservation canceled")
plt.pie(top_10_country, autopct= "%.2f", labels=top_10_country.index)
plt.show()




