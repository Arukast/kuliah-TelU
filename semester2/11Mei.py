import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px

# data = pd.read_excel('C:\\Users\\tubag\\OneDrive\\Dokumen\\Alta\\KULIAH\\Pemrograman\\Semester2\\datacontoh11mei.xlsx')
data = pd.read_excel('datacontoh11mei.xlsx')
print(data.head())
print(data.describe())
data.groupby('Jenis Kelamin').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.show()

data.groupby('Jurusan Sekolah SMA').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)
plt.show()

plt.subplots(figsize=(8, 8))
df_2dhist = pd.DataFrame({
    x_label: grp['Jurusan Kuliah'].value_counts()
    for x_label, grp in data.groupby('Jurusan Sekolah SMA')
})
sns.heatmap(df_2dhist, cmap='viridis')
plt.xlabel('Jurusan Sekolah SMA')
_ = plt.ylabel('Jurusan Kuliah')
plt.show()

# Histogram untuk umur
a = plt.figure(figsize=(10, 6))
sns.histplot(data['Umur'], kde=True)
# kde-kernel density
plt.title('Distribusi Umur')
plt.xlabel('Umur')
plt.ylabel('Frekuensi')
a.show()
# jika kedip doang tambahkan
input('Tekan entetr untuk melanjutkan....')

# Scatter plot Gaji vs Pengalaman Kerja
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Pengalaman Kerja (tahun)', y='Gaji', data=data)
plt.title('Hubungan Gaji dan Pengalaman Kerja')
plt.xlabel('Pengalaman Kerja (tahun)')
plt.ylabel('Gaji')
plt.show()