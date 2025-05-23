# Pandas data struccture
import pandas as pd
#series
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s)
#dataframes
data = {"Name": ["Abdulkareem", "Abdulmateen"], "Age": [55, 22]}
df = pd.DataFrame(data)
print(df)

# loading data from csv excel and other souce

df = pd.read_csv("data.csv")
df = pd.read_excel("data.xlsx")

# saving data : saving in csv and excel
df.to_csv("data.csv", index=False)
df.to_excel("data.xlsx", index=False)

# Viewing Data

print(df.head())

print(df.tail())

# summarry of dataframe
print(df.info())

# statistical summary
print(df.describe())

# selecting by data column/s

print(df[df["Age", "Name"]])

print(df[df["Age"] > 25])  # by filtering

# selecting by data row

print(df.iloc[0]) # first row

print(df.iloc[:, 0]) # by position

# selecting by label

print(df.iloc[0])
print(df.iloc[:, "Name"])