import pandas as pd
import seaborn as sns

# Data Preparation

df = pd.read_csv('data/movies.csv')
print(df.head())
df.info()
