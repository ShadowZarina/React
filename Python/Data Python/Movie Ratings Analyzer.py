# Movie Ratings Analyzer

# import Pandas & Matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# load data with Pandas
df = pd.read_csv('movies.csv')  
print(df.head())

# remove movies with missing data
df = df.dropna(subset=['rating', 'year', 'genre'])
# treat years as integers
df['year'] = df['year'].astype(int)

# calculate average ratings by year
yearly_avg = df.groupby('year')['rating'].mean()

# count the number of genres and select top 10
genre_counts = df['genre'].value_counts().head(10)

# generate a line graph using Matplotlib
plt.figure(figsize=(10, 6)) 
plt.plot(yearly_avg.index, yearly_avg.values)
plt.title("Average Movie Rating per Year")
plt.xlabel("Year")
plt.ylabel("Rating")
plt.show()