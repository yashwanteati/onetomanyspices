import streamlit as st
from pathlib import Path
import base64

# ---------------- Page Settings ----------------
st.set_page_config(page_title="About OTMS | One to Many Spices", layout="wide")

# ---------------- CSS Styling ----------------
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    .center-text {
        text-align: center;
        margin-top: 20px;
        margin-bottom: 30px;
    }
    .description-box {
        background-color: #fff8e7;
        border-radius: 15px;
        padding: 30px;
        margin: 20px auto;
        width: 70%;
        font-size: 20px;
        line-height: 1.6;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }
    .nav-buttons {
        text-align: center;
        margin-top: 40px;
    }
    .nav-buttons a {
        display: inline-block;
        padding: 12px 24px;
        margin: 0 10px;
        background-color: #f9b24e;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        text-decoration: none;
        transition: background-color 0.3s ease;
    }
    .nav-buttons a:hover {
        background-color: #ff914d;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Header Section (Logos + Title) ----------------
header_cols = st.columns([1, 4, 1])
with header_cols[0]:
    st.image("otms_assets/otms_logo_light.png", use_container_width=True)
with header_cols[1]:
    st.markdown("""
        <div class='center-text'>
            <h1 style='font-size: 48px;'>ABOUT OTMS</h1>
            <h4 style='letter-spacing: 10px; font-size: 22px; margin-top: -10px;'>
                LEARN ABOUT OUR JOURNEY, BLENDS, AND VISION
            </h4>
        </div>
    """, unsafe_allow_html=True)
with header_cols[2]:
    st.image("otms_assets/cookfinity_logo_light.png", use_container_width=True)

# ---------------- Description Section ----------------
st.markdown("""
    <div class='description-box'>
        Welcome to One to Many Spices (OTMS) — the world's first one-stop food app and spice brand.
        Our mission is to simplify cooking by offering expertly crafted spice blends that bring restaurant-quality
        flavors to your kitchen. Whether you're a beginner or a seasoned chef, OTMS is here to help you
        <b>Learn, Cook, Shop, Create, and Engage</b> with food like never before.
        <br><br>
        Explore our spice blends, discover cooking techniques, and be part of a growing food-loving community!
    </div>
""", unsafe_allow_html=True)

# ---------------- Navigation Buttons ----------------
st.markdown("""
    <div class='nav-buttons'>
        <a href="/learn" target="_self">⬅ Back to Learn</a>
        <a href="/home" target="_self">🏠 Home</a>
    </div>
""", unsafe_allow_html=True)
