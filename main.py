
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('cats.html')

@app.route('/cats')
def cats():
    conn = sqlite3.connect('cats.db')
    c = conn.cursor()
    c.execute('SELECT * FROM cats')
    cats = c.fetchall()
    conn.close()
    return render_template('cats.html', cats=cats)

@app.route('/breeds/<breed_id>')
def breeds(breed_id):
    conn = sqlite3.connect('cats.db')
    c = conn.cursor()
    c.execute('SELECT * FROM breeds WHERE id=?', (breed_id,))
    breed = c.fetchone()
    conn.close()
    return render_template('breeds.html', breed=breed)

if __name__ == '__main__':
    app.run(debug=True)
