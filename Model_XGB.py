 #Masukkan Library
import pandas as pd

from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import MinMaxScaler
import xgboost as xgb
from sklearn.metrics import mean_squared_error, mean_absolute_error

import joblib

#Masukkan file data csv
data = pd.read_csv("DATA.csv")

#PENENTUAN VARIABEL
X = data.drop(['Agama', 'Bahasa_Inggris', 'Ketahanan_Pangan', 'Pancasila', 'Pendidikan_Kewarganegaraan',
              'Studi_Kebantenan', 'Tata_Tulis_dan_Komunikasi_Ilmiah',
              'Kuliah_Kerja_Mahasiswa', 'Seminar_Pendidikan_Agama', 'Pengantar_Ekonomika ',
              'Mekatronika_dan_Opimasi_Sistem_Produksi', 'Analisis_dan_Peancangan_Perusahaan',
              'Manajemen_Pemasaran', 'Tugas_Akhir_2', 'Status_Kelulusan'], axis=1)
y = data['Status_Kelulusan']

# Membuat objek scaler
scaler = MinMaxScaler()

# Melakukan normalisasi pada data latih (X)
X_normalized = scaler.fit_transform(X)

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import numpy as np

# Membuat objek KFold atau StratifiedKFold dengan 10 lipatan
kf = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)

# Inisialisasi list untuk menyimpan skor metrik evaluasi
precision_scores = []
recall_scores = []
f1_scores = []
accuracy_scores = []

# Loop melalui setiap fold
for fold, (train_index, test_index) in enumerate(kf.split(X_normalized, y), start=1):
    X_train = X_normalized[train_index]  # Data X untuk fold latih
    X_test = X_normalized[test_index]  # Data X untuk fold uji
    y_train = y[train_index]  # Data y untuk fold latih
    y_test = y[test_index]  # Data y untuk fold uji

    # Inisialisasi dan latih model (gantilah dengan model Anda)
    XGB_model = xgb.XGBClassifier(learning_rate=0.25,
    max_depth=20,
    n_estimators=200,
    objective='binary:logistic',  # Untuk klasifikasi biner
    random_state=42)
    XGB_model.fit(X_train, y_train)

    # Lakukan prediksi pada data uji
    y_pred_XGB = XGB_model.predict(X_test)

    # Hitung metrik evaluasi untuk fold ini
    precision = precision_score(y_test, y_pred_XGB)
    recall = recall_score(y_test, y_pred_XGB)
    f1 = f1_score(y_test, y_pred_XGB)
    accuracy = accuracy_score(y_test, y_pred_XGB)
    cm = confusion_matrix(y_test, y_pred_XGB)

    # Simpan skor metrik evaluasi ke dalam list
    precision_scores.append(precision)
    recall_scores.append(recall)
    f1_scores.append(f1)
    accuracy_scores.append(accuracy)

    # Cetak skor metrik evaluasi untuk fold ini
    print(f"Fold {fold} - Precision: {precision:.2f}, Recall: {recall:.2f}, F1-score: {f1:.2f}, Accuracy: {accuracy:.2f}")

    mse = mean_squared_error(y_test, y_pred_XGB)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred_XGB)

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
# Cetak rata-rata skor metrik evaluasi dari semua fold
print(f"Rata-rata Precision: {np.mean(precision_scores):.2f}")
print(f"Rata-rata Recall: {np.mean(recall_scores):.2f}")
print(f"Rata-rata F1-score: {np.mean(f1_scores):.2f}")
print(f"Rata-rata Accuracy: {np.mean(accuracy_scores):.2f}")
print("Confusion Matrix:")
print(cm)

joblib.dump(XGB_model, 'xgboost_model.pkl')
