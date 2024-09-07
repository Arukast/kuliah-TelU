import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Baca File
file_path = ('Semester2/Melbourne_housing_FULL.csv')
data = pd.read_csv(file_path)
# Bagian 1 - Nomor 1 Membaca Data
print(data.head(5))
rows, columns = data.shape
print(f'Jumlah baris: {rows}')
print(f'Jumlah kolom: {columns}')
# Bagian 1 - Nomor 2 Deskripsi Data
print(f'Tipe data setiap kolom:\n{data.dtypes}')
print(f'Jumlah nilai yang hilang dari setiap kolom:\n{data.isnull().sum()}')
# Bagian 1 - Nomor 3 Statistika Deskriptif
dfSubSet1 = data[['Price', 'Landsize', 'BuildingArea']].describe().loc[['mean', '50%', 'std', 'min', 'max']]
dfSubSet1.rename(index={'50%': 'median'}, inplace=True)
print(dfSubSet1)

plt.figure(figsize=(12, 6))
sns.histplot(data['Price'].dropna(), bins=30, kde=True)
plt.title('Histogram of Price')
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(data['Landsize'].dropna(), kde=True)
plt.title('Histogram of Landsize')
plt.show()


