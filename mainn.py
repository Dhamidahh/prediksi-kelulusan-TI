#Masukkan Library
import pandas as pd
import joblib
import streamlit as st
from PIL import Image

data = pd.read_csv("DATA.csv")

X = data.drop(['Agama', 'Bahasa_Inggris', 'Ketahanan_Pangan', 'Pancasila', 'Pendidikan_Kewarganegaraan',
              'Studi_Kebantenan', 'Tata_Tulis_dan_Komunikasi_Ilmiah',
              'Kuliah_Kerja_Mahasiswa', 'Seminar_Pendidikan_Agama', 'Pengantar_Ekonomika ',
              'Mekatronika_dan_Opimasi_Sistem_Produksi', 'Analisis_dan_Peancangan_Perusahaan',
              'Manajemen_Pemasaran', 'Tugas_Akhir_2', 'Status_Kelulusan'], axis=1)
y = data['Status_Kelulusan']

# Muat model
model = joblib.load('random_forest_model.pkl')

# Muat data training
X_train = joblib.load('X_train.pkl')
y_train = joblib.load('y_train.pkl')

# Judul aplikasi
st.title('Prediksi Kelulusan Mahasiswa TI UNTIRTA')

# Masukkin gambar
img = Image.open('Logo Univ.jpg')
img = img.resize((300,300))
st.image(img, use_column_width = False)

# Masukkan Nama
Nama_Lengkap = st.text_input("Nama Lengkap: ")

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
img = img.resize((300,300))
st.image(img, use_column_width = False)


# Fungsi untuk melakukan prediksi
def predict_lulus_tepat_waktu(input_nilai_mata_kuliah):
    prediction = model.predict([input_nilai_mata_kuliah])
    return prediction[0]


# Input nilai mata kuliah
Bahasa_Inggris = st.number_input("Masukkan Nilai Bahasa Inggris", 0.0, max(data["Bahasa_Inggris"]), 4.0, 0.0)
Fisika_Dasar_1 = st.number_input("Masukkan Nilai Fisika Dasar 1", 0.0, max(data["Fisika_Dasar_1"]), 4.0, 0.0)
Kalkulus_1 = st.number_input("Masukkan Nilai Kalkulus 1", 0.0, max(data["Kalkulus_1"]), 4.0, 0.0)
Kimia_Dasar = st.number_input("Masukkan Nilai Kimia Dasar", 0.0, max(data["Kimia_Dasar"]), 4.0, 0.0)
Pengantar_Teknik_Industri = st.number_input("Masukkan Nilai Pengantar Teknik Industri 1", 0.0,
                                            max(data["Pengantar_ Teknik_Industri"]), 4.0, 0.0)
Sistem_Lingkungan_Industri = st.number_input("Masukkan Nilai Sistem Lingkungan Industri", 0.0,
                                             max(data["Sistem_Lingkungan_Industri"]), 4.0, 0.0)
Fisika_Dasar_2 = st.number_input("Masukkan Nilai Fisika Dasar 2", 0.0, max(data["Fisika_Dasar_2"]), 4.0, 0.0)
Kalkulus_2 = st.number_input("Masukkan Nilai Kalkulus 2", 0.0, max(data["Kalkulus_2"]), 4.0, 0.0)
Menggambar_Teknik = st.number_input("Masukkan Nilai Menggambar Teknik", 0.0, max(data["Menggambar_Teknik"]), 4.0, 0.0)
Pengantar_Ekonomika = st.number_input("Masukkan Nilai Pengantar Ekonomika", 0.0, max(data["Pengantar_Ekonomika "]), 4.0, 0.0)
Praktikum_Fisika_Dasar = st.number_input("Masukkan Nilai Praktikum Fisika Dasar", 0.0,
                                         max(data["Praktikum_Fisika_Dasar"]), 4.0, 0.0)
Praktikum_Menggambar_Teknik = st.number_input("Masukkan Nilai Praktikum Menggambar Teknik", 0.0,
                                              max(data["Praktikum_Menggambar_Teknik"]), 4.0, 0.0)
Aljabar_Linear = st.number_input("Masukkan Nilai Aljabar Linear", 0.0, max(data["Aljabar_Linear"]), 4.0)
Ergonomi_dan_Perancangan_Sistem_Kerja_1 = st.number_input("Masukkan Nilai Ergonomi dan Perancangan Sistem Kerja 1", 0.0,
                                                          max(data["Ergonomi_dan_Perancangan_Sistem_Kerja_1"]), 4.0, 0.0)
Mekanika_Teknik = st.number_input("Masukkan Nilai Mekanika Teknik", 0.0, max(data["Mekanik_Teknik"]), 4.0, 0.0)
Material_Teknik = st.number_input("Masukkan Nilai Material Teknik", 0.0, max(data["Material_Teknik"]), 4.0, 0.0)
Pemrograman_Komputer = st.number_input("Masukkan Nilai Pemrograman Komputer", 0.0, max(data["Pemrograman_Komputer"]),
                                       4.0, 0.0)
Penelitian_Operasional_1 = st.number_input("Masukkan Nilai Penelitian Operasional 1", 0.0,
                                           max(data["Penelitian_Operasional"]), 4.0, 0.0)
Praktikum_Material = st.number_input("Masukkan Nilai Praktikum Material", 0.0, max(data["Praktikum_Material"]), 4.0, 0.0)
Praktikum_Pemrograman_Komputer = st.number_input("Masukkan Nilai Praktikum Pemrograman Komputer", 0.0,
                                                 max(data["Praktikum_Pemrograman_Komputer"]), 4.0, 0.0)
