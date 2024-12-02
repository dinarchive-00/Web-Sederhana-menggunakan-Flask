from flask import Flask, render_template

app = Flask(__name__)

# Route untuk landing page
@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/krs")
def krs():
    return render_template("krs.html")

# Route dinamis untuk halaman lain
@app.route("/<page>")
def index(page):
    # Pilih template berdasarkan halaman
    if page == "DataDiri":
        content_template = "data_diri.html"
    elif page == "KRS":
        content_template = "krs.html"
    elif page == "DaftarNilai":
        content_template = "daftar_nilai.html"
    elif page == "LaporanNilai":
        content_template = "laporan_nilai.html"
    elif page == "GrafikIPK":
        content_template = "grafik_ipk.html"
    else:
        return render_template("404.html"), 404  # Halaman tidak ditemukan

    return render_template("index.html", page=page, content_template=content_template)

if __name__ == "__main__":
    app.run(debug=True)