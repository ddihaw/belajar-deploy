# Menggunakan image Python sebagai dasar
FROM python:3.9

# Menentukan direktori kerja di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt requirements.txt

# Menginstal semua dependensi yang ada di requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin semua file dari direktori lokal ke dalam direktori kerja di container
COPY . .

# Menentukan variabel lingkungan untuk Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development  # Opsional, untuk mode pengembangan

# Menentukan port yang digunakan oleh container
EXPOSE 5000

# Menjalankan perintah untuk menjalankan aplikasi Flask
CMD ["flask", "run", "--host=0.0.0.0"]