Proses_Manufaktur = st.number_input("Masukkan Nilai Proses Manufaktur", 0.0, max(data["Proses_Manufaktur"]), 4.0, 0.0)
Statistika_Industri = st.number_input("Masukkan Nilai Statistika Industri 1", 0.0, max(data["Statistika_Industri"]), 4.0)
Analisis_Biaya = st.number_input("Masukkan Nilai Analisis Biaya", 0.0, max(data["Analisis_Biaya"]), 4.0, 0.0)
Ergonomi_dan_Perancangan_Sistem_Kerja_2 = st.number_input("Masukkan Nilai Ergonomi dan Perancangan Sistem Kerja 2", 0.0,
                                                          max(data["Ergonomi_dan_Perancangan_Sistem_Kerja_2"]), 4.0, 0.0)
Matematika_Optimasi = st.number_input("Masukkan Nilai Matematika Optimasi", 0.0, max(data["Matematika_Optimasi"]),
                                      4.0, 0.0)
Perancangan_dan_Pengembangan_Produk = st.number_input("Masukkan Nilai Perancangan dan Pengembangan Produk", 0.0,
                                                      max(data["Perancangan_dan_Pengembangan _Produk "]), 4.0)
Penelitian_Operasional_2 = st.number_input("Masukkan Nilai Penelitian Operasional 2", 0.0,
                                           max(data["Penelitian_Operasional_2"]), 4.0, 0.0, key="penelitian_operasional_2")
Praktikum_Perancangan_Teknik_Industri_1 = st.number_input("Masukkan Nilai Praktikum Perancangan Teknik Industri 1", 0.0,
                                                          max(data["Praktikum_Perancangan_Teknik_Industri_1"]), 4.0, 0.0)
Psikologi_Industri = st.number_input("Masukkan Nilai Psikologi Industri", 0.0, max(data["Psikologi_Industri"]), 4.0, 0.0)
Statistika_Industri_2 = st.number_input("Masukkan Nilai Statistika Industri 2", 0.0, max(data["Statistika_Industri_2"]),
                                        4.0, 0.0)
Ekonomi_Teknik = st.number_input("Masukkan Nilai Ekonomi Teknik", 0.0, max(data["Ekonomi_Teknik"]), 4.0, 0.0)
Mekatronika_dan_Opimasi_Sistem_Produksi = st.number_input("Masukkan Nilai Mekatronika dan Optimasi Sistem Produksi",
                                                          0.0, max(data["Mekatronika_dan_Opimasi_Sistem_Produksi"]),
                                                          4.0, 0.0)
Pemodelan_Sistem = st.number_input("Masukkan Nilai Pemodelan Sistem", 0.0, max(data["Pemodelan_Sistem"]), 4.0, 0.0)
Pengendalian_dan_Penjaminan_Mutu = st.number_input("Masukkan Nilai Pengendalian dan Penjaminan Mutu", 0.0,
                                                   max(data["Pengendalian_dan_Penjaminan_Mutu"]), 4.0, 0.0)
Perancangan_Tata_Letak_Fasilitas = st.number_input("Masukkan Nilai Perancangan Tata Letak Fasilitas", 0.0,
                                                   max(data["Perancangan_Tata_Letak_Fasilitas"]), 4.0, 0.0)
Perencanaan_dan_Pengendalian_Produksi = st.number_input("Masukkan Nilai Perancangan dan Pengendalian Produksi", 0.0,
                                                        max(data["Perencanaan_dan_Pengendalian_Produksi"]), 4.0, 0.0)
Praktikum_Perancangan_Teknik_Industri_2 = st.number_input("Masukkan Nilai Praktikum Perancangan Teknik Industri 2", 0.0,
                                                          max(data["Praktikum_Perancangan_Teknik_Industri_2"]), 4.0, 0.0)
Analisis_dan_Peancangan_Perusahaan = st.number_input("Masukkan Nilai Analisis dan Perancangan Perusahaan", 0.0,
                                                     max(data["Analisis_dan_Peancangan_Perusahaan"]), 4.0, 0.0)
Analisis_dan_Perancangan_Sistem_Informasi = st.number_input("Masukkan Nilai Analisis dan Perancangan Sistem Informasi",
                                                            0.0, max(data["Analisis_dan_Perancangan_Sistem_Informasi"]),
                                                            4.0, 0.0)
Kerja_Praktek = st.number_input("Masukkan Nilai Kerja Praktek", 0.0, max(data["Kerja_Praktek"]), 4.0, 0.0)
Kesehatan_dan_Keselamatan_Kerja = st.number_input("Masukkan Nilai Kesehatan dan Keselamatan Kerja", 0.0,
                                                  max(data["Kesehatan_dan_Keselamatan_Kerja"]), 4.0, 0.0)
Organisasi_dan_Manajemen_Perusahaan_Industri = st.number_input(
    "Masukkan Nilai Organisasi dan Manajemen Perusahaan Industri", 0.0,
    max(data["Organisasi_dan_Manajemen_Perusahaan_Industri"]), 4.0, 0.0)
Praktikum_Perancangan_Teknik_Industri_3 = st.number_input("Masukkan Nilai Praktikum dan Perancangan Teknik Industri 3",
                                                          0.0, max(data["Praktikum_Perancangan_Teknik_Industri_2"]),
                                                          4.0, 0.0)
Simulasi_Komputer = st.number_input("Masukkan Nilai Simulasi Komputer", 0.0, max(data["Simulasi_Komputer"]), 4.0, 0.0)
Sistem_Produksi = st.number_input("Masukkan Nilai Sistem Produksi", 0.0, max(data["Sistem_Produksi"]), 4.0, 0.0)
Kewirausahaan = st.number_input("Masukkan Nilai Kewirausahaan", 0.0, max(data["Kewirausahaan"]), 4.0, 0.0)
Manajemen_Pemasaran = st.number_input("Masukkan Nilai Manajemen Pemasaran", 0.0, max(data["Manajemen_Pemasaran"]), 4.0, 0.0)
Metodologi_Penelitian = st.number_input("Masukkan Nilai Metodologi Peneltian", 0.0, max(data["Metodologi_Penelitian"]),
                                        4.0, 0.0)
