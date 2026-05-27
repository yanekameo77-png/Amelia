try:
    import streamlit as st
    import streamlit.components.v1 as components
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "Streamlit belum terinstall. Jalankan: pip install streamlit"
    )

import time

# ====================================
# KONFIGURASI HALAMAN
# ====================================

st.set_page_config(
    page_title="Simulasi Gas Ideal",
    layout="centered"
)

# ====================================
# JUDUL
# ====================================

st.title("⚛️ Simulasi Gas Ideal")

st.write("""
### Contoh Soal

Berapakah massa jenis gas oksigen pada:
- Tekanan = 1520 Torr
- Suhu = 25°C

Diketahui:
- Massa atom O = 16 g/mol
- Mr O₂ = 32 g/mol
""")

# ====================================
# SLIDER SUHU
# ====================================

suhu_animasi = st.slider(
    "🌡️ Atur Suhu Gas (K)",
    100,
    1000,
    300
)

# Semakin tinggi suhu → semakin cepat
kecepatan = max(1, 12 - (suhu_animasi / 100))

st.write(
    f"Semakin tinggi suhu ({suhu_animasi} K), "
    "partikel bergerak semakin cepat."
)

# ====================================
# HTML + CSS ANIMASI
# ====================================

html_code = f"""
<!DOCTYPE html>
<html>
<head>

<style>

body {{
    margin: 0;
    overflow: hidden;
    background-color: transparent;
}}

.kotak {{
    width: 100%;
    height: 400px;
    border-radius: 20px;
    position: relative;
    overflow: hidden;

    background:
    radial-gradient(circle at center,
    #1e3a8a,
    #020617);

    border: 2px solid cyan;

    box-shadow:
    0px 0px 20px rgba(0,255,255,0.4);
}}

.bola {{
    width: 18px;
    height: 18px;
    border-radius: 50%;
    position: absolute;

    background: cyan;

    box-shadow:
    0 0 15px cyan,
    0 0 25px cyan;
}}

.b1 {{
    animation: gerak1 {kecepatan}s linear infinite alternate;
}}

.b2 {{
    animation: gerak2 {kecepatan*0.8}s linear infinite alternate;
}}

.b3 {{
    animation: gerak3 {kecepatan*1.2}s linear infinite alternate;
}}

.b4 {{
    animation: gerak4 {kecepatan*0.6}s linear infinite alternate;
}}

@keyframes gerak1 {{

    from {{
        transform: translate(0px,0px);
    }}

    to {{
        transform: translate(300px,220px);
    }}
}}

@keyframes gerak2 {{

    from {{
        transform: translate(0px,200px);
    }}

    to {{
        transform: translate(280px,-50px);
    }}
}}

@keyframes gerak3 {{

    from {{
        transform: translate(150px,0px);
    }}

    to {{
        transform: translate(-100px,230px);
    }}
}}

@keyframes gerak4 {{

    0% {{
        transform: translate(0px,0px);
    }}

    25% {{
        transform: translate(200px,50px);
    }}

    50% {{
        transform: translate(100px,200px);
    }}

    75% {{
        transform: translate(250px,120px);
    }}

    100% {{
        transform: translate(50px,250px);
    }}
}}

</style>

</head>

<body>

<div class="kotak">

    <div class="bola b1"
    style="left:20px; top:20px;">
    </div>

    <div class="bola b2"
    style="left:100px; top:80px;">
    </div>

    <div class="bola b3"
    style="left:200px; top:140px;">
    </div>

    <div class="bola b4"
    style="left:300px; top:50px;">
    </div>

    <div class="bola b1"
    style="left:400px; top:180px;">
    </div>

    <div class="bola b2"
    style="left:500px; top:120px;">
    </div>

    <div class="bola b3"
    style="left:600px; top:220px;">
    </div>

</div>

</body>
</html>
"""

# ====================================
# TAMPILKAN ANIMASI
# ====================================

components.html(
    html_code,
    height=420
)

# ====================================
# PERSAMAAN GAS IDEAL
# ====================================

st.subheader("📘 Persamaan Gas Ideal")


::contentReference[oaicite:0]{index=0}


st.write(
    "Karena yang dicari massa jenis (ρ), "
    "maka persamaan diubah menjadi:"
)

:contentReference[oaicite:1]{index=1}

# ====================================
# LANGKAH PENYELESAIAN
# ====================================

st.subheader("🧮 Langkah Penyelesaian")

st.write("### 1. Mengubah tekanan dari Torr ke atm")

:contentReference[oaicite:2]{index=2}

st.write("### 2. Mengubah suhu ke Kelvin")

:contentReference[oaicite:3]{index=3}

st.write("### 3. Menentukan massa molar gas oksigen")

:contentReference[oaicite:4]{index=4}

st.write("### 4. Memasukkan ke rumus massa jenis")

:contentReference[oaicite:5]{index=5}

# ====================================
# PERHITUNGAN
# ====================================

P = 2
M = 32
R = 0.082
T = 298

hasil = (P * M) / (R * T)

# ====================================
# TOMBOL HASIL
# ====================================

if st.button("🚀 Tampilkan Hasil"):

    progress = st.progress(0)

    for i in range(100):

        time.sleep(0.01)

        progress.progress(i + 1)

    st.success("Perhitungan selesai!")

    st.markdown(
        f'''
        <div style="
        background:linear-gradient(to right,#22c55e,#16a34a);
        padding:20px;
        border-radius:15px;
        text-align:center;
        font-size:32px;
        color:white;
        font-weight:bold;
        box-shadow:0px 0px 20px rgba(0,255,0,0.5);
        ">
        Massa Jenis Gas O₂ = {hasil:.2f} g/L
        </div>
        ''',
        unsafe_allow_html=True
    )

    st.balloons()

# ====================================
# KESIMPULAN
# ====================================

st.subheader("📌 Kesimpulan")

st.write(f"""

Berdasarkan persamaan gas ideal:

PV = nRT

maka massa jenis gas oksigen pada:
- tekanan 1520 Torr
- suhu 25°C

adalah:

# {hasil:.2f} g/L

""")

# ====================================
# TEST
# ====================================

assert round(hasil, 2) == 2.62, (
    "Hasil perhitungan tidak sesuai"
)
