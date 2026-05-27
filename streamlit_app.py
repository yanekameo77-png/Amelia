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
st.markdown(
    """
    <style>
    body {
        font-family: Arial;
    }

    .kotak {
        width: 100%;
        height: 240px;
        border: 3px solid #1f77b4;
        border-radius: 15px;
        position: relative;
        overflow: hidden;
        background-color: #eef7ff;
        margin-bottom: 20px;
    }

    .bola {
        width: 18px;
        height: 18px;
        background-color: #1f77b4;
        border-radius: 50%;
        position: absolute;
        animation: gerak 5s linear infinite alternate;
    }

    @keyframes gerak {
        0% {transform: translate(0px,0px);} 
        20% {transform: translate(250px,30px);} 
        40% {transform: translate(120px,120px);} 
        60% {transform: translate(300px,170px);} 
        80% {transform: translate(50px,100px);} 
        100% {transform: translate(180px,190px);} 
    }

    .rumus {
        background-color: #f0f0f0;
        padding: 15px;
        border-radius: 10px;
        font-size: 24px;
        text-align: center;
        margin-top: 10px;
        font-weight: bold;
    }

    .hasil {
        background-color: #d4edda;
        padding: 20px;
        border-radius: 10px;
        font-size: 28px;
        text-align: center;
        color: #155724;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# JUDUL
# =========================
st.title("Simulasi Gas Ideal - Massa Jenis Gas Oksigen")

st.write(
    """
### Contoh Soal

Berapakah massa jenis gas oksigen pada tekanan **1520 Torr**
dan suhu **25°C**?

### Diketahui:
- Massa atom O = 16 g/mol
- Mr O₂ = 32 g/mol
- Tekanan = 1520 Torr
- Suhu = 25°C
"""
)

# =========================
# ANIMASI PARTIKEL GAS
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
.b1 {
    animation: gerak1 6s linear infinite alternate;
}

.b2 {
    animation: gerak2 4s linear infinite alternate;
}

.b3 {
    animation: gerak3 5s linear infinite alternate;
}

.b4 {
    animation: gerak4 7s linear infinite alternate;
}

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
# RUMUS
# =========================
st.subheader("Persamaan Gas Ideal")

st.markdown(
    '<div class="rumus">PV = nRT</div>',
    unsafe_allow_html=True
)

st.write(
    "Karena yang dicari massa jenis (ρ), maka persamaan diubah menjadi:"
)

st.latex(r"\rho = \frac{PM}{RT}")

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