Sistem_Rantai_Pasok = st.number_input("Masukkan Nilai Sistem Rantai Pasok", 0.0, max(data["Sistem_Rantai_Pasok"]), 4.0, 0.0)
Tugas_Akhir_1 = st.number_input("Masukkan Nilai Tugas Akhir 1", 0.0, max(data["Tugas_Akhir_1"]), 4.0, 0.0)
Tugas_Akhir_2 = st.number_input("Masukkan Nilai Tugas Akhir 2", 0.0, max(data["Tugas_Akhir_2"]), 4.0, 0.0)

if st.button('Prediksi'):
    input_nilai_mata_kuliah = [Bahasa_Inggris, Fisika_Dasar_1, Kalkulus_1, Kimia_Dasar,
                               Pengantar_Teknik_Industri, Sistem_Lingkungan_Industri, Fisika_Dasar_2,
                               Kalkulus_2, Menggambar_Teknik, Pengantar_Ekonomika,
                               Praktikum_Fisika_Dasar, Praktikum_Menggambar_Teknik, Aljabar_Linear,
                               Ergonomi_dan_Perancangan_Sistem_Kerja_1, Material_Teknik, Mekanika_Teknik,
                               Pemrograman_Komputer, Penelitian_Operasional_1, Praktikum_Material,
                               Praktikum_Pemrograman_Komputer, Proses_Manufaktur, Statistika_Industri,
                               Analisis_Biaya, Ergonomi_dan_Perancangan_Sistem_Kerja_2, Matematika_Optimasi,
                               Penelitian_Operasional_2, Perancangan_dan_Pengembangan_Produk,
                               Praktikum_Perancangan_Teknik_Industri_1, Psikologi_Industri, Statistika_Industri_2,
                               Ekonomi_Teknik, Mekatronika_dan_Opimasi_Sistem_Produksi, Pemodelan_Sistem,
                               Pengendalian_dan_Penjaminan_Mutu, Perancangan_Tata_Letak_Fasilitas,
                               Perencanaan_dan_Pengendalian_Produksi, Praktikum_Perancangan_Teknik_Industri_2,
                               Analisis_dan_Peancangan_Perusahaan, Analisis_dan_Perancangan_Sistem_Informasi,
                               Kerja_Praktek, Kesehatan_dan_Keselamatan_Kerja,
                               Organisasi_dan_Manajemen_Perusahaan_Industri, Praktikum_Perancangan_Teknik_Industri_3,
                               Simulasi_Komputer, Sistem_Produksi, Kewirausahaan, Manajemen_Pemasaran,
                               Metodologi_Penelitian, Sistem_Rantai_Pasok, Tugas_Akhir_1,
                               Tugas_Akhir_2]  # Tambahkan nilai mata kuliah lain
    prediction = predict_lulus_tepat_waktu(input_nilai_mata_kuliah)

    if 'name' in st.session_state:
        st.write(f"Halo {st.session_state.name}!")

    if 'age' in st.session_state:
        st.write(f"NIM {st.session_state.age}.")

    if prediction == 1:
        st.write('Hasil Prediksi: Lulus Tepat Waktu')
    else:
        st.write('Hasil Prediksi: Lulus Tidak Tepat Waktu')



# Pilihan semester
semester = st.selectbox("Pilih Semester:", ["1", "2", "3", "4", "5", "6", "7", "8"])




