# Aggregration Functions in Pandas
import pandas as pd
# Sample DataFrame
grouped = df.groupby("column_name")

for name, group in grouped:
    print(name)
    print(group)
 # Using the groupby method to aggregate data   
grouped.mean()
grouped.sum()

df.groupby("category_column")["numeric_column"].mean()
df.groupby("category_column").agg({"numeric_column":["mean", "max", "min"]})

# Using pivot_table to aggregate data

pivot = df.pivot_table(
    values="numeric_column",
    index="category_column",
    aggfunc="mean"
)

# Using custom aggregation functions


def range_func(x):
    return x.max() - x.min()

df.groupby("category_column")["numeric_column"].agg(range_func)

df.groupby("category_column")["numeric_column"].mean()
df.groupby("category_column")["numeric_column"].max()
df.groupby("category_column")["numeric_column"].min()

df.groupby("category_column").agg(
    {"numeric_column": ["mean", "max", "min"]}
)









