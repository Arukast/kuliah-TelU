"""### Soal 1: Pembersihan Data

1. **Deteksi dan Penanganan Nilai Hilang**
    - Identifikasi kolom-kolom yang memiliki nilai hilang dalam dataset. Bersihkan dataset dengan mengisi nilai hilang tersebut menggunakan metode yang sesuai.
    - Tampilkan persentase nilai hilang untuk setiap kolom sebelum dan setelah pembersihan.
2. **Deteksi dan Penanganan Outlier**
    - Gunakan metode IQR (Interquartile Range) untuk mendeteksi outlier pada kolom `Passenger Count`. Buat plot boxplot untuk visualisasi.
    - (pastikan anda sudah pip install scikit-learn statsmodels)"""
import pandas as pd
import numpy as np
# Plot boxplot untuk visualisasi outlier
import matplotlib.pyplot as plt
# Visualisasi distribusi data
import seaborn as sns
# PCA
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from statsmodels.tsa.seasonal import seasonal_decompose
# Soal 1
# import pandas as pd
# import numpy as np

# Membaca data
file_path = 'Semester2/SF_Air_Traffic_Passenger_Statistics.csv'
data = pd.read_csv(file_path)
try:
    # Deteksi nilai hilang
    missing_values = data.isnull().sum() / len(data) * 100
    print("Persentase nilai hilang sebelum pembersihan:")
    print(missing_values)

    # Mengisi nilai hilang dengan metode yang sesuai
    data_cleaned = data.fillna(method='ffill').fillna(method='bfill')

    # Tampilkan persentase nilai hilang setelah pembersihan
    missing_values_cleaned = data_cleaned.isnull().sum() / len(data_cleaned) * 100
    print("Persentase nilai hilang setelah pembersihan:")
    print(missing_values_cleaned)

    # Deteksi outlier menggunakan metode IQR
    Q1 = data_cleaned['Passenger Count'].quantile(0.25)
    Q3 = data_cleaned['Passenger Count'].quantile(0.75)
    IQR = Q3 - Q1
    outliers = data_cleaned[(data_cleaned['Passenger Count'] < (Q1 - 1.5 * IQR)) | (data_cleaned['Passenger Count'] > (Q3 + 1.5 * IQR))]

    # Plot boxplot untuk visualisasi outlier
    # import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    plt.boxplot(data_cleaned['Passenger Count'])
    plt.title('Boxplot of Passenger Count')
    plt.ylabel('Passenger Count')
    plt.show()
finally:
    print('Soal 1 Selesai')
"""### Soal 2: Analisis Statistik Deskriptif

1. **Statistik Deskriptif**
    - Hitung statistik deskriptif (mean, median, standard deviation) untuk kolom `Passenger Count` secara keseluruhan dan berdasarkan `Operating Airline`.
2. **Distribusi Data**
    - Buat histogram dan KDE plot untuk visualisasi distribusi `Passenger Count`."""
try:
    # Soal 2
    # Statistik deskriptif untuk seluruh data
    overall_stats = data_cleaned['Passenger Count'].describe()
    print("Statistik deskriptif untuk seluruh data:")
    print(overall_stats)

    # Statistik deskriptif berdasarkan Operating Airline
    airline_stats = data_cleaned.groupby('Operating Airline')['Passenger Count'].describe()
    print("Statistik deskriptif berdasarkan Operating Airline:")
    print(airline_stats)

    # Visualisasi distribusi data
    # import seaborn as sns

    plt.figure(figsize=(12, 6))
    sns.histplot(data_cleaned['Passenger Count'], bins=30, kde=True)
    plt.title('Histogram and KDE Plot of Passenger Count')
    plt.xlabel('Passenger Count')
    plt.ylabel('Frequency')
    plt.show()
finally:
    print('Soal 2 Selesai')
"""### Soal 3: Analisis Korelasi

1. **Heatmap Korelasi**
    - Hitung matriks korelasi untuk kolom numerik dalam dataset. Visualisasikan matriks korelasi menggunakan heatmap.
2. **Scatter Plot**
    - Buat scatter plot untuk menganalisis hubungan antara `Passenger Count` dan `Activity Period`. Tampilkan juga garis regresi."""
