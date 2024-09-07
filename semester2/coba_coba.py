import streamlit as st
import mysql.connector
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Fungsi untuk menghubungkan ke database
def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='restaurant',
        port=3306  
    )
    return connection

def add_pelanggan(Nama_Pelanggan, Nomor_Telepon, ID_Karyawan):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO pelanggan(Nama_Pelanggan, Nomor_Telepon, ID_Karyawan) VALUES (%s, %s, %s)', (Nama_Pelanggan, Nomor_Telepon, ID_Karyawan))
    connection.commit()
    cursor.close()
    connection.close()

def add_pesanan(Waktu_Pemesanan, ID_Pelanggan, ID_Meja, Makan_ditempat):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Pesanan (Waktu_Pemesanan, ID_Pelanggan, ID_Meja, Makan_ditempat) VALUES (%s, %s, %s, %s)', (Waktu_Pemesanan, ID_Pelanggan, ID_Meja, Makan_ditempat))
    connection.commit()
    cursor.close()
    connection.close()

def add_jumlah_menu_pesanan(ID_Pesanan, ID_Menu, Jumlah):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO jumlah_menu_pesanan (ID_Pesanan, ID_Menu, Jumlah) VALUES (%s, %s, %s)', (ID_Pesanan, ID_Menu, Jumlah))
    connection.commit()
    cursor.close()
    connection.close()

def add_reservasi(ID_Pelanggan, Waktu_Reservasi, ID_Meja):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO reservasi(ID_Pelanggan, Waktu_Reservasi, ID_Meja) VALUES (%s, %s, %s)', (ID_Pelanggan, Waktu_Reservasi, ID_Meja))
    connection.commit()
    cursor.close()
    connection.close()

def get_karyawan():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM karyawan')
    karyawan = cursor.fetchall()
    cursor.close()
    connection.close()
    return karyawan

def get_menu():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM menu')
    karyawan = cursor.fetchall()
    cursor.close()
    connection.close()
    return karyawan

def get_meja():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM meja')
    karyawan = cursor.fetchall()
    cursor.close()
    connection.close()
    return karyawan

def get_pelanggan():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM pelanggan')
    karyawan = cursor.fetchall()
    cursor.close()
    connection.close()
    return karyawan

def get_pesanan():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM pesanan')
    karyawan = cursor.fetchall()
    cursor.close()
    connection.close()
    return karyawan

st.title('Restaurant Arabia')

# Bagian untuk menambahkan pelanggan baru
with st.container():
    karyawan = get_karyawan()
    st.header('Add New Pelanggan')
    nama = st.text_input('Nama Pelanggan')
    nomor_telepon = st.text_input('Nomor Telepon')
    
    karyawan_options = {karyawan['ID_Karyawan']: karyawan['Nama_Karyawan'] for karyawan in karyawan}
    selected_karyawan_id = st.selectbox('Select Karyawan', list(karyawan_options.keys()), format_func=lambda x: karyawan_options[x])
    
    if st.button('Add Pelanggan'):
        if nama and nomor_telepon and selected_karyawan_id:
            add_pelanggan(nama, nomor_telepon, selected_karyawan_id)
            st.success(f'Pelanggan "{nama}" added successfully!')
        else:
            st.error('Mohon isi semua data yang diperlukan.')

# buat reservasi
with st.container():
    pelanggan = get_pelanggan()
    meja = get_meja()
    st.header('Add New Reservasi')
    
    pelanggan_options = {pelanggan['ID_Pelanggan']: pelanggan['Nama_Pelanggan'] for pelanggan in pelanggan}
    selected_pelanggan_id_reservasi = st.selectbox('Select pelanggan', list(pelanggan_options.keys()), format_func=lambda x: pelanggan_options[x], key="select_pelanggan_reservasi")

    input_tanggal = st.date_input('Tanggal', key="input_tanggal_reservasi")
    input_waktu = st.time_input('Waktu', key="input_waktu_reservasi")
    Waktu_Reservasi = datetime.combine(input_tanggal, input_waktu)
    
    meja_options = {meja['ID_Meja']:meja['Kapasitas'] for meja in meja}
    selected_meja_id_reservasi = st.selectbox('Pilih Kapasitas Meja', list(meja_options.keys()), format_func=lambda x: meja_options[x], key="select_meja_reservasi")

    if st.button('Add reservasi'):
        if selected_pelanggan_id_reservasi and Waktu_Reservasi and selected_meja_id_reservasi:
            add_reservasi(selected_pelanggan_id_reservasi, Waktu_Reservasi, selected_meja_id_reservasi)    
            st.success(f'Reservasi pelanggan "{nama}" added successfully!')
        else:
            st.error('Mohon isi semua data yang diperlukan.')

# Bagian untuk menambah Pesanan
with st.container():
    meja = get_meja()
    pelanggan = get_pelanggan()
    st.header('Pesanan')
    Waktu_Pemesanan = datetime.now()

    pelanggan_options = {pelanggan['ID_Pelanggan']: pelanggan['Nama_Pelanggan'] for pelanggan in pelanggan}
    selected_pelanggan_id = st.selectbox('Select pelanggan', list(pelanggan_options.keys()), format_func=lambda x: pelanggan_options[x])

    meja_options = {meja['ID_Meja']:meja['Kapasitas'] for meja in meja}
    selected_meja_id = st.selectbox('Pilih Kapasitas Meja', list(meja_options.keys()), format_func=lambda x: meja_options[x])
    
    Makan_ditempat = st.checkbox('Makan ditempat', value=True)

    if st.button('Add Pesanan'):
        if Waktu_Pemesanan and selected_pelanggan_id and selected_meja_id and Makan_ditempat:
            add_pesanan(Waktu_Pemesanan, selected_pelanggan_id, selected_meja_id, Makan_ditempat)
            st.success(f'Pesanan "{nama}" telah ditambahkan!')
        else:
            st.error('Mohon isi semua data yang diperlukan.')

#Bagian untuk jumlah menu pesanan
with st.container():
    st.header('Pesanan List')
    loans = get_pesanan()
    loans_df = pd.DataFrame(loans)
    st.dataframe(loans_df)

with st.container():
    menu = get_menu()
    pesanan = get_pesanan()
    st.header('Menu')

    pesanan_options = {pesanan['ID_Pesanan']: pesanan['ID_Pelanggan'] for pesanan in pesanan}
    selected_pesanan_id = st.selectbox('Select pelanggan', list(pesanan_options.keys()), format_func=lambda x: pesanan_options[x])

    menu_options = {menu['ID_Menu']: menu['Nama_Menu'] for menu in menu}
    selected_menu_id = st.selectbox('Select menu', list(menu_options.keys()), format_func=lambda x: menu_options[x])

    Jumlah = st.text_input('Jumlah')

    if st.button('Add jumlah pesanan'):
        if selected_pesanan_id and selected_menu_id and Jumlah:
            add_jumlah_menu_pesanan(selected_pesanan_id, selected_menu_id, Jumlah)
            st.success(f'added successfully!')
        else:
            st.error('Mohon isi semua data yang diperlukan.')