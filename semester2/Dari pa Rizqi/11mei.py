import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
#jika xlsx pip install openpyxl
data = pd.read_excel('datacontoh11mei.xlsx')
#jika path tidak ada, bisa diisi dengan path lengkap
#data = pd.read_excel('Lokasi.xlsx lengkap/datacontoh11mei.xlsx')
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


# Histogram untuk Umur
a=plt.figure(figsize=(10, 6))
sns.histplot(data['Umur'], kde=True)
#kde=kernel density
plt.title('Distribusi Umur')
plt.xlabel('Umur')
plt.ylabel('Frekuensi')
a.show()


b = plt.figure(figsize=(10, 6))
sns.scatterplot(x='Pengalaman Kerja (tahun)', y='Gaji', data=data)
plt.title('Hubungan Gaji dan Pengalaman Kerja')
plt.xlabel('Pengalaman Kerja (tahun)')
plt.ylabel('Gaji')
b.show()


# Boxplot Gaji berdasarkan Jurusan Kuliah
c = plt.figure(figsize=(12, 8))
sns.boxplot(x='Jurusan Kuliah', y='Gaji', data=data)
plt.title('Distribusi Gaji berdasarkan Jurusan Kuliah')
plt.xlabel('Jurusan Kuliah')
plt.ylabel('Gaji')
plt.xticks(rotation=45)
c.show()


# Bar plot Gaji berdasarkan Jenis Kelamin
d = plt.figure(figsize=(10, 6))
sns.barplot(x='Jenis Kelamin', y='Gaji', data=data)
plt.title('Rata-Rata Gaji Berdasarkan Jenis Kelamin')
plt.xlabel('Jenis Kelamin')
plt.ylabel('Rata-Rata Gaji')
d.show()



# Membuat subset dari data yang hanya berisi kolom numerik
data_numerik = data.select_dtypes(include=['int64', 'float64'])

# Menghitung korelasi antar kolom numerik
korelasi = data_numerik.corr()

# Visualisasi heatmap korelasi
e = plt.figure(figsize=(12, 10))
sns.heatmap(korelasi, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Heatmap Korelasi Antar Fitur Numerik')
e.show()

#input tekan keyboard untuk lanjut
input("Tekan Enter untuk melanjutkan...")

#untuk yang di vscode pip install plotly

# Membuat fungsi untuk memetakan kategori ke ID unik
def map_categories(column):
    unique = column.unique()
    return {name: i for i, name in enumerate(unique)}

# Memetakan kategori ke ID
school_map = map_categories(data['Asal Sekolah'])
major_map = map_categories(data['Jurusan Sekolah SMA'])
job_map = map_categories(data['Pekerjaan'])

# Membuat sumber, target, dan nilai untuk Sankey diagram
source = []
target = []
value = []

for idx, row in data.iterrows():
    source.append(school_map[row['Asal Sekolah']])
    target.append(len(school_map) + major_map[row['Jurusan Sekolah SMA']])
    value.append(1)

    source.append(len(school_map) + major_map[row['Jurusan Sekolah SMA']])
    target.append(len(school_map) + len(major_map) + job_map[row['Pekerjaan']])
    value.append(1)

# Membuat label
labels = list(school_map.keys()) + list(major_map.keys()) + list(job_map.keys())

# Membuat Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels
    ),
    link=dict(
        source=source,  # indices correspond to labels
        target=target,
        value=value
    ))])

fig.update_layout(title_text="Sankey Diagram: Aliran Asal Sekolah, Jurusan, dan Pekerjaan", font_size=10)
fig.show()



# Histogram untuk distribusi umur menggunakan Plotly
fig = px.histogram(data, x='Umur', nbins=10, title='Distribusi Umur')
fig.update_layout(bargap=0.1)
fig.show()

# Boxplot untuk gaji menggunakan Plotly
fig = px.box(data, y='Gaji', title='Distribusi Gaji')
fig.show()

# Rata-rata gaji berdasarkan jurusan kuliah
avg_salary_by_major = data.groupby('Jurusan Kuliah')['Gaji'].mean().reset_index()

# Bar plot menggunakan Plotly
fig = px.bar(avg_salary_by_major, x='Jurusan Kuliah', y='Gaji',
             title='Rata-Rata Gaji Berdasarkan Jurusan Kuliah')
fig.show()

# Membuat subset dari data yang hanya berisi kolom numerik
import plotly.express as px

data_numerik = data.select_dtypes(include=['int64', 'float64'])

# Korelasi antar fitur numerik
korelasi = data_numerik.corr()

# Heatmap korelasi menggunakan Plotly
fig = px.imshow(korelasi, text_auto=True, aspect="auto",
                labels=dict(x="Fitur", y="Fitur", color="Korelasi"),
                title="Heatmap Korelasi Antar Fitur Numerik")
fig.show()
