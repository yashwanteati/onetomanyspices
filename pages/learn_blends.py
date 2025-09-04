import streamlit as st
from pathlib import Path
import base64

# ---------------- Page Settings ----------------
st.set_page_config(page_title="Learn Blends | One to Many Spices", layout="wide")

# ---------------- CSS Styling ----------------
st.markdown(    """
    <style>
    .stApp, body { background: #0b0d10 !important; color: #e9eef4 !important; }
    [data-testid="stSidebar"] { display: none !important; }
    .block-container { padding-top: 1.2rem; max-width: 1300px; }
    <style>
    [data-testid="stSidebar"] {
        display: none;
    }

    .button-img {
        border-radius: 20px;
        transition: transform 0.3s ease-in-out;
        cursor: pointer;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.2);
    }

    .button-img:hover {
        transform: scale(1.1);
    }

    .menu-button {
        text-align: center;
        margin-top: 20px;
    }

    h1 {
        text-align: center;
        font-size: 48px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Helper Function ----------------
def img_to_base64(path):
    try:
        return base64.b64encode(Path(path).read_bytes()).decode()
    except Exception:
        return ""

# ---------------- Load Blend Images ----------------
blend_images = {
    "red": img_to_base64("otms_assets/red_blend.png"),
    "white": img_to_base64("otms_assets/white_blend.png"),
    "yellow": img_to_base64("otms_assets/yellow_blend.png"),
    "brown": img_to_base64("otms_assets/brown_blend.png"),
    "green": img_to_base64("otms_assets/green_blend.png"),
    "gray": img_to_base64("otms_assets/gray_blend.png"),
}

# ---------------- Page Header ----------------
header_cols = st.columns([1, 4, 1])
with header_cols[0]:
    st.image("otms_assets/otms_logo_dark.png", use_container_width=True)

with header_cols[1]:
    st.markdown("<h1>EXPLORE OUR BLENDS</h1>", unsafe_allow_html=True)

with header_cols[2]:
    st.image("otms_assets/cookfinity_logo_dark.png", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- Blend Config ----------------
blends = [
    {"name": "RED Blend", "page": "blend_red", "img": blend_images["red"]},
    {"name": "WHITE Blend", "page": "blend_white", "img": blend_images["white"]},
    {"name": "YELLOW Blend", "page": "blend_yellow", "img": blend_images["yellow"]},
    {"name": "BROWN Blend", "page": "blend_brown", "img": blend_images["brown"]},
    {"name": "GREEN Blend", "page": "blend_green", "img": blend_images["green"]},
    {"name": "GRAY Blend", "page": "blend_gray", "img": blend_images["gray"]},
]

# ---------------- Render 6 Blends in 2 Rows ----------------
for row in range(2):
    cols = st.columns(3)
    for i, col in enumerate(cols):
        idx = row * 3 + i
        if idx < len(blends):
            blend = blends[idx]
            b64_img = blend["img"]
            if b64_img:
                with col:
                    st.markdown(
                        f"""
                        <div class="menu-button">
                            <a href="/{blend['page']}" target="_self">
                                <img src="data:image/png;base64,{b64_img}" 
                                     class="button-img" 
                                     style="height: 250px; width: 250px; object-fit: cover;">
                            </a>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                col.warning(f"Image not found for {blend['name']}")