# Daftar mata kuliah untuk setiap semester (contoh)
mata_kuliah_semester = {
    "1":    {"Fisika Dasar 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kimia Dasar": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Material Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pengantar Teknik Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Menggambar Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Menggambar Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Logika Pemrograman": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0]
    },
    "2":    {"Fisika Dasar 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kimia Dasar": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Material Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pengantar Teknik Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Menggambar Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Menggambar Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Logika Pemrograman": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Aljabar Linear": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Fisika Dasar 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Mekanika Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Fisika Dasar": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Proses Manufaktur": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ekologi Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Proses Manufaktur": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0]
    },
    "3":    {"Fisika Dasar 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kimia Dasar": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Material Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pengantar Teknik Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Menggambar Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Menggambar Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Logika Pemrograman": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Aljabar Linear": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Fisika Dasar 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Mekanika Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Fisika Dasar": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Proses Manufaktur": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ekologi Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Proses Manufaktur": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Analisis Biaya": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Penelitian Operasional 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perencanaan dan Pengendalian Produksi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Sistem rantai Pasok": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ergonomi Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 3": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Statistika 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0]
    },
    "4":    {"Fisika Dasar 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kimia Dasar": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Material Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pengantar Teknik Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Menggambar Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Menggambar Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Logika Pemrograman": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Aljabar Linear": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Fisika Dasar 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Mekanika Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Fisika Dasar": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Proses Manufaktur": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ekologi Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Proses Manufaktur": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Analisis Biaya": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Penelitian Operasional 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perencanaan dan Pengendalian Produksi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Sistem rantai Pasok": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ergonomi Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 3": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Statistika 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Analisis dan Perancangan Sistem Informasi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pemodelan Sistem": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Penelitian Operasional 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pengendalian dan Penjaminan Mutu": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Analitika Data": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ergonomi 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Analisis dan Perancangan Sistem Informasi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Statistika 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0]
    },
    "5":    {"Fisika Dasar 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kimia Dasar": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Material Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pengantar Teknik Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Menggambar Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Menggambar Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Logika Pemrograman": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Aljabar Linear": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Fisika Dasar 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Mekanika Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Fisika Dasar": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Proses Manufaktur": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ekologi Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Proses Manufaktur": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Analisis Biaya": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Penelitian Operasional 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perencanaan dan Pengendalian Produksi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Sistem rantai Pasok": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ergonomi Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 3": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Statistika 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Analisis dan Perancangan Sistem Informasi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pemodelan Sistem": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Penelitian Operasional 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pengendalian dan Penjaminan Mutu": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Analitika Data": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ergonomi 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Analisis dan Perancangan Sistem Informasi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Statistika 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Keselamatan dan Keamanan Kerja": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perancangan dan Pengembangan Produk": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perancangan Tata Letak Fasilitas": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Simulasi Sistem": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Sistem Produksi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perilaku Organisasi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Tata Letak Fasilitas": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Terintegarasi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0]
    },
    "6":    {"Fisika Dasar 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kimia Dasar": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Material Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pengantar Teknik Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Menggambar Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Menggambar Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Logika Pemrograman": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Aljabar Linear": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Fisika Dasar 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Mekanika Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Fisika Dasar": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Proses Manufaktur": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ekologi Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Proses Manufaktur": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Analisis Biaya": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Penelitian Operasional 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perencanaan dan Pengendalian Produksi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Sistem rantai Pasok": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ergonomi Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 3": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Statistika 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Analisis dan Perancangan Sistem Informasi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pemodelan Sistem": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Penelitian Operasional 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pengendalian dan Penjaminan Mutu": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Analitika Data": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ergonomi 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Analisis dan Perancangan Sistem Informasi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Statistika 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Keselamatan dan Keamanan Kerja": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perancangan dan Pengembangan Produk": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perancangan Tata Letak Fasilitas": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Simulasi Sistem": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Sistem Produksi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perilaku Organisasi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Tata Letak Fasilitas": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Terintegarasi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kerja Praktek": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ekonomika dan Ekonomi Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perancangan dan Manajemen Organisasi Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0]
    },
    "7":    {"Fisika Dasar 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kimia Dasar": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Material Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pengantar Teknik Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Menggambar Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Menggambar Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Logika Pemrograman": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Aljabar Linear": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Fisika Dasar 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Mekanika Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Fisika Dasar": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Proses Manufaktur": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ekologi Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Proses Manufaktur": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Analisis Biaya": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Penelitian Operasional 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perencanaan dan Pengendalian Produksi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Sistem rantai Pasok": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ergonomi Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kalkulus 3": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Statistika 1": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Analisis dan Perancangan Sistem Informasi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pemodelan Sistem": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Penelitian Operasional 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Pengendalian dan Penjaminan Mutu": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Analitika Data": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ergonomi 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Analisis dan Perancangan Sistem Informasi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Statistika 2": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Keselamatan dan Keamanan Kerja": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perancangan dan Pengembangan Produk": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perancangan Tata Letak Fasilitas": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Simulasi Sistem": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Sistem Produksi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perilaku Organisasi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Tata Letak Fasilitas": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Praktikum Terintegarasi": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Kerja Praktek": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Ekonomika dan Ekonomi Teknik": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perancangan dan Manajemen Organisasi Industri": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Metodologi Penelitian": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0],
             "Perancangan Sistem Terpadu": [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0]
    }
}

with st.form():
    Semester = st.selectbox("Pilih Semester:", mata_kuliah_semester)

    # Pilihan mata kuliah berdasarkan semester
    selected_mata_kuliah = st.selectbox("Pilih Mata Kuliah:", list(mata_kuliah_semester[semester].key()))

    # Pilihan nilai mata kuliah (select box)
    nilai_options = [4.0, 3.75, 3.50, 3.00, 2.75, 2.50, 2.00, 1.00, 0]  # Nilai-nilai yang dapat dipilih
    selected_nilai = st.selectbox(f"Pilih Nilai {selected_mata_kuliah}:", nilai_options)

    # Format input sesuai dengan format yang digunakan dalam pelatihan model
    input_data = {
        "semester": [semester],
        "nilai": [selected_nilai]
    }

with st.form("my_form"):
    semester = st.selectbox("Pilih Semester:", ["1", "2", "3"])

# Submit form

    if st.form_submit_button("Submit"):
        st.write(f"Semester yang Dipilih: {semester}")

    # Lakukan prediksi dengan model XGBoost
        prediction = model.predict(input_data)

        if semester == "1":
            if prediction[0] == 1:
                result = "Selamat! Anda bisa lulus tepat waktu. Semangat belajar!"
            else:
                result = "Maaf, kamu tidak bisa lulus tepat waktu. Harapkan tingkatkan belajarmu lagi."
        elif semester == "2":
            if prediction[0] == 1:
                result = "Selamat! Anda bisa lulus tepat waktu tanpa harus mengulang mata kuliah."
            else:
                result = "Maaf, kamu tidak bisa lulus tepat waktu. Harapkan tingkatkan belajarmu lagi."
        elif semester == "3":
            if prediction[0] == 1:
                result = "Selamat! Anda bisa lulus tepat waktu dalam semester ini."
            else:
                result = "Maaf, kamu tidak bisa lulus tepat waktu. Harapkan tingkatkan belajarmu lagi."
        else:
            result = "Anda perlu memperhatikan nilai Anda untuk memastikan kelulusan tepat waktu."

    # Tampilkan hasil prediksi
        st.write(f"Hasil Prediksi: {result}")


mata_kuliah_mapping = {
    "Pemrograman Komputer": "Logika Pemrograman",
    "Sistem Lingkungan Industri": "Ekologi Industri",
    "Praktikum Perancangan Teknik Indsutri 1": "Praktikum Proses Mnuafaktu",
    "Ergonomi dan Perancangan Sistem Kerja 1": "Ergonomi 1",
    "Matematika Optimasi": "Kalkulus 3",
    "Statistika Industri 1": "Statistika 1",
    "Praktikum Material": "Analitika Data",
    "Ergonomi dan Perancangan Sistem Informasi": "Praktikum Analisis dan Peranacangan SIstem Informasi",
    "Statistika Industri 2": "Statistika 2",
    "Simulasi Komputer": "Simulasi Sistem",
    "Psikologi Industri": "Perilaku Organisasi",
    "Praktikum Perancangan Teknik Industri 2": "Praktikum Tata Letak Fasilitas",
    "Praktikum Perancangan Teknik Industri 3": "Praktikum Terintegrasi",
    "Ekonomi Teknik": "Ekonomika dan Ekonomi Teknik",
    "Organisasi dan Manajemen Perusahaan Industri": "Perancangan dan Manajemen Organisasi Industri",
    "Tugas Akhir 1": "Perancangan Sistem Terpadu"
}

