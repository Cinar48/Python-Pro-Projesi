from model import atik_ayristirici
from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('Ana_sayfa.html', sonuc=None)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'Dosya bulunamadı', 400

    file = request.files['file']
    if file.filename == '':
        return 'Dosya seçilmedi', 400
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Modeli çalıştır
    
    sonuc = atik_ayristirici(image=file_path)

    # Ana sayfaya sonucu gönder
    return render_template('upload.html', sonuc=sonuc)

app.run(debug=True)