try:
    # Soal 3
    # Matriks korelasi
    data_cleaned2 = data_cleaned.select_dtypes(include=['int64', 'float64'])
    correlation_matrix = data_cleaned2.corr()
    print("Matriks korelasi:")
    print(correlation_matrix)

    # Visualisasi matriks korelasi menggunakan heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()

    # Scatter plot untuk hubungan antara Passenger Count dan Activity Period
    data_cleaned['Activity Period'] = pd.to_datetime(data_cleaned['Activity Period'], format='%Y%m')
    data_cleaned['Year'] = data_cleaned['Activity Period'].dt.year

    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Year', y='Passenger Count', data=data_cleaned)
    sns.regplot(x='Year', y='Passenger Count', data=data_cleaned, scatter=False, color='red')
    plt.title('Scatter Plot of Passenger Count vs Activity Period')
    plt.xlabel('Activity Period (Year)')
    plt.ylabel('Passenger Count')
    plt.show()
finally:
    print('Soal 3 Selesai')
"""### Soal 4: Analisis Multivariat

1. **Pairplot**
    - Buat pairplot untuk kolom-kolom numerik dalam dataset untuk melihat hubungan antara variabel-variabel tersebut.
2. **PCA (Principal Component Analysis)**
    - Lakukan PCA pada dataset dan visualisasikan hasilnya dalam 2D plot untuk memahami variabilitas data."""
try:
    # Soal 4
    # Pairplot untuk kolom-kolom numerik
    sns.pairplot(data_cleaned.select_dtypes(include=[np.number]))
    plt.title('Pairplot of Numeric Columns')
    plt.show()

    # PCA
    # from sklearn.decomposition import PCA
    # from sklearn.preprocessing import StandardScaler

    # Standarisasi data
    numeric_data = data_cleaned.select_dtypes(include=[np.number])
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numeric_data)

    # Lakukan PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(scaled_data)

    # Visualisasikan hasil PCA
    plt.figure(figsize=(10, 6))
    plt.scatter(pca_result[:, 0], pca_result[:, 1], c='blue', alpha=0.5)
    plt.title('PCA Result (2D)')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.show()
finally:
    print('Soal 4 Selesai')
"""### Soal 5: Analisis Waktu dan Musiman

1. **Decompose Time Series**
    - Lakukan dekomposisi data time series `Passenger Count` untuk melihat komponen tren, musiman, dan residu.
2. **Seasonal Plot**
    - Buat plot musiman untuk menganalisis pola musiman dalam data `Passenger Count`."""
try:
    # Soal 5
    # from statsmodels.tsa.seasonal import seasonal_decompose

    # Group by Activity Period dan hitung total penumpang per bulan
    monthly_data = data_cleaned.groupby('Activity Period')['Passenger Count'].sum()

    # Lakukan dekomposisi data time series
    decomposition = seasonal_decompose(monthly_data, model='additive')
    decomposition.plot()
    plt.show()

    # Plot musiman
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=monthly_data.index.month, y=monthly_data.values)
    plt.title('Seasonal Plot of Passenger Count')
    plt.xlabel('Month')
    plt.ylabel('Passenger Count')
    plt.show()
finally:
    print('Soal 5 Selesai')
"""### Soal 6: Sort dan Group By

1. **Sort Data**
    - Urutkan data berdasarkan `Passenger Count` dalam urutan menurun dan tampilkan 10 baris pertama.
2. **Group By**
    - Kelompokkan data berdasarkan `Operating Airline` dan hitung total `Passenger Count` untuk setiap maskapai. Tampilkan 10 maskapai dengan jumlah penumpang terbanyak."""
try:
    # Soal 6
    # Sort Data
    sorted_data = data_cleaned.sort_values(by='Passenger Count', ascending=False)
    top_10_passenger_counts = sorted_data.head(10)
    print("10 baris pertama setelah diurutkan berdasarkan Passenger Count:")
    print(top_10_passenger_counts)

    # Group By
    grouped_by_airline = data_cleaned.groupby('Operating Airline')['Passenger Count'].sum().sort_values(ascending=False)
    top_10_airlines = grouped_by_airline.head(10)
    print("10 maskapai dengan jumlah penumpang terbanyak:")
    print(top_10_airlines)
finally:
    print('Soal 6 Selesai')