data['Pemrograman_Komputer'] = data['Pemrograman_Komputer'].replace('Pemrograman Komputer', 'Logika Pemrograman')
data['Sistem_Lingkungan_Industri'] = data['Sistem_Lingkungan_Industri'].replace('Sistem Lingkungan Industri', 'Ekologi Industri')
data['Praktikum_Perancangan_Teknik_Indsutri_1'] = data['Praktikum_Perancangan_Teknik_Indsutri_1'].replace('Praktikum Perancangan Teknik Indsutri 1', 'Praktikum Proses Mnuafaktur')
data['Matematika_Optimasi'] = data['Matematika_Optimasi'].replace('Matematika Optimasi', 'Kalkulus 3')
data['Statistika_Industri']= data['Statistika_Industri'].replace('Statistika Industri": "Statistika 1')
data['Praktikum_Material'] = data['Praktikum_Material'].replace('Praktikum Material', 'Analitika Data')
data['Ergonomi_dan_Perancangan_Sistem_Kerja_2'] = data['Ergonomi_dan_Perancangan_Sistem_Kerja_2'].replace('Ergonomi dan Perancangan Sistem Kerja 2', 'Ergonomi 2')
data['Praktikum_Pemrogaman Komputer'] = data['Praktikum_Pemrogaman Komputer'].replace('Praktikum Pemrogaman Komputer', 'Praktikum Analisis dan Peranacangan Sistem Informasi')
data['Statistika_Industri_2'] = data['Statistika_Industri_2'].replace('Statistika Industri 2', 'Statistika 2')
data['Simulasi_Komputer'] = data['Simulasi_Komputer'].replace('Simulasi Komputer', 'Simulasi Sistem')
data['Psikologi_Industri'] = data['Psikologi_Industri'].replace('Psikologi Industri', 'Perilaku Organisasi')
data['Praktikum_Perancangan_Teknik_Industri_2'] = data['Praktikum_Perancangan_Teknik_Industri_2'].replace('Praktikum Perancangan Teknik Industri 2', 'Praktikum Tata Letak Fasilitas')
data['Praktikum_Perancangan_Teknik_Industri_3'] = data['Praktikum_Perancangan_Teknik_Industri_3].replace('Praktikum Perancangan Teknik Industri 3', 'Praktikum Terintegrasi')
data['Ekonomi_Teknik'] = data['Ekonomi_Teknik'].replace('Ekonomi Teknik', 'Ekonomika dan Ekonomi Teknik')
data['Organisasi_dan_Manajemen_Perusahaan_Industri'] = data['Organisasi_dan_Manajemen_Perusahaan_Industri'].replace('Organisasi dan Manajemen Perusahaan Industri', 'Perancangan dan Manajemen Organisasi Industri')
data['Tugas_Akhir_1'] = data['Tugas_Akhir_1'].replace('Tugas Akhir 1', 'Perancangan Sistem Terpadu')

for mata_kuliah in all_courses:
    # Hitung rata-rata nilai mata kuliah
    if mata_kuliah == 'Fisika_Dasar_1':
        nilai_rata_rata[mata_kuliah] = data['Fisika_Dasar_1'].mean()
    if mata_kuliah == 'Kalkulus_1':
        nilai_rata_rata[mata_kuliah] = data['Kalkulus_1'].mean()
    if mata_kuliah == 'Material_Teknik':
            nilai_rata_rata[mata_kuliah] = data['Material_Teknik'].mean()
    if mata_kuliah == 'Pengantar_Teknik_Industri':
            nilai_rata_rata[mata_kuliah] = data['Pengantar_Teknik_Industri'].mean()
    if mata_kuliah == 'Kimia_Dasar':
            nilai_rata_rata[mata_kuliah] = data['Kimia_Dasar'].mean()
    if mata_kuliah == 'Menggambar_Teknik':
            nilai_rata_rata[mata_kuliah] = data['Menggambar_Teknik'].mean()
    if mata_kuliah == 'Praktikum_Menggambar_Teknik':
            nilai_rata_rata[mata_kuliah] = data['Praktikum_Menggambar_Teknik'].mean()
    if mata_kuliah == 'Logika_Pemrograman':
            nilai_rata_rata[mata_kuliah] = data['Logika_Pemrograman'].mean()
    if mata_kuliah == 'Aljabar_Linear':
            nilai_rata_rata[mata_kuliah] = data['Aljabar_Linear'].mean()
    if mata_kuliah == 'Fisika_Dasar_2':
            nilai_rata_rata[mata_kuliah] = data['Fisika_Dasar_2'].mean()
    if mata_kuliah == 'Kalkulus_2':
            nilai_rata_rata[mata_kuliah] = data['Kalkulus_2'].mean()
    if mata_kuliah == 'Mekanika_Teknik':
            nilai_rata_rata[mata_kuliah] = data['Mekanika_Teknik'].mean()
    if mata_kuliah == 'Praktikum_Fisika_Dasar':
            nilai_rata_rata[mata_kuliah] = data['Praktikum_Fisika_Dasar'].mean()
    if mata_kuliah == 'Proses_Manufaktur':
            nilai_rata_rata[mata_kuliah] = data['Proses_Manufaktur'].mean()
    if mata_kuliah == 'Ekologi_Industri':
            nilai_rata_rata[mata_kuliah] = data['Ekologi_Industri'].mean()
    if mata_kuliah == 'Praktikum_Proses_Manufaktur':
            nilai_rata_rata[mata_kuliah] = data['Praktikum_Proses_Manufaktur'].mean()
    if mata_kuliah == 'Analisis_Biaya':
            nilai_rata_rata[mata_kuliah] = data['Analisis_Biaya'].mean()
    if mata_kuliah == 'Penelitian_Operasional_1':
            nilai_rata_rata[mata_kuliah] = data['Penelitian_Operasional_1'].mean()
    if mata_kuliah == 'Perencanaan_dan_Pengendalian_Produksi':
            nilai_rata_rata[mata_kuliah] = data['Perencanaan_dan_Pengendalian_Produksi'].mean()
    if mata_kuliah == 'Sistem_rantai_Pasok':
            nilai_rata_rata[mata_kuliah] = data['Sistem_rantai_Pasok'].mean()
    if mata_kuliah == 'Ergonomi_Industri':
            nilai_rata_rata[mata_kuliah] = data['Ergonomi_Industri'].mean()
    if mata_kuliah == 'Kalkulus_3':
            nilai_rata_rata[mata_kuliah] = data['Kalkulus_3'].mean()
    if mata_kuliah == 'Statistika_1':
            nilai_rata_rata[mata_kuliah] = data['Statistika_1'].mean()
    if mata_kuliah == 'Analisis_dan_Perancangan_Sistem_Informasi':
            nilai_rata_rata[mata_kuliah] = data['Analisis_dan_Perancangan_Sistem_Informasi'].mean()
    if mata_kuliah == 'Pemodelan_Sistem':
            nilai_rata_rata[mata_kuliah] = data['Pemodelan_Sistem'].mean()
    if mata_kuliah == 'Penelitian_Operasional_2':
            nilai_rata_rata[mata_kuliah] = data['Penelitian_Operasional_2'].mean()
    if mata_kuliah == 'Pengendalian_dan_Penjaminan_Mutu':
            nilai_rata_rata[mata_kuliah] = data['Pengendalian_dan_Penjaminan_Mutu'].mean()
    if mata_kuliah == 'Analitika_Data':
            nilai_rata_rata[mata_kuliah] = data['Analitika_Data'].mean()
    if mata_kuliah == 'Ergonomi_2':
            nilai_rata_rata[mata_kuliah] = data['Ergonomi_2'].mean()
    if mata_kuliah == 'Praktikum_Analisis_dan_Perancangan_Sistem_Informasi':
            nilai_rata_rata[mata_kuliah] = data['Praktikum_Analisis_dan_Perancangan_Sistem_Informasi'].mean()
    if mata_kuliah == 'Keselamatan_dan_Keamanan_Kerja':
            nilai_rata_rata[mata_kuliah] = data['Keselamatan_dan_Keamanan_Kerja'].mean()
    if mata_kuliah == 'Perancangan_dan_Pengembangan_Produk':
            nilai_rata_rata[mata_kuliah] = data['Perancangan_dan_Pengembangan_Produk'].mean()
    if mata_kuliah == 'Perancangan_Tata_Letak_Fasilitas':
            nilai_rata_rata[mata_kuliah] = data['Perancangan_Tata_Letak_Fasilitas'].mean()
    if mata_kuliah == 'Simulasi_Sistem':
            nilai_rata_rata[mata_kuliah] = data['Simulasi_Sistem'].mean()
    if mata_kuliah == 'Sistem_Produksi':
            nilai_rata_rata[mata_kuliah] = data['Sistem_Produksi'].mean()
    if mata_kuliah == 'Perilaku_Organisasi':
            nilai_rata_rata[mata_kuliah] = data['Perilaku_Organisasi'].mean()
    if mata_kuliah == 'Praktikum_Tata_Letak_Fasilitas':
            nilai_rata_rata[mata_kuliah] = data['Praktikum_Tata_Letak_Fasilitas'].mean()
    if mata_kuliah == 'Praktikum_Terintegarasi':
            nilai_rata_rata[mata_kuliah] = data['Praktikum_Terintegarasi'].mean()
    if mata_kuliah == 'Kerja_Praktek':
            nilai_rata_rata[mata_kuliah] = data['Kerja_Praktek'].mean()
    if mata_kuliah == 'Ekonomika_dan_Ekonomi_Teknik':
            nilai_rata_rata[mata_kuliah] = data['Ekonomika_dan_Ekonomi_Teknik'].mean()
    if mata_kuliah == 'Perancangan_dan_Manajemen_Organisasi_Industri':
            nilai_rata_rata[mata_kuliah] = data['Perancangan_dan_Manajemen_Organisasi_Industri'].mean()
    if mata_kuliah == 'Metodologi_Penelitian':
            nilai_rata_rata[mata_kuliah] = data['Metodologi_Penelitian'].mean()
    if mata_kuliah == 'Perancangan_Sistem_Terpadu':
            nilai_rata_rata[mata_kuliah] = data['Perancangan_Sistem_Terpadu'].mean()

# List semua mata kuliah
all_courses =     ['Fisika_Dasar_1', 'Kalkulus_1', 'Kimia_Dasar', 'Material_Teknik', 'Pengantar_Teknik_Industri',
                   'Menggambar_Teknik', 'Praktikum_Menggambar_Teknik', 'Pemrograman_Komputer', 'Aljabar_Linear',
                   'Fisika_Dasar_2', 'Kalkulus_2', 'Mekanika_Teknik', 'Praktikum_Fisika_Dasar', 'Proses_Manufaktur',
                   'Ekologi_Industri', 'Praktikum_Proses_Manufaktur', 'Analisis_Biaya', 'Penelitian_Operasional_1',
                   'Perencanaan_dan_Pengendalian_Produksi', 'Sistem_rantai_Pasok', 'Ergonomi_Industri', 'Kalkulus_3',
                   'Statistika_1', 'Analisis_dan_Perancangan_Sistem_Informasi', 'Pemodelan_Sistem',
                   'Penelitian_Operasional_2', 'Pengendalian_dan_Penjaminan_Mutu', 'Analitika_Data', 'Ergonomi_2',
                   'Praktikum_Analisis_dan_Perancangan_Sistem_Informasi', 'Statistika_2', 'Keselamatan_dan_Keamanan_Kerja',
                   'Perancangan_dan_Pengembangan_Produk', 'Perancangan_Tata_Letak_Fasilitas', 'Simulasi_Sistem',
                   'Sistem_Produksi', 'Perilaku_Organisasi', 'Praktikum_Tata_Letak_Fasilitas', 'Praktikum_Terintegarasi',
                   'Kerja_Praktek', 'Ekonomika_dan_Ekonomi_Teknik', 'Perancangan_dan_Manajemen_Organisasi_Industri'
                   'Metodologi_Penelitian', 'Perancangan_Sistem_Terpadu']


# Create a dictionary to store course grades for each semester
semester_courses = {
    "Semester 1": ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
                   'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Logika Pemrograman'],
    "Semester 2": ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
                   'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Logika Pemrograman', 'Aljabar Linear',
                   'Fisika Dasar 2', 'Kalkulus 2', 'Mekanika Teknik', 'Praktikum Fisika Dasar', 'Proses Manufaktur',
                   'Ekologi Industri', 'Praktikum Proses Manufaktur'],
    "Semester 3": ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
                   'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Logika Pemrograman', 'Aljabar Linear',
                   'Fisika Dasar 2', 'Kalkulus 2', 'Mekanika Teknik', 'Praktikum Fisika Dasar', 'Proses Manufaktur',
                   'Ekologi Industri', 'Praktikum Proses Manufaktur', 'Analisis Biaya', 'Penelitian Operasional 1',
                   'Perencanaan dan Pengendalian Produksi', 'Sistem rantai Pasok', 'Ergonomi Industri', 'Kalkulus 3',
                   'Statistika 1'],
    "Semester 4": ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
                   'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Logika Pemrograman', 'Aljabar Linear',
                   'Fisika Dasar 2', 'Kalkulus 2', 'Mekanika Teknik', 'Praktikum Fisika Dasar', 'Proses Manufaktur',
                   'Ekologi Industri', 'Praktikum Proses Manufaktur', 'Analisis Biaya', 'Penelitian Operasional 1',
                   'Perencanaan dan Pengendalian Produksi', 'Sistem rantai Pasok', 'Ergonomi Industri', 'Kalkulus 3',
                   'Statistika 1', 'Analisis dan Perancangan Sistem Informasi', 'Pemodelan Sistem', 'Penelitian Operasional 2',
                   'Pengendalian dan Penjaminan Mutu', 'Analitika Data', 'Ergonomi 2', 'Praktikum Analisis dan Perancangan Sistem Informasi',
                   'Statistika 2'],
    "Semester 5": ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
                   'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Logika Pemrograman', 'Aljabar Linear',
                   'Fisika Dasar 2', 'Kalkulus 2', 'Mekanika Teknik', 'Praktikum Fisika Dasar', 'Proses Manufaktur',
                   'Ekologi Industri', 'Praktikum Proses Manufaktur', 'Analisis Biaya', 'Penelitian Operasional 1',
                   'Perencanaan dan Pengendalian Produksi', 'Sistem rantai Pasok', 'Ergonomi Industri', 'Kalkulus 3',
                   'Statistika 1', 'Analisis dan Perancangan Sistem Informasi', 'Pemodelan Sistem',
                   'Penelitian Operasional 2', 'Pengendalian dan Penjaminan Mutu', 'Analitika Data', 'Ergonomi 2',
                   'Praktikum Analisis dan Perancangan Sistem Informasi', 'Statistika 2', 'Keselamatan dan Keamanan Kerja',
                   'Perancangan dan Pengembangan Produk', 'Perancangan Tata Letak Fasilitas', 'Simulasi Sistem',
                   'Sistem Produksi', 'Perilaku Organisasi', 'Praktikum Tata Letak Fasilitas', 'Praktikum Terintegarasi'],
    "Semester 6": ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
                   'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Logika Pemrograman', 'Aljabar Linear',
                   'Fisika Dasar 2', 'Kalkulus 2', 'Mekanika Teknik', 'Praktikum Fisika Dasar', 'Proses Manufaktur',
                   'Ekologi Industri', 'Praktikum Proses Manufaktur', 'Analisis Biaya', 'Penelitian Operasional 1',
                   'Perencanaan dan Pengendalian Produksi', 'Sistem rantai Pasok', 'Ergonomi Industri', 'Kalkulus 3',
                   'Statistika 1', 'Analisis dan Perancangan Sistem Informasi', 'Pemodelan Sistem',
                   'Penelitian Operasional 2', 'Pengendalian dan Penjaminan Mutu', 'Analitika Data', 'Ergonomi 2',
                   'Praktikum Analisis dan Perancangan Sistem Informasi', 'Statistika 2' 'Keselamatan dan Keamanan Kerja',
                   'Perancangan dan Pengembangan Produk', 'Perancangan Tata Letak Fasilitas', 'Simulasi Sistem',
                   'Sistem Produksi', 'Perilaku Organisasi', 'Praktikum Tata Letak Fasilitas', 'Praktikum Terintegarasi',
                   'Kerja Praktek', 'Ekonomika dan Ekonomi Teknik', 'Perancangan dan Manajemen Organisasi Industri'],
    "Semester 7": ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
                   'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Logika Pemrograman', 'Aljabar Linear',
                   'Fisika Dasar 2', 'Kalkulus 2', 'Mekanika Teknik', 'Praktikum Fisika Dasar', 'Proses Manufaktur',
                   'Ekologi Industri', 'Praktikum Proses Manufaktur', 'Analisis Biaya', 'Penelitian Operasional 1',
                   'Perencanaan dan Pengendalian Produksi', 'Sistem rantai Pasok', 'Ergonomi Industri', 'Kalkulus 3',
                   'Statistika 1', 'Analisis dan Perancangan Sistem Informasi', 'Pemodelan Sistem',
                   'Penelitian Operasional 2', 'Pengendalian dan Penjaminan Mutu', 'Analitika Data', 'Ergonomi 2',
                   'Praktikum Analisis dan Perancangan Sistem Informasi', 'Statistika 2' 'Keselamatan dan Keamanan Kerja',
                   'Perancangan dan Pengembangan Produk', 'Perancangan Tata Letak Fasilitas', 'Simulasi Sistem',
                   'Sistem Produksi', 'Perilaku Organisasi', 'Praktikum Tata Letak Fasilitas', 'Praktikum Terintegarasi',
                   'Kerja Praktek', 'Ekonomika dan Ekonomi Teknik', 'Perancangan dan Manajemen Organisasi Industri'
                   'Metodologi Penelitian', 'Perancangan Sistem Terpadu']
}

