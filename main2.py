#Masukkan Library
import pandas as pd
import joblib
import streamlit as st
from PIL import Image

data = pd.read_csv("DATA.csv")

X = data.drop(['Agama', 'Ketahanan_Pangan', 'Pancasila', 'Pendidikan_Kewarganegaraan',
              'Studi_Kebantenan', 'Tata_Tulis_dan_Komunikasi_Ilmiah', 'Kuliah_Kerja_Mahasiswa',
              'Seminar_Pendidikan_Agama', 'Status_Kelulusan'], axis=1)
y = data['Status_Kelulusan']
# Muat model
model = joblib.load('random_forest_model.pkl')

# Muat data training
X_train = joblib.load('X_train.pkl')
y_train = joblib.load('y_train.pkl')

# Judul aplikasi
st.title('Prediksi Kelulusan Tepat Waktu')

# Judul header dan masukkin nama
st.header("Aplikasi Prediksi Kelulusan Mahasiswa TI UNTIRTA")

# Masukkan Nama
Nama_Lengkap = st.text_input("Nama_Lengkap: ")

# Masukkan NIM
NIM = st.number_input("NIM:", min_value=0, max_value=3333999999, value=0)

# Set st.session_state setelah pengguna memasukkan Nama dan NIM
if Nama_Lengkap:
    st.session_state.name = Nama_Lengkap

if NIM:
    st.session_state.age = NIM

# Masukkin gambar
st.subheader('Keterangan Nilai Bobot Mata Kuliah')
img = Image.open('Nilai Bobot Mata Kuliah.jpg')
img = img.resize((300, 300))
st.image(img, use_column_width=False)


# Fungsi untuk melakukan prediksi
def predict_lulus_tepat_waktu(data_prediksi):
    prediction = model.predict([data_prediksi])
    return prediction[0]

# Daftar nama mata kuliah
mata_kuliah = [
    "Bahasa_Inggris",
    "Fisika Dasar"
]

# Inisialisasi dictionary nilai
nilai = {}

# Inisialisasi nilai hasil_prediksi
hasil_prediksi = None

# Buat select box untuk setiap mata kuliah
for Bahasa_Inggris in mata_kuliah:
    nilai[Bahasa_Inggris] = st.selectbox(f"Pilih Nilai{mata_kuliah} :", [1, 2, 3, 4])

for Fisika_Dasar in mata_kuliah:
        nilai[Fisika_Dasar] = st.selectbox(f"Pilih Nilai{mata_kuliah} :", [1, 2, 3, 4])

    # Prediksi nilai kelulusan
    if st.button("Prediksi Kelulusan"):
        # Buat DataFrame berdasarkan nilai yang dipilih
        data_prediksi = pd.DataFrame.from_dict(nilai, orient='index', columns=['Nilai'])

        # Lakukan prediksi menggunakan model
        hasil_prediksi = predict_lulus_tepat_waktu(data_prediksi)

    if 'name' in st.session_state:
        st.write(f"Halo {st.session_state.name}!")

    if 'age' in st.session_state:
        st.write(f"NIM {st.session_state.age}.")

    # Tampilkan hasil prediksi
    st.write("Hasil Prediksi Kelulusan:")
    if hasil_prediksi is not None:
        if hasil_prediksi == 1:
            st.write("Mahasiswa diperkirakan lulus tepat waktu.")
        else:
            st.write("Mahasiswa diperkirakan tidak lulus tepat waktu.")