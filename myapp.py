from flask import Flask, jsonify, render_template
from flask_mysqldb import MySQL

# Inisialisasi Flask app
app = Flask(__name__)

# Konfigurasi koneksi ke database MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskmysql'  # pastikan nama database sesuai di phpMyAdmin

# Inisialisasi MySQL
mysql = MySQL(app)

# Route utama - tampilkan halaman HTML
@app.route('/')
def index():
    return render_template('index.html')

# Route API - ambil data users dalam format JSON
@app.route('/api/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()

    users = []
    for row in data:
        users.append({
            'id': row[0],
            'username': row[1],
            'password': row[2],
            'email': row[3],
            'alamat': row[4],
            'no_telp': row[5]
        })

    return jsonify(users)

# Jalankan server Flask
if __name__ == '__main__':
    app.run(debug=True)