data['Pemrograman_Komputer'] = data['Pemrograman_Komputer'].replace('Pemrograman Komputer', 'Logika Pemrograman')
data['Sistem_Lingkungan_Industri'] = data['Sistem_Lingkungan_Industri'].replace('Sistem Lingkungan Industri', 'Ekologi Industri')
data['Praktikum_Perancangan_Teknik_Industri_1'] = data['Praktikum_Perancangan_Teknik_Industri_1'].replace('Praktikum Perancangan Teknik Indsutri 1', 'Praktikum Proses Mnuafaktur')
data['Matematika_Optimasi'] = data['Matematika_Optimasi'].replace('Matematika Optimasi', 'Kalkulus 3')
data['Statistika_Industri'] = data['Statistika_Industri'].replace({'Statistika Industri': 'Statistika 1'})
data['Praktikum_Material'] = data['Praktikum_Material'].replace('Praktikum Material', 'Analitika Data')
data['Ergonomi_dan_Perancangan_Sistem_Kerja_2'] = data['Ergonomi_dan_Perancangan_Sistem_Kerja_2'].replace('Ergonomi dan Perancangan Sistem Kerja 2', 'Ergonomi 2')
data['Praktikum_Pemrograman_Komputer'] = data['Praktikum_Pemrograman_Komputer'].replace('Praktikum Pemrogaman Komputer', 'Praktikum Analisis dan Peranacangan Sistem Informasi')
data['Statistika_Industri_2'] = data['Statistika_Industri_2'].replace('Statistika Industri 2', 'Statistika 2')
data['Simulasi_Komputer'] = data['Simulasi_Komputer'].replace('Simulasi Komputer', 'Simulasi Sistem')
data['Psikologi_Industri'] = data['Psikologi_Industri'].replace('Psikologi Industri', 'Perilaku Organisasi')
data['Praktikum_Perancangan_Teknik_Industri_2'] = data['Praktikum_Perancangan_Teknik_Industri_2'].replace('Praktikum Perancangan Teknik Industri 2', 'Praktikum Tata Letak Fasilitas')
data['Praktikum_Perancangan_Teknik_Industri_2'] = data['Praktikum_Perancangan_Teknik_Industri_2'].replace('Praktikum Perancangan Teknik Industri 3', 'Praktikum Terintegrasi')
data['Ekonomi_Teknik'] = data['Ekonomi_Teknik'].replace('Ekonomi Teknik', 'Ekonomika dan Ekonomi Teknik')
data['Organisasi_dan_Manajemen_Perusahaan_Industri'] = data['Organisasi_dan_Manajemen_Perusahaan_Industri'].replace('Organisasi dan Manajemen Perusahaan Industri', 'Perancangan dan Manajemen Organisasi Industri')
data['Tugas_Akhir_1'] = data['Tugas_Akhir_1'].replace('Tugas Akhir 1', 'Perancangan Sistem Terpadu')


