# HANDLING MISSING VALUES
import pandas as pd
# drop rows with any missing values in dataframe
df = df.dropna()

# drop column with any missing values in dataframe
df = df.dropna(axis =1)

# filling missing values in dataframe with zero
df["column_name"] = df["column_name"].fillna(0)

# filling missing values in dataframe based on interpolation
df["column_name"] = df["column_name"].interpolate()

# forward filling
df.fillna(method ="ffill")
# backword filling
df.fillna(method ="bfill")

# DATA TRANSFORMATION
# Renaming columns
df = df.rename(columns ={"old_name":"new_name"})
# Changing data types
df["column_name"] = df["column_name"].astype("float") # converting to float
df["column_name"] = df.to_datetime(df["column_name"]) # to datetime

# Creating or modifying colums
df["new_column"] = df["existing_column"] * 2

# combining and merging dataframe

# using concatenation
combined = pd.concat([df1, df2], axis=0) # along row
combined = pd.concat([df1, df2], axis=1) # along column
# using merging
merged = pd.merge(df1, df2, on="common_column")
merged = pd.merge(df1, df2, how="left", on="common_column")
merged = pd.merge(df1, df2, how="inner", on="common_column")

# using joining
joined = df1.join(df2, how="inner") # index allignment