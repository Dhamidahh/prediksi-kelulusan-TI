import streamlit as st
import joblib
import pandas as pd
from PIL import Image
from streamlit_option_menu import option_menu
import numpy as np

data = pd.read_csv("DATA.csv")

X = data.drop(['Agama', 'Bahasa_Inggris', 'Ketahanan_Pangan', 'Pancasila', 'Pendidikan_Kewarganegaraan',
              'Studi_Kebantenan', 'Tata_Tulis_dan_Komunikasi_Ilmiah',
              'Kuliah_Kerja_Mahasiswa', 'Seminar_Pendidikan_Agama', 'Pengantar_Ekonomika ',
              'Mekatronika_dan_Opimasi_Sistem_Produksi', 'Analisis_dan_Peancangan_Perusahaan',
              'Manajemen_Pemasaran', 'Tugas_Akhir_2', 'Status_Kelulusan'], axis=1)
y = data['Status_Kelulusan']


# Muat model
model = joblib.load('random_forest_model.pkl')

# Judul aplikasi
st.title("Prediksi Kelulusan Mahasiswa")

# Judul aplikasi
st.title('Prediksi Kelulusan Mahasiswa TI UNTIRTA')

# Masukkin gambar
st.subheader('Keterangan Nilai Bobot Mata Kuliah')
img = Image.open('Nilai Bobot Mata Kuliah.jpg')
img = img.resize((300, 300))
st.image(img, use_column_width = True)

# Masukkan Nama
Nama_Lengkap = st.text_input("Nama Lengkap: ")

# Masukkan NIM
NIM = st.number_input("NIM:", min_value=0, max_value=3333999999, value=0)

# Set st.session_state setelah pengguna memasukkan Nama dan NIM
if Nama_Lengkap:
    st.session_state.name = Nama_Lengkap

if NIM:
    st.session_state.age = NIM

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7"]
)

def predict_lulus_tepat_waktu(input_nilai_mata_kuliah):
    prediction = model.predict([input_nilai_mata_kuliah])
    return prediction[0]

if selected == "Semester 1":
    st.header(f"Masukkan Nilai Pada Semester 1 ke Mata Kuliah")
    # Ambil kolom-kolom yang ada di Semester 1
    semester_1_columns = ["Fisika Dasar 1", "Kalkulus 1", "Kimia Dasar"]

    # Buat dictionary untuk menyimpan nilai mata kuliah
    nilai_mata_kuliah = {}

    # Loop melalui kolom-kolom Semester 1 dan tampilkan input nilai
    for mata_kuliah in semester_1_columns:
        nilai = st.number_input(f"Masukkan Nilai {mata_kuliah}", 0.0, max(data[mata_kuliah]), 0.0)
        nilai_mata_kuliah[mata_kuliah] = nilai  # Simpan nilai dalam dictionary

    if st.button('Prediksi'):
        # Konversi nilai-nilai mata kuliah ke dalam list
        input_nilai_mata_kuliah = [nilai_mata_kuliah.get(mk, np.nan) for mk in data.columns]

        # Lakukan prediksi dengan model XGBoost
        prediction = model.predict([input_nilai_mata_kuliah])

        st.write('Hasil Prediksi:')
        if prediction[0] == 1:
            st.write('Lulus Tepat Waktu')
        else:
            st.write('Lulus Tidak Tepat Waktu')

if selected == "Semester 2":
    st.header(f"Masukkan Nilai Pada Semester 1 ke Mata Kuliah")
    # Ambil kolom-kolom yang ada di Semester 1
    semester_2_columns = ["Fisika Dasar 1", "Kalkulus 1", "Kimia Dasar", "Analisis_Biaya", "Tugas_Akhir_1"]

    # Buat dictionary untuk menyimpan nilai mata kuliah
    nilai_mata_kuliah = {}

    # Loop melalui kolom-kolom Semester 1 dan tampilkan input nilai
    for mata_kuliah in semester_2_columns:
        nilai = st.number_input(f"Masukkan Nilai {mata_kuliah}", 0.0, max(data[mata_kuliah]), 0.0)
        nilai_mata_kuliah[mata_kuliah] = nilai  # Simpan nilai dalam dictionary

    if st.button('Prediksi'):
        # Konversi nilai-nilai mata kuliah ke dalam list
        input_nilai_mata_kuliah = [nilai_mata_kuliah.get(mk, np.nan) for mk in data.columns]

        # Lakukan prediksi dengan model XGBoost
        prediction = model.predict([input_nilai_mata_kuliah])

        st.write('Hasil Prediksi:')
        if prediction[0] == 1:
            st.write('Lulus Tepat Waktu')
        else:
            st.write('Lulus Tidak Tepat Waktu')