data[X] = data[X].replace({
    'Pemrograman Komputer': 'Logika Pemrograman',
    'Sistem Lingkungan Industri': 'Ekologi Industri',
    'Praktikum Perancangan Teknik Indsutri 1': 'Praktikum Proses Mnuafaktur',
    'Matematika Optimasi': 'Kalkulus 3',
    'Statistika Industri': 'Statistika 1',
    'Praktikum Material': 'Analitika Data',
    'Ergonomi dan Perancangan Sistem Kerja 2': 'Ergonomi 2',
    'Praktikum Pemrogaman Komputer': 'Praktikum Analisis dan Peranacangan Sistem Informasi',
    'Statistika Industri 2': 'Statistika 2',
    'Simulasi Komputer': 'Simulasi Sistem',
    'Psikologi Industri': 'Perilaku Organisasi',
    'Praktikum Perancangan Teknik Industri 2': 'Praktikum Tata Letak Fasilitas',
    'Praktikum Perancangan Teknik Industri 3': 'Praktikum Terintegrasi',
    'Ekonomi Teknik': 'Ekonomika dan Ekonomi Teknik',
    'Organisasi dan Manajemen Perusahaan Industri': 'Perancangan dan Manajemen Organisasi Industri',
    'Tugas Akhir 1': 'Perancangan Sistem Terpadu'
})


SEMESTER_2 = pickle.load(
    open('MODEL_SEMESTER2_MLP.sav.sav', 'rb'))
SEMESTER_3 = pickle.load(
    open('MODEL_SEMESTER3_KNN.sav', 'rb'))
SEMESTER_4 = pickle.load(
    open('MODEL_SEMESTER4_RF.sav', 'rb'))
SEMESTER_5 = pickle.load(
    open('MODEL_SEMESTER5_RF.sav', 'rb'))
SEMESTER_6 = pickle.load(
    open('MODEL_SEMESTER6_XGB.sav', 'rb'))
SEMESTER_7 = pickle.load(
    open('MODEL_SEMESTER7_RF.sav', 'rb'))
