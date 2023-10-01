#Masukkan Library
import pandas as pd
import joblib
import streamlit as st
from PIL import Image

# Load your CSV data
data = pd.read_csv("DATA.csv")

X = data.drop(['Agama', 'Bahasa_Inggris', 'Ketahanan_Pangan', 'Pancasila', 'Pendidikan_Kewarganegaraan',
              'Studi_Kebantenan', 'Tata_Tulis_dan_Komunikasi_Ilmiah', 'Kewirausahaan',
              'Kuliah_Kerja_Mahasiswa', 'Seminar_Pendidikan_Agama', 'Pengantar_Ekonomika ',
              'Mekatronika_dan_Opimasi_Sistem_Produksi', 'Analisis_dan_Peancangan_Perusahaan',
              'Manajemen_Pemasaran', 'Tugas_Akhir_2', 'Status_Kelulusan'], axis=1)
y = data['Status_Kelulusan']

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

# Load the pre-trained XGBoost model
model = joblib.load('xgboost_model.pkl')

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

# Create a dictionary to store course grades for each semester
semester_courses = {
    "Semester 1": ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
                   'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Pemrograman Komputer'],
    "Semester 2": ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
                   'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Pemrograman Komputer', 'Aljabar Linear',
                   'Fisika Dasar 2', 'Kalkulus 2', 'Mekanika Teknik', 'Praktikum Fisika Dasar', 'Proses Manufaktur',
                   'Sistem Lingkungan Industri', 'Praktikum Perancangan Teknik Industri 1'],
    "Semester 3": ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
                   'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Pemrograman Komputer', 'Aljabar Linear',
                   'Fisika Dasar 2', 'Kalkulus 2', 'Mekanika Teknik', 'Praktikum Fisika Dasar', 'Proses Manufaktur',
                   'Sistem Lingkungan Industri', 'Praktikum Perancangan Teknik Industri 1', 'Analisis Biaya', 'Penelitian Operasional 1',
                   'Perencanaan dan Pengendalian Produksi', 'Sistem rantai Pasok', 'Ergonomi Industri', 'Matematika Optimasi',
                   'Statistika Industri 1'],
    "Semester 4": ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
                   'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Pemrograman Komputer', 'Aljabar Linear',
                   'Fisika Dasar 2', 'Kalkulus 2', 'Mekanika Teknik', 'Praktikum Fisika Dasar', 'Proses Manufaktur',
                   'Sistem Lingkungan Industri', 'Praktikum Perancangan Teknik Industri 1', 'Analisis Biaya', 'Penelitian Operasional 1',
                   'Perencanaan dan Pengendalian Produksi', 'Sistem rantai Pasok', 'Ergonomi Industri', 'Matematika Optimasi',
                   'Statistika Industri 1', 'Analisis dan Perancangan Sistem Informasi', 'Pemodelan Sistem', 'Penelitian Operasional 2',
                   'Pengendalian dan Penjaminan Mutu', 'Praktikum Material', 'Ergonomi dan Perancangan Sistem Kerja 2', 'Praktikum Pemrograman Komputer',
                   'Statistika Industri 2'],
    "Semester 5": ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
                   'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Pemrograman Komputer', 'Aljabar Linear',
                   'Fisika Dasar 2', 'Kalkulus 2', 'Mekanika Teknik', 'Praktikum Fisika Dasar', 'Proses Manufaktur',
                   'Sistem Lingkungan Industri', 'Praktikum Perancangan Teknik Industri 1', 'Analisis Biaya', 'Penelitian Operasional 1',
                   'Perencanaan dan Pengendalian Produksi', 'Sistem rantai Pasok', 'Ergonomi Industri', 'Matematika Optimasi',
                   'Statistika Industri 1', 'Analisis dan Perancangan Sistem Informasi', 'Pemodelan Sistem',
                   'Penelitian Operasional 2', 'Pengendalian dan Penjaminan Mutu', 'Praktikum Material', 'Ergonomi dan Perancangan Sistem Kerja 2',
                   'Praktikum Pemrograman Komputer', 'Statistika Industri 2' 'Keselamatan dan Keamanan Kerja',
                   'Perancangan dan Pengembangan Produk', 'Perancangan Tata Letak Fasilitas', 'Simulasi Komputer',
                   'Sistem Produksi', 'Psikologi Industri', 'Praktikum Perancangan Teknik Industri 2', 'Praktikum Terintegarasi'],
    "Semester 6": ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
                   'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Pemrograman Komputer', 'Aljabar Linear',
                   'Fisika Dasar 2', 'Kalkulus 2', 'Mekanika Teknik', 'Praktikum Fisika Dasar', 'Proses Manufaktur',
                   'Sistem Lingkungan Industri', 'Praktikum Perancangan Teknik Industri 1', 'Analisis Biaya', 'Penelitian Operasional 1',
                   'Perencanaan dan Pengendalian Produksi', 'Sistem rantai Pasok', 'Ergonomi Industri', 'Matematika Optimasi',
                   'Statistika Industri 1', 'Analisis dan Perancangan Sistem Informasi', 'Pemodelan Sistem',
                   'Penelitian Operasional 2', 'Pengendalian dan Penjaminan Mutu', 'Praktikum Material', 'Ergonomi dan Perancangan Sistem Kerja 2',
                   'Praktikum Pemrograman Komputer', 'Statistika Industri 2' 'Keselamatan dan Keamanan Kerja',
                   'Perancangan dan Pengembangan Produk', 'Perancangan Tata Letak Fasilitas', 'Simulasi Komputer',
                   'Sistem Produksi', 'Psikologi Industri', 'Praktikum Perancangan Teknik Industri 2', 'Praktikum Terintegarasi',
                   'Kerja Praktek', 'Ekonomi Teknik', 'Organisasi dan Manajemen Perusahaan Industri'],
    "Semester 7": ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
                   'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Pemrograman Komputer', 'Aljabar Linear',
                   'Fisika Dasar 2', 'Kalkulus 2', 'Mekanika Teknik', 'Praktikum Fisika Dasar', 'Proses Manufaktur',
                   'Sistem Lingkungan Industri', 'Praktikum Perancangan Teknik Industri 1', 'Analisis Biaya', 'Penelitian Operasional 1',
                   'Perencanaan dan Pengendalian Produksi', 'Sistem rantai Pasok', 'Ergonomi Industri', 'Matematika Optimasi',
                   'Statistika Industri 1', 'Analisis dan Perancangan Sistem Informasi', 'Pemodelan Sistem',
                   'Penelitian Operasional 2', 'Pengendalian dan Penjaminan Mutu', 'Praktikum Material', 'Ergonomi dan Perancangan Sistem Kerja 2',
                   'Praktikum Pemrograman Komputer', 'Statistika Industri 2' 'Keselamatan dan Keamanan Kerja',
                   'Perancangan dan Pengembangan Produk', 'Perancangan Tata Letak Fasilitas', 'Simulasi Komputer',
                   'Sistem Produksi', 'Psikologi Industri', 'Praktikum Perancangan Teknik Industri 2', 'Praktikum Terintegarasi',
                   'Kerja Praktek', 'Ekonomi Teknik', 'Organisasi dan Manajemen Perusahaan Industri'
                   'Metodologi Penelitian', 'Tugas Akhir 1']
}

