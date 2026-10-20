from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def beranda():
    return render_template("index.html")


@app.route("/tentang")
def tentang():
    return "<h1>Tentang</h1><p>Ini adalah halaman tentang website saya.</p>"


@app.route("/kontak")
def kontak():
    return "<h1>Kontak</h1><p>Silakan hubungi saya melalui halaman kontak.</p>"


if __name__ == "__main__":
    app.run(debug=True)