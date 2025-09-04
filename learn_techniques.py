import streamlit as st

st.set_page_config(page_title="Cooking Techniques | OTMS", layout="wide")

st.markdown("""
    <style>
    [data-testid="stSidebar"] { display: none; }
    .center-text { text-align: center; margin-top: 20px; margin-bottom: 30px; }
    .description-box { background-color: #e8f8ff; border-radius: 15px; padding: 30px;
        margin: 20px auto; width: 70%; font-size: 20px; line-height: 1.6;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1); }
    .nav-buttons { text-align: center; margin-top: 40px; }
    .nav-buttons a { display: inline-block; padding: 12px 24px; margin: 0 10px;
        background-color: #3498db; color: white; font-weight: bold; border-radius: 8px;
        text-decoration: none; transition: background-color 0.3s ease; }
    .nav-buttons a:hover { background-color: #2980b9; }
    </style>
""", unsafe_allow_html=True)

header_cols = st.columns([1,4,1])
with header_cols[0]:
    st.image("otms_assets/otms_logo_light.png", use_container_width=True)
with header_cols[1]:
    st.markdown("<div class='center-text'><h1>BASIC TO PRO COOKING</h1></div>", unsafe_allow_html=True)
with header_cols[2]:
    st.image("otms_assets/cookfinity_logo_light.png", use_container_width=True)

st.markdown("""
    <div class='description-box'>
        From chopping techniques to advanced restaurant-style cooking,
        explore step-by-step lessons to elevate your cooking skills.
        OTMS guides you from beginner to pro!
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div class='nav-buttons'>
        <a href="/learn" target="_self">⬅ Back to Learn</a>
        <a href="/home" target="_self">🏠 Home</a>
    </div>
""", unsafe_allow_html=True)
