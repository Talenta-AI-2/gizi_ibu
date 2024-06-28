import sqlite3
import pandas as pd

# Langkah 1 > Load data file
df = pd.read_csv('Dataset_TKPI.csv')

# Langkah 2. > Data Cleaning
df.columns = df.columns.str.strip()

# Langkah 3 > Buat Database dengan SQLite
connection = sqlite3.connect('gizi_indo.db')

# Langkah 4. > Upload data ke SQLite
# fail;replace;append

df.to_sql('indonesian_food_composition', connection, if_exists='replace')

# Langkah 5. > Close koneksi
connection.close()