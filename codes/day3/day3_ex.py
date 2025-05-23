import kagglehub

path = kagglehub.dataset_download("dylanjcastillo/7k-books-with-metadata")

import pandas as pd

# Load Dataset
books = pd.read_csv(f"{path}/books.csv")

# Explore structure
print("First 5 rows: \n", books.head())
print("Last 5 rows: \n", books.tail())
print(books.info())
print(books.describe())

# selected column

selected_columns = books[["title"]]

print("Selected Columns: \n", selected_columns)

# filtered rows

filtered_rows = books[(books["title"] > '15.0')]

print("Filteres Rows: \n", filtered_rows)