all_courses = ['Fisika Dasar 1', 'Kalkulus 1', 'Kimia Dasar', 'Material Teknik', 'Pengantar Teknik Industri',
               'Menggambar Teknik', 'Praktikum Menggambar Teknik', 'Pemrograman Komputer', 'Aljabar Linear',
               'Fisika Dasar 2', 'Kalkulus 2', 'Mekanika Teknik', 'Praktikum Fisika Dasar', 'Proses Manufaktur',
               'Sistem Lingkungan Industri', 'Praktikum Perancangan Teknik Industri 1', 'Analisis Biaya', 'Penelitian Operasional 1',
               'Perencanaan dan Pengendalian Produksi', 'Sistem rantai Pasok', 'Ergonomi Industri', 'Matematika Optimasi',
               'Statistika Industri 1', 'Analisis dan Perancangan Sistem Informasi', 'Pemodelan Sistem',
               'Penelitian Operasional 2', 'Pengendalian dan Penjaminan Mutu', 'Praktikum Material', 'Ergonomi dan Perancangan Sistem Kerja 2',
               'Praktikum Pemrograman Komputer', 'Statistika Industri 2', 'Keselamatan dan Keamanan Kerja',
               'Perancangan dan Pengembangan Produk', 'Perancangan Tata Letak Fasilitas', 'Simulasi Komputer',
               'Sistem Produksi', 'Psikologi Industri', 'Praktikum Perancangan Teknik Industri 2', 'Praktikum Terintegarasi',
               'Kerja Praktek', 'Ekonomi Teknik', 'Organisasi dan Manajemen Perusahaan Industri',
               'Metodologi Penelitian', 'Tugas Akhir 1']

