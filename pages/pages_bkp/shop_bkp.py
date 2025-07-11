import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="Shop | One to Many Spices", layout="wide")

# ---------------- Hide Sidebar ----------------
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }
    .blend-card {
        background-color: white;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 2px 4px 12px rgba(0,0,0,0.1);
        text-align: center;
        transition: transform 0.2s ease;
    }
    .blend-card:hover {
        transform: scale(1.03);
    }
    .blend-title {
        font-size: 22px;
        font-weight: bold;
        margin: 12px 0 5px 0;
    }
    .blend-desc {
        font-size: 14px;
        color: #666;
        margin-bottom: 12px;
    }
    .buy-btn {
        background-color: #FF3C38;
        color: white;
        padding: 8px 18px;
        border: none;
        border-radius: 10px;
        font-weight: bold;
        text-decoration: none;
    }
    .buy-btn:hover {
        background-color: #cc2c2a;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Helper Function ----------------
def img_to_base64(path):
    try:
        return base64.b64encode(Path(path).read_bytes()).decode()
    except:
        return ""

# ---------------- Header ----------------
header_cols = st.columns([1, 4, 1])
with header_cols[0]:
    st.image("otms_assets/otms_logo_light.png", use_container_width=True)
with header_cols[1]:
    st.markdown("""
        <div style='text-align: center; margin-top: 20px;'>
            <h1 style='font-size: 48px;'>SHOP OUR SPICE BLENDS</h1>
            <p style='font-size: 18px; color: #555;'>Discover, Order & Enjoy the Flavors of OTMS</p>
        </div>
    """, unsafe_allow_html=True)
with header_cols[2]:
    st.image("otms_assets/cookfinity_logo_light.png", use_container_width=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------- Blend Cards ----------------
blends = [
    {"name": "RED Blend", "desc": "Perfect for fiery curries and marinades.", "img": "otms_assets/red_blend.png"},
    {"name": "YELLOW Blend", "desc": "Bright, aromatic, ideal for dals and vegetables.", "img": "otms_assets/yellow_blend.png"},
    {"name": "WHITE Blend", "desc": "Creamy base masala without overpowering color.", "img": "otms_assets/white_blend.png"},
    {"name": "GREEN Blend", "desc": "Fresh herbaceous punch for greens and chutneys.", "img": "otms_assets/green_blend.png"},
    {"name": "BROWN Blend", "desc": "Bold, earthy notes for gravies and biryanis.", "img": "otms_assets/brown_blend.png"},
    {"name": "GRAY Blend", "desc": "Replaces ginger-garlic paste—clean and powerful.", "img": "otms_assets/gray_blend.png"},
]

rows = [blends[i:i+3] for i in range(0, len(blends), 3)]
for row in rows:
    cols = st.columns(3)
    for col, blend in zip(cols, row):
        with col:
            base64_img = img_to_base64(blend["img"])
            if base64_img:
                col.markdown(f"<div class='blend-card'>", unsafe_allow_html=True)
                col.markdown(f"<img src='data:image/png;base64,{base64_img}' width='100%' style='border-radius:12px;'/>", unsafe_allow_html=True)
                col.markdown(f"<div class='blend-title'>{blend['name']}</div>", unsafe_allow_html=True)
                col.markdown(f"<div class='blend-desc'>{blend['desc']}</div>", unsafe_allow_html=True)
                col.markdown(f"<a href='#' class='buy-btn'>Buy Now</a>", unsafe_allow_html=True)
                col.markdown("</div>", unsafe_allow_html=True)

# ---------------- Footer ----------------
st.markdown("<br><hr><br>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>✨ Limited Edition Gift Packs Coming Soon!</h4>", unsafe_allow_html=True)
