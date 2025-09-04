import streamlit as st
from pathlib import Path
import base64
from PIL import Image

st.set_page_config(page_title="GRAY Blend | One to Many Spices", layout="wide")

# --- Styling ---
st.markdown("""
    <style>
    .stApp, body { background: #0b0d10 !important; color: #e9eef4 !important; }
    [data-testid="stSidebar"] { display: none !important; }
    .block-container { padding-top: 1.2rem; max-width: 1300px; }

    .button-group {
        display: flex; justify-content: center; gap: 1.5rem; margin-top: 3rem;
    }
    .back-btn, .home-btn {
        font-size: 18px; padding: 0.75rem 1.5rem; border-radius: 10px; border: none;
        cursor: pointer; font-weight: 600; box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .back-btn { background-color: #e3ebf4; }
    .home-btn { background-color: #ffe9ae; }

    .recipe-hover:hover {
        transform: scale(1.05); transition: transform 0.3s ease-in-out;
        box-shadow: 0 8px 20px rgba(0,0,0,0.25);
    }
    .center-blend-img { display: flex; justify-content: center; margin: 1rem 0 2rem; }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("<h1 style='text-align: center;'>GRAY BLEND</h1>", unsafe_allow_html=True)

# Image
try:
    gray_b64 = base64.b64encode(Path("otms_assets/gray_blend.png").read_bytes()).decode()
except Exception:
    gray_b64 = ""
st.markdown(f"""
    <div class='center-blend-img'>
        <img src='data:image/png;base64,{gray_b64}' width='300'>
    </div>
""", unsafe_allow_html=True)

# --- Description Card + Blend-colored button ---
st.markdown("""
    <div style='text-align: center; padding: 20px; background-color: #111419; border-radius: 10px; margin-top: 1.5rem; color: #f5f5f5;'>
        <strong style='color:#ffd700;'>GRAY Blend</strong> is savory, pungent, and versatile—our substitute for ginger-garlic paste.
        It builds depth and umami into curries, stir-fries, and marinades while saving time in the kitchen.
        A bonus: no need to peel or grind fresh paste.<br><br>
        <em>Best used in:</em> <strong>Sambar, Chicken Curries, Veg Stir-Fries</strong>.
        <br><br>
        <a href='/shop' target='_self'>
            <button style='padding: 10px 20px; background-color: #616161; color: white; border: none; border-radius: 6px; font-size: 16px; cursor:pointer;'>
                Shop GRAY Blend
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)

# --- Recipes ---
st.markdown("<h2 style='text-align: center; margin-top: 2rem;'>Recipes Using GRAY Blend</h2>", unsafe_allow_html=True)

cols = st.columns(3)
recipes = [
    {"img": "otms_assets/recipes/South_Indian_Sambar.png",   "link": "/cook?recipe=south_indian_sambar"},
    {"img": "otms_assets/recipes/Gray_Chicken_Curry.png",    "link": "/cook?recipe=gray_chicken_curry"},
    {"img": "otms_assets/recipes/Quick_Veg_StirFry.png",     "link": "/cook?recipe=quick_veg_stirfry"},
]
for col, recipe in zip(cols, recipes):
    with col:
        try:
            b64_image = base64.b64encode(Path(recipe["img"]).read_bytes()).decode()
            col.markdown(f"""
                <a href="{recipe['link']}" target="_self">
                    <img src="data:image/png;base64,{b64_image}" width="340" height="340" class="recipe-hover" style="border-radius: 25px; object-fit: cover;">
                </a>
            """, unsafe_allow_html=True)
        except FileNotFoundError:
            st.warning(f"Image not found: {recipe['img']}")

# --- Back & Home ---
st.markdown("""
<div class="button-group">
    <a href="/shop" target="_self"><button class="back-btn">⬅️ Back to Blends</button></a>
    <a href="/" target="_self"><button class="home-btn">🏡 Home</button></a>
</div>
""", unsafe_allow_html=True)