data['Nilai_Rata_Rata'] = data[all_courses].mean(axis=1)

nilai_semester_df = pd.DataFrame(columns=all_courses)

# Define grade_options dictionary
grade_options = {
    'A': '4.00',
    'A-': '3.75',
    'B+': '3.50',
    'B': '3.00',
    'B-': '2.75',
    'C+': '2.50',
    'C': '2.00',
    'D': '1.00',
    'E': '0.00'
}


nilai_rata_rata = {}  # Buat dictionary untuk menyimpan nilai rata-rata

# Hitung rata-rata nilai mata kuliah
for mata_kuliah in all_courses:
    data[mata_kuliah] = pd.to_numeric(data[mata_kuliah], errors='coerce')  # Ubah kolom nilai menjadi numerik
    nilai_rata_rata[mata_kuliah] = data[mata_kuliah].mean()

# Set nilai-nilai untuk mata kuliah pada semester tertentu dan isi nilai-nilai yang kosong dengan rata-rata
for mata_kuliah in all_courses:
    nilai = st.selectbox(f'Nilai {mata_kuliah}:', options=list(grade_options.keys()),
                         format_func=lambda x: grade_options[x])

# Function to make predictions
def predict_lulus_tepat_waktu(input_nilai_semester):
    prediction = model.predict(input_nilai_semester)
    return prediction[0]


# Streamlit app title
st.title('Prediksi Kelulusan Mahasiswa')

# Select the semester
selected_semester = st.selectbox('Pilih Semester:', list(semester_courses.keys()))

# Buat DataFrame kosong dengan semua mata kuliah

# Input course grades for the selected semester
st.header(selected_semester)
nilai_semester = {}
courses = semester_courses[selected_semester]
for mata_kuliah in courses:
    nilai = st.selectbox(f'Nilai {mata_kuliah}:', options=list(grade_options.keys()))
    nilai_semester[mata_kuliah] = nilai

    # Jika pengguna tidak memilih nilai, isi dengan nilai rata-rata
    if not nilai:
        nilai_semester[mata_kuliah] = nilai_rata_rata[mata_kuliah]

    nilai_semester_df.loc[0, mata_kuliah] = nilai_semester[mata_kuliah]
# Button to make predictions
if st.button(f'Prediksi Kelulusan {selected_semester}'):
    input_nilai_semester = nilai_semester_df.iloc[0].tolist()  # Ambil nilai-nilai semester dari DataFrame

    # Periksa jika ada nilai yang kosong (None)
    if None in input_nilai_semester:
        st.warning("Harap isi semua nilai mata kuliah!")

            # Ganti nilai-nilai kosong dengan rata-rata dari mata kuliah tersebut
        for i in range(len(input_nilai_semester)):
            if input_nilai_semester[i] is None:
                mata_kuliah = all_courses[i]
                input_nilai_semester[i] = nilai_rata_rata[mata_kuliah]

    prediction = predict_lulus_tepat_waktu(input_nilai_semester)

    st.write("Hasil Prediksi Kelulusan:")
    if prediction == 1:
        st.write('Lulus Tepat Waktu')
    else:
        st.write('Tidak Lulus Tepat Waktu')