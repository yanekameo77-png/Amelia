st.markdown("""
<style>

/* ==========================
   FLOATING CALCULATOR ICONS
   ========================== */

.floating-bg{
    position: fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    overflow:hidden;
    z-index:-1;
    pointer-events:none;
}

.floating-bg span{
    position:absolute;
    display:block;
    color:rgba(255,255,255,0.05);
    font-size:40px;
    animation:floatCalc linear infinite;
}

.floating-bg span:nth-child(1){
    left:10%;
    animation-duration:20s;
    font-size:50px;
}

.floating-bg span:nth-child(2){
    left:25%;
    animation-duration:25s;
    animation-delay:-5s;
}

.floating-bg span:nth-child(3){
    left:45%;
    animation-duration:18s;
    font-size:60px;
}

.floating-bg span:nth-child(4){
    left:65%;
    animation-duration:22s;
    animation-delay:-10s;
}

.floating-bg span:nth-child(5){
    left:85%;
    animation-duration:28s;
}

@keyframes floatCalc{

    0%{
        transform:
        translateY(110vh)
        rotate(0deg);

        opacity:0;
    }

    15%{
        opacity:0.08;
    }

    85%{
        opacity:0.08;
    }

    100%{
        transform:
        translateY(-120px)
        rotate(360deg);

        opacity:0;
    }
}

</style>

<div class="floating-bg">
    <span>🧮</span>
    <span>⚗️</span>
    <span>📈</span>
    <span>🧮</span>
    <span>📊</span>
</div>

""", unsafe_allow_html=True)
