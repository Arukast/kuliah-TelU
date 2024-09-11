import pandas as pd

# Membaca data dari file CSV
df = pd.read_csv('Top 50 Football Player.csv')

# Menambahkan kolom rata-rata
df['Average'] = (df['Speed'] + df['Stamina'] + df['Attack'] + df['Defense'])/4
# Mengurutkan data berdasarkan rata-rata tertinggi
df = df.sort_values('Average', ascending=False)

# Memfilter data berdasarkan umur antara 23 dan 28 tahun
df = df[(df['Age']>=23)&(df['Age']<=28)]
# Mengambil 11 data teratas
df = df.head(11)
# Menghitung total harga
totalHarga = df['Price ($)'].sum()

# Mencari nilai tertinggi dari setiap kolom ability beserta nama pemain
speedTertinggi = df.loc[df['Speed'].idxmax(), 'Name']
staminaTertinggi = df.loc[df['Stamina'].idxmax(), 'Name']
attackTertinggi = df.loc[df['Attack'].idxmax(), 'Name']
defenseTertinggi = df.loc[df['Defense'].idxmax(), 'Name']

# Menampilkan data
print(f'{df}\n')
print(f'Total Harga: ${totalHarga}\n')
print(f'Speed Tertinggi: {speedTertinggi} ({df["Speed"].max()})')
print(f'Stamina Tertinggi: {staminaTertinggi} ({df["Stamina"].max()})')
print(f'Attack Tertinggi: {attackTertinggi} ({df["Attack"].max()})')
print(f'Defense Tertinggi: {defenseTertinggi} ({df["Defense"].max()})')


