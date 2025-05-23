# Merging Two dataset  and performing data transformation
import pandas as pd
import numpy as np

# Create a book dataset
import kagglehub

path1 = kagglehub.dataset_download("dylanjcastillo/7k-books-with-metadata")
path2 = kagglehub.dataset_download("dylanjcastillo/7k-books-with-metadata")

# Load Dataset
books1 = pd.read_csv(f"{path1}/books.csv")
books2 = pd.read_csv(f"{path2}/books.csv")

print("Dataset 1: \n", books1)
print("Dataset 2: \n", books2)

merged = pd.merge(books1, books2, how="inner") 
print("Merged Dataset: \n", merged)

merged["ratings"] = (merged["ratings_count"] / 200) * 100
print("Transformed Dataset \n", merged)