from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/profiling_bumd')
def profiling_bumd():
    return render_template('profiling_bumd.html')

@app.route('/api/data')
def get_data():
    file_path = 'D:/0. Kantor/9. IKND/07. Pofiling BUMN/_Profil BUMD Per Provinsi/Dashboard/Database/004. Data Putusan BUMD.xlsx'
    df = pd.read_excel(file_path, usecols=['Nama BUMD', 'Jenis Fraud', 'Tahun Persidangan', 'Status Kasus', 'No. SIPP', 'Tautan Putusan'])
    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
