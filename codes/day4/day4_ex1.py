# Cleaning a books dataset by handling missing values and renaming columns

import pandas as pd
import numpy as np

# Create a sample dataset
import kagglehub

path = kagglehub.dataset_download("dylanjcastillo/7k-books-with-metadata")

# Load Dataset
books = pd.read_csv(f"{path}/books.csv")

print("Original Dataset: \n", books)
# fill empty rating_count with mean of ratings_count
books["ratings_count"] = books["ratings_count"].fillna(books["ratings_count"].mean())
# fill empty rating_count with interpolation of ratings_count
books["ratings_count"] = books["ratings_count"].interpolate()
# rename columns
books = books.rename(columns={"isbn13":"book_numner", "ratings_count": "ratings"})

# drop rows with missing values 
books = books.dropna()

print("Dataset: \n", books)