try:
    import streamlit as st
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "Streamlit belum terinstall. Jalankan perintah: pip install streamlit"
    )

import time

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Animasi Gas Ideal",
    layout="centered"
)

# =========================
# STYLE CSS
# =========================
st.markdown("""
<style>

.main {
    background: linear-gradient(to bottom, #0f172a, #1e293b);
    color: white;
}

.kotak {
    width: 100%;
    height: 350px;
    border-radius: 20px;
    position: relative;
    overflow: hidden;
    background: radial-gradient(circle, #1e3a8a, #020617);
    box-shadow: 0px 0px 30px rgba(0,255,255,0.3);
    border: 2px solid cyan;
}

/* PARTIKEL */
.bola {
    width: 18px;
    height: 18px;
    border-radius: 50%;
    position: absolute;
    background: cyan;
    box-shadow: 0 0 15px cyan;
}

/* ANIMASI BERBEDA */
st.markdown(f"""
<style>

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

</style>
""", unsafe_allow_html=True)

/* KEYFRAMES */
@keyframes gerak1 {
    0% {transform: translate(0,0);}
    100% {transform: translate(300px,220px);}
}

@keyframes gerak2 {
    0% {transform: translate(0,200px);}
    100% {transform: translate(280px,-50px);}
}

@keyframes gerak3 {
    0% {transform: translate(150px,0);}
    100% {transform: translate(-100px,230px);}
}

@keyframes gerak4 {
    0% {transform: translate(0,0);}
    25% {transform: translate(200px,50px);}
    50% {transform: translate(100px,200px);}
    75% {transform: translate(250px,120px);}
    100% {transform: translate(50px,250px);}
}

/* KOTAK HASIL */
.hasil {
    background: linear-gradient(to right, #22c55e, #16a34a);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 32px;
    color: white;
    font-weight: bold;
    box-shadow: 0px 0px 20px rgba(0,255,0,0.5);
    animation: muncul 1s ease-in-out;
}

@keyframes muncul {
    from {
        opacity: 0;
        transform: scale(0.5);
    }

    to {
        opacity: 1;
        transform: scale(1);
    }
}

</style>
""", unsafe_allow_html=True)
# =========================
# ANIMASI PARTIKEL GAS
# =========================
st.subheader("⚛️ Simulasi Partikel Gas Ideal")

html_partikel = ""

kelas = ["b1", "b2", "b3", "b4"]

for i in range(20):

    left = (i * 30) % 500
    top = (i * 20) % 250

    kelas_animasi = kelas[i % 4]

    html_partikel += f'''
    <div class="bola {kelas_animasi}"
    style="left:{left}px; top:{top}px;">
    </div>
    '''

st.markdown(
    f'<div class="kotak">{html_partikel}</div>',
    unsafe_allow_html=True
)

# =========================
# SLIDER SUHU
# =========================

suhu_animasi = st.slider(
    "Atur Suhu Gas (K)",
    100,
    1000,
    300
)

# Semakin tinggi suhu → semakin cepat
kecepatan = 12 - (suhu_animasi / 100)

# Batas minimum
if kecepatan < 1:
    kecepatan = 1
# =========================
# LANGKAH PENYELESAIAN
# =========================
st.subheader("Langkah Penyelesaian")

st.write("### 1. Mengubah tekanan dari Torr ke atm")

st.latex(r"P = \frac{1520}{760} = 2\ atm")

st.write("### 2. Mengubah suhu ke Kelvin")

st.latex(r"T = 25 + 273 = 298\ K")

st.write("### 3. Menentukan massa molar oksigen")

st.latex(r"M_{O_2} = 2 \times 16 = 32\ g/mol")

st.write("### 4. Memasukkan nilai ke rumus massa jenis")

st.latex(r"\rho = \frac{PM}{RT}")

st.latex(r"\rho = \frac{(2)(32)}{(0.082)(298)}")

# =========================
# PERHITUNGAN OTOMATIS
# =========================
P = 2
M = 32
R = 0.082
T = 298

hasil = (P * M) / (R * T)

# =========================
# TOMBOL HASIL
# =========================
if st.button("Tampilkan Hasil Perhitungan"):

    progress = st.progress(0)

    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    st.success("Perhitungan selesai!")

    st.markdown(
        f'<div class="hasil">Massa Jenis Gas O₂ = {hasil:.2f} g/L</div>',
        unsafe_allow_html=True
    )

    st.balloons()

# =========================
# KESIMPULAN
# =========================
st.subheader("Kesimpulan")

st.write(
    f"""
Berdasarkan persamaan gas ideal:

PV = nRT

maka massa jenis gas oksigen pada tekanan 1520 Torr
 dan suhu 25°C adalah:

## {hasil:.2f} g/L
"""
)

# =========================
# TEST SEDERHANA
# =========================
assert round(hasil, 2) == 2.62, "Hasil perhitungan tidak sesuai"
