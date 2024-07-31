import pandas as pd

file_path = 'D:/0. Kantor/9. IKND/07. Pofiling BUMN/_Profil BUMD Per Provinsi/Dashboard/Database/004. Data Putusan BUMD.xlsx'

try:
    df = pd.read_excel(file_path, usecols=['Nama BUMD', 'Jenis Fraud', 'Tahun Persidangan', 'Status Kasus', 'No. SIPP', 'Tautan Putusan'])
    print(df.head())  # Menampilkan beberapa baris pertama dari DataFrame
except Exception as e:
    print(f"Error reading the Excel file: {e}")
