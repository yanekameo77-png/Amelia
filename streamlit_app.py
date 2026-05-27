# =========================
# STYLE CSS MODERN
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




