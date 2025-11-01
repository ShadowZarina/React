import pandas as pd

df = pd.read_csv(r"C:\Users\Andrea\Downloads\Coding\Python\Data Python\bestsellers.csv")

# Get the first 5 rows of the spreadsheet
print(df.head())

# Get the shape of the spreadsheet
print(df.shape)

# Get the column names of the spreadsheet
print(df.columns)

# Get summary statistics for each column
print(df.describe())

# Remove all duplicate rows
df.drop_duplicates(inplace=True)

# Rename column names to "Title", "Publication Year", and "Rating"
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

# Convert "Price" column to use the float data type
df["Price"] = df["Price"].astype(float)


# List of authors with the most best selling books
author_counts = df['Author'].value_counts()
print(author_counts)
 
# List of genres and their average ratings
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)


# Export top selling authors to a CSV file
author_counts.head(10).to_csv("top_authors.csv")

# Export average rating by genre to a CSV file